# One Finger

介绍： One_finger 是基于django框架开发，监测Openstack平台状态，平台自动化恢复等事务




依赖：
ansible 
configure ansible.cfg

/etc/ansible/ansible.cfg 
host_key_checking = False

获取后台信息：
使用django的crontab 来监测后台状态。

监测nova，neutron、cinder、glance、ceph等

注: 如果没有配置在获取主机的时候无法获取信