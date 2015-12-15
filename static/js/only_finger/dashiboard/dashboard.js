/**
 * Created by Administrator on 2015/12/10.
 */

  require.config({
    paths: {
        echarts: 'http://echarts.baidu.com/build/dist'
    }
  });
  require(
    [
        'echarts',
        'echarts/chart/pie' // 使用柱状图就加载bar模块，按需加载
    ],
    function (ec) {
        // 基于准备好的dom，初始化echarts图表
        var neutron_manager_status = ec.init(document.getElementById('neutron_manager_status'));
        var neutron_comput_status = ec.init(document.getElementById('neutron_comput_status'));

        var nova_manager_status = ec.init(document.getElementById('nova_manager_status'));
        var nova_compute_status = ec.init(document.getElementById('nova_compute_status'));

        var cinder_manager_status = ec.init(document.getElementById('cinder_manager_status'));
        var cinder_volume_status = ec.init(document.getElementById('cinder_volume_status'));

        var ceph_mon_status = ec.init(document.getElementById('ceph_mon_status'));
        var ceph_osd_status = ec.init(document.getElementById('ceph_osd_status'));



        var neutron_manager_status_option= {
            title : {
                text: 'Ntueron Manager Staus',
                //subtext: '纯属虚构',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            color: ['#23c6c8','#16987e' ,'#ea394c'],
            calculable : true,
            series : [
                {

                    //name:'访问来源',
                    type:'pie',
                    radius : [70,'80%'],
                    center: ['50%', '55%'],
                    itemStyle: {
                      normal: {
                        //borderColor: '', //设置间隔的颜色
                        borderWidth: '5',//设置间隔的宽度
                        label: {
                          position: 'inner', //设置提示字体在内部
                          //distance: '0.9', //设置字体在区域的位置，默认是0.5 就是中间
                },
                labelLine: {
                  show: false  //设置外接线关闭
                }
              }
            },
                    data:[
                        {value:50, name:'L3 Agent'},
                        {value:50, name:'DHCP Agent'},

                    ]
                }
            ]
        };
        var neutron_comput_status_option = {
            title : {
                text: 'Ntueron Compuste Staus',
                //subtext: '纯属虚构',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            //color: ['#ea394c#1ab394','rad','#f79d3c', '#ea394c' ],
            color: ['#1ab394', '#f79d3c', '#ea394c'],
            //legend: {
            //    orient : 'vertical',
            //    x : 'left',
            //    data:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎']
            //},
            calculable : true,
            series : [
                {
                    name:'访问来源',
                    type:'pie',
                    startAngle: 45,
                    clockWise: false,
                    radius : [70,'80%'],
                    center: ['50%', '55%'],
                    itemStyle: {
                      normal: {
                        //borderColor: '', //设置间隔的颜色
                        //borderWidth: '5',//设置间隔的宽度
                        label: {
                          position: 'inner', //设置提示字体在内部
                          distance: '0.9', //设置字体在区域的位置，默认是0.5 就是中间
                        },
                        labelLine: {
                          show:false,  //设置外接线关闭
                        }
                      }
                    },
                    data:[
                        {value:80, name:'OK'},
                        {value:5, name:'服务不可用'},
                        //{value:5, name:'服务down'},
                        {value:10, name:'物理机down'},
                        //{value:1548, name:'搜索引擎'}
                    ]
                }
            ]
        };

        var nova_manager_status_option= {
            title : {
                text: 'Ntueron Manager Staus',
                //subtext: '纯属虚构',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            color: ['#23c6c8','#16987e' ,'#ea394c'],
            calculable : true,
            series : [
                {

                    //name:'访问来源',
                    type:'pie',
                    radius : [70,'80%'],
                    center: ['50%', '55%'],
                    itemStyle: {
                      normal: {
                        //borderColor: '', //设置间隔的颜色
                        borderWidth: '5',//设置间隔的宽度
                        label: {
                          position: 'inner', //设置提示字体在内部
                          //distance: '0.9', //设置字体在区域的位置，默认是0.5 就是中间
                },
                labelLine: {
                  show: false  //设置外接线关闭
                }
              }
            },
                    data:[
                        {value:50, name:'L3 Agent'},
                        {value:50, name:'DHCP Agent'},

                    ]
                }
            ]
        };
        var nova_compute_status_option = {
            title : {
                text: 'Ntueron Compuste Staus',
                //subtext: '纯属虚构',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            //color: ['#ea394c#1ab394','rad','#f79d3c', '#ea394c' ],
            color: ['#1ab394', '#f79d3c', '#ea394c'],
            //legend: {
            //    orient : 'vertical',
            //    x : 'left',
            //    data:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎']
            //},
            calculable : true,
            series : [
                {
                    name:'访问来源',
                    type:'pie',
                    startAngle: 45,
                    clockWise: false,
                    radius : [70,'80%'],
                    center: ['50%', '55%'],
                    itemStyle: {
                      normal: {
                        //borderColor: '', //设置间隔的颜色
                        //borderWidth: '5',//设置间隔的宽度
                        label: {
                          position: 'inner', //设置提示字体在内部
                          distance: '0.9', //设置字体在区域的位置，默认是0.5 就是中间
                        },
                        labelLine: {
                          show:false,  //设置外接线关闭
                        }
                      }
                    },
                    data:[
                        {value:80, name:'OK'},
                        {value:5, name:'服务不可用'},
                        //{value:5, name:'服务down'},
                        {value:10, name:'物理机down'},
                        //{value:1548, name:'搜索引擎'}
                    ]
                }
            ]
        };

        var  cinder_manager_status_option= {
            title : {
                text: 'Ntueron Manager Staus',
                //subtext: '纯属虚构',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            color: ['#23c6c8','#16987e' ,'#ea394c'],
            calculable : true,
            series : [
                {

                    //name:'访问来源',
                    type:'pie',
                    radius : [70,'80%'],
                    center: ['50%', '55%'],
                    itemStyle: {
                      normal: {
                        //borderColor: '', //设置间隔的颜色
                        borderWidth: '5',//设置间隔的宽度
                        label: {
                          position: 'inner', //设置提示字体在内部
                          //distance: '0.9', //设置字体在区域的位置，默认是0.5 就是中间
                },
                labelLine: {
                  show: false  //设置外接线关闭
                }
              }
            },
                    data:[
                        {value:50, name:'L3 Agent'},
                        {value:50, name:'DHCP Agent'},

                    ]
                }
            ]
        };
        var  volume_status_option= {
            title : {
                text: 'Ntueron Manager Staus',
                //subtext: '纯属虚构',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            color: ['#23c6c8','#16987e' ,'#ea394c'],
            calculable : true,
            series : [
                {

                    //name:'访问来源',
                    type:'pie',
                    radius : [70,'80%'],
                    center: ['50%', '55%'],
                    itemStyle: {
                      normal: {
                        //borderColor: '', //设置间隔的颜色
                        borderWidth: '5',//设置间隔的宽度
                        label: {
                          position: 'inner', //设置提示字体在内部
                          //distance: '0.9', //设置字体在区域的位置，默认是0.5 就是中间
                },
                labelLine: {
                  show: false  //设置外接线关闭
                }
              }
            },
                    data:[
                        {value:50, name:'L3 Agent'},
                        {value:50, name:'DHCP Agent'},

                    ]
                }
            ]
        };

        var  ceph_mon_status_option= {
            title : {
                text: 'Ntueron Manager Staus',
                //subtext: '纯属虚构',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            color: ['#23c6c8','#16987e' ,'#ea394c'],
            calculable : true,
            series : [
                {

                    //name:'访问来源',
                    type:'pie',
                    radius : [70,'80%'],
                    center: ['50%', '55%'],
                    itemStyle: {
                      normal: {
                        //borderColor: '', //设置间隔的颜色
                        borderWidth: '5',//设置间隔的宽度
                        label: {
                          position: 'inner', //设置提示字体在内部
                          //distance: '0.9', //设置字体在区域的位置，默认是0.5 就是中间
                },
                labelLine: {
                  show: false  //设置外接线关闭
                }
              }
            },
                    data:[
                        {value:50, name:'L3 Agent'},
                        {value:50, name:'DHCP Agent'},

                    ]
                }
            ]
        };

        var  ceph_osd_status_option= {
            title : {
                text: 'Ntueron Manager Staus',
                //subtext: '纯属虚构',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            color: ['#23c6c8','#16987e' ,'#ea394c'],
            calculable : true,
            series : [
                {

                    //name:'访问来源',
                    type:'pie',
                    radius : [70,'80%'],
                    center: ['50%', '55%'],
                    itemStyle: {
                      normal: {
                        //borderColor: '', //设置间隔的颜色
                        borderWidth: '5',//设置间隔的宽度
                        label: {
                          position: 'inner', //设置提示字体在内部
                          //distance: '0.9', //设置字体在区域的位置，默认是0.5 就是中间
                },
                labelLine: {
                  show: false  //设置外接线关闭
                }
              }
            },
                    data:[
                        {value:50, name:'L3 Agent'},
                        {value:50, name:'DHCP Agent'},

                    ]
                }
            ]
        };




        // 为echarts对象加载数据
        //neutron
        neutron_manager_status.setOption(neutron_manager_status_option);
        neutron_comput_status.setOption(neutron_comput_status_option);

        //nova
        nova_manager_status.setOption(nova_manager_status_option);
        nova_compute_status.setOption(nova_compute_status_option);

        //cinder
        cinder_manager_status.setOption(cinder_manager_status_option);
        cinder_volume_status.setOption(volume_status_option);

        //ceph
        ceph_mon_status.setOption(ceph_mon_status_option);
        ceph_osd_status.setOption(ceph_osd_status_option);




    }
  );
