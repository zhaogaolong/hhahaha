#!/usr/bin/env python
# coding:utf8
def main(self, argv):
        # Parse args once to find version and debug settings

        # get_base_parser：获取基本的命令行解析器；
        # 调用add_argument方法实现添加具体命令行参数；
        # 构造参数解析类ArgumentParser的实例parser，然后通过实例调用方法parser.add_argument增加一些固有的参数；
        parser = self.get_base_parser()
        # parse_known_args函数是将解析的参数按属性的方式存储到Namespace对象；
        (options, args) = parser.parse_known_args(argv)
        self.setup_debugging(options.debug)
        api_version_input = True

        # 确定使用API的版本，默认版本为V1；
        if not options.os_volume_api_version:
            # Environment variable OS_VOLUME_API_VERSION was
            # not set and '--os-volume-api-version' option doesn't
            # specify a value.  Fall back to default.
            options.os_volume_api_version = DEFAULT_OS_VOLUME_API_VERSION
            api_version_input = False

        # build available subcommands based on version
        # 根据所使用的API版本，进一步确定API扩展的版本；
        self.extensions = self._discover_extensions(options.os_volume_api_version)
        self._run_extension_hooks('__pre_parse_args__')

        # 创建可利用的subcommands，基于版本；
        subcommand_parser = self.get_subcommand_parser(
            options.os_volume_api_version)
        self.parser = subcommand_parser

        if options.help or not argv:
            subcommand_parser.print_help()
            return 0

        # 命令行参数的解析；
        args = subcommand_parser.parse_args(argv)
        self._run_extension_hooks('__post_parse_args__', args)

        # Short-circuit and deal with help right away.
        if args.func == self.do_help:
            self.do_help(args)
            return 0
        elif args.func == self.do_bash_completion:
            self.do_bash_completion(args)
            return 0

        (os_username, os_password, os_tenant_name, os_auth_url,
         os_region_name, os_tenant_id, endpoint_type, insecure,
         service_type, service_name, volume_service_name,
         username, apikey, projectid, url, region_name, cacert) = (
             args.os_username, args.os_password,
             args.os_tenant_name, args.os_auth_url,
             args.os_region_name, args.os_tenant_id,
             args.endpoint_type, args.insecure,
             args.service_type, args.service_name,
             args.volume_service_name, args.username,
             args.apikey, args.projectid,
             args.url, args.region_name, args.os_cacert)

        if not endpoint_type:
            endpoint_type = DEFAULT_CINDER_ENDPOINT_TYPE

        if not service_type:
            service_type = DEFAULT_CINDER_SERVICE_TYPE
            service_type = utils.get_service_type(args.func) or service_type

        #FIXME(usrleon): Here should be restrict for project id same as
        # for os_username or os_password but for compatibility it is not.

        # 若干参数的相关验证和处理；
        if not utils.isunauthenticated(args.func):
            if not os_username:
                if not username:
                    raise exc.CommandError(
                        "You must provide a username "
                        "via either --os-username or env[OS_USERNAME]")
                else:
                    os_username = username

            if not os_password:
                if not apikey:
                    raise exc.CommandError("You must provide a password "
                                           "via either --os-password or via "
                                           "env[OS_PASSWORD]")
                else:
                    os_password = apikey

            if not (os_tenant_name or os_tenant_id):
                if not projectid:
                    raise exc.CommandError("You must provide a tenant_id "
                                           "via either --os-tenant-id or "
                                           "env[OS_TENANT_ID]")
                else:
                    os_tenant_name = projectid

            if not os_auth_url:
                if not url:
                    raise exc.CommandError(
                        "You must provide an auth url "
                        "via either --os-auth-url or env[OS_AUTH_URL]")
                else:
                    os_auth_url = url

            if not os_region_name and region_name:
                os_region_name = region_name

        if not (os_tenant_name or os_tenant_id):
            raise exc.CommandError(
                "You must provide a tenant_id "
                "via either --os-tenant-id or env[OS_TENANT_ID]")

        if not os_auth_url:
            raise exc.CommandError(
                "You must provide an auth url "
                "via either --os-auth-url or env[OS_AUTH_URL]")

        # 类Client的初始化；
        self.cs = client.Client(options.os_volume_api_version, os_username,
                                os_password, os_tenant_name, os_auth_url,
                                insecure, region_name=os_region_name,
                                tenant_id=os_tenant_id,
                                endpoint_type=endpoint_type,
                                extensions=self.extensions,
                                service_type=service_type,
                                service_name=service_name,
                                volume_service_name=volume_service_name,
                                retries=options.retries,
                                http_log_debug=args.debug,
                                cacert=cacert)

        # 如果所要调用的方法没有标志为unauthenticated，则需要进行身份验证操作；
        try:
            if not utils.isunauthenticated(args.func):
                self.cs.authenticate()
        except exc.Unauthorized:
            raise exc.CommandError("Invalid OpenStack Cinder credentials.")
        except exc.AuthorizationFailure:
            raise exc.CommandError("Unable to authorize user")

        # 实现调用相关方法对Volume API的版本进行验证操作；
        endpoint_api_version = None
        # Try to get the API version from the endpoint URL.  If that fails fall
        # back to trying to use what the user specified via
        # --os-volume-api-version or with the OS_VOLUME_API_VERSION environment
        # variable.  Fail safe is to use the default API setting.
        try:
            endpoint_api_version = \
                self.cs.get_volume_api_version_from_endpoint()
            if endpoint_api_version != options.os_volume_api_version:
                msg = (("Volume API version is set to %s "
                        "but you are accessing a %s endpoint. "
                        "Change its value via either --os-volume-api-version "
                        "or env[OS_VOLUME_API_VERSION]")
                       % (options.os_volume_api_version, endpoint_api_version))
                raise exc.InvalidAPIVersion(msg)
        except exc.UnsupportedVersion:
            endpoint_api_version = options.os_volume_api_version
            if api_version_input:
                logger.warning("Unable to determine the API version via "
                               "endpoint URL.  Falling back to user "
                               "specified version: %s" %
                               endpoint_api_version)
            else:
                logger.warning("Unable to determine the API version from "
                               "endpoint URL or user input.  Falling back to "
                               "default API version: %s" %
                               endpoint_api_version)

        args.func(self.cs, args)
