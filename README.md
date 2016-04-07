# One Finger

介绍： One_finger 是基于django框架开发，监测Openstack平台状态，平台自动化恢复等事务




依赖：
ansible 
configure ansible.cfg

/etc/ansible/ansible.cfg 
host_key_checking = False

获取后台信息：

监测nova，neutron、cinder、glance、ceph等

注: 如果没有配置在获取主机的时候无法获取信



shellinaboxd -p 4201 -t -s /192.168.0.3:SSH:192.168.0.3
ps -ef|grep -e 14244df  |grep -v grep  


http://192.168.254.230:4203/?u=root&p=r00tme