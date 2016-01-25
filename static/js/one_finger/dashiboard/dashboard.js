/**
 * Created by Administrator on 2015/12/10.
 */

  //require.config({
  //  paths: {
  //      echarts: 'http://echarts.baidu.com/build/dist'
  //  }
  //});
  //require(
  //  [
  //      'echarts',
  //      'echarts/chart/pie' // 使用柱状图就加载bar模块，按需加载
  //  ],
  //  function (ec) {

        // 基于准备好的dom，初始化echarts图表
        //var neutron_manager_status = ec.init(document.getElementById('neutron_manager_status'));
        var neutron_manager_status = echarts.init(document.getElementById('neutron_manager_status'));

        //var neutron_comput_status = ec.init(document.getElementById('neutron_comput_status'));
        var neutron_comput_status = echarts.init(document.getElementById('neutron_comput_status'));
        //
        //var nova_manager_status = ec.init(document.getElementById('nova_manager_status'));\
        var nova_manager_status = echarts.init(document.getElementById('nova_manager_status'));

        //var nova_compute_status = ec.init(document.getElementById('nova_compute_status'));
        var nova_compute_status = echarts.init(document.getElementById('nova_compute_status'));

        //var cinder_manager_status = ec.init(document.getElementById('cinder_manager_status'));
        var cinder_manager_status = echarts.init(document.getElementById('cinder_manager_status'));


        //var cinder_volume_status = ec.init(document.getElementById('cinder_volume_status'));
        var cinder_volume_status = echarts.init(document.getElementById('cinder_volume_status'));

        //var ceph_mon_status = ec.init(document.getElementById('ceph_mon_status'));
        var ceph_mon_status = echarts.init(document.getElementById('ceph_mon_status'));

        //var ceph_osd_status = ec.init(document.getElementById('ceph_osd_status'));
        var ceph_osd_status = echarts.init(document.getElementById('ceph_osd_status'));


        var manager_option = new Object(

            {
            backgroundColor: '#e7eaec',
            title : {
                text: 'Ntueron Manager',
                x:'center'
            },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                x: 'left',
                //left: 'left',
                //top : 'bottom',

                data:['M1','M2','M3']
            },

            color: ['#1ab394', '#ea394c'],
            series: [
                {
                    name:'服务器',
                    type:'pie',
                    radius: ['40%', '70%'],
                    avoidLabelOverlap: false,
                    label: {
                        normal: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            show: true,
                            textStyle: {
                                fontSize: '30',
                                fontWeight: 'bold'
                            }
                        }
                    },
                    labelLine: {
                        normal: {
                            show: true
                        }
                    },

                    itemStyle: {
                        normal: {
                            borderColor: 'White',
                            borderWidth: '10'
                        },
                    },

                    center:['50%', '60%'],
                    data:[
                          {value:50, name:'M1'},
                          {value:50, name:'M2'},
                          {value:50, name:'M3'},
                    ]
                }
            ]
        });


        var compute_option = new Object( {
            backgroundColor: '#e7eaec',

            title : {
                text: 'Ntueron Compute',
                //subtext: '纯属虚构',
                x:'center'
            },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                x: 'left',
                //left: 'left',
                //top : 'bottom',

                data:['DOWN','UP']
            },
            color: ['#ea394c','#1ab394'],
            series: [
                {
                    name:'服务器',
                    type:'pie',
                    radius: ['40%', '70%'],
                    avoidLabelOverlap: false,
                    label: {
                        normal: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            show: true,
                            textStyle: {
                                fontSize: '30',
                                fontWeight: 'bold'
                            }
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    itemStyle: {
                        normal: {
                            borderColor: 'White',
                            borderWidth: '10'
                        },
                    },
                    center:['50%', '60%'],
                    data:[
                          {value:10, name:'DOWN'},
                          {value:90, name:'UP'},


                    ]
                }
            ]
        });



        var  volume_status_option= {
              backgroundColor: '#e7eaec',

              tooltip : {
                  formatter: "{a} <br/>{b} : {c}%"
              },
              toolbox: {
                  show : true,
                  feature : {
                      mark : {show: true},
                      restore : {show: false},
                      saveAsImage : {show: false}
                  }
              },
              series : [
                  {
                      name:'使用率',
                      type:'gauge',
                      detail : {
                          formatter:'{value}%',
                          show : true,
                          offsetCenter: ['0', 70], // 设置数据% 的方向位置
                          textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                            color: 'auto',
                            fontSize : 20
                          }
                      },
                      axisLine: {            // 坐标轴线
                            show: true,        // 默认显示，属性show控制显示与否
                            lineStyle: {       // 属性lineStyle控制线条样式
                                color: [[0.6, '#1ab394'],[0.8, '#f7a54a'],[1, '#ec4758' ]],
                                width: 30
                            }
                      },

                      pointer : {
                            length : '60%',
                            width : 3,
                            color : '#16987e'
                      },

                      title : {
                            show : true,
                            offsetCenter: ['0', 110],       // x, y，单位px
                            textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                                color: '#333',
                                fontSize : 20
                            }
                      },

                      data:[{value: 50,  name: '存储使用率'}]
                  }
              ]
          };

        timeTicket = setInterval(function (){
          var v = (Math.random() * 100).toFixed(2) - 0;
          console.log(v);
          volume_status_option.series[0].data[0].value = v;
          cinder_volume_status.setOption(volume_status_option, true);
        },2000);





        var  ceph_osd_status_option= {
              backgroundColor: '#e7eaec',

              tooltip : {
                  formatter: "{a} <br/>{b} : {c}%"
              },
              toolbox: {
                  show : true,
                  feature : {
                      mark : {show: true},
                      restore : {show: false},
                      saveAsImage : {show: false}
                  }
              },
              series : [
                  {
                      name:'使用率',
                      type:'gauge',
                      detail : {
                          formatter:'{value}%',
                          show : true,
                          offsetCenter: ['0', 70], // 设置数据% 的方向位置
                          textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                            color: 'auto',
                            fontSize : 20
                          }
                      },
                      axisLine: {            // 坐标轴线
                            show: true,        // 默认显示，属性show控制显示与否
                            lineStyle: {       // 属性lineStyle控制线条样式
                                color: [[0.6, '#1ab394'],[0.8, '#f7a54a'],[1, '#ec4758' ]],
                                width: 30
                            }
                      },

                      pointer : {
                            length : '60%',
                            width : 3,
                            color : '#16987e'
                      },

                      title : {
                            show : true,
                            offsetCenter: ['0', 110],       // x, y，单位px
                            textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                                color: '#333',
                                fontSize : 20
                            }
                      },

                      data:[{value: 50,  name: '存储使用率'}]
                  }
              ]
          };

        timeTicket = setInterval(function (){
          var v = (Math.random() * 100).toFixed(2) - 0;
          console.log(v);
          ceph_osd_status_option.series[0].data[0].value = v;
          ceph_osd_status.setOption(ceph_osd_status_option, true);
        },2000);





        // 为echarts对象加载数据
        //neutron manager
        var neutron_manager_status_option = manager_option;
        neutron_manager_status_option.title.text = 'Nutron mananger';
        neutron_manager_status.setOption(neutron_manager_status_option);

        //neutron compute
        var neutron_comput_status_option = compute_option;
        neutron_comput_status_option.title.text = 'Nutron Compute';
        neutron_comput_status.setOption(neutron_comput_status_option);

        ////nova
        var nova_manager_status_option = manager_option;
        nova_manager_status_option.title.text = 'Nova  mananger';
        nova_manager_status.setOption(nova_manager_status_option);

        var nova_compute_status_option = compute_option;
        nova_compute_status_option.title.text = 'Nova Compute';
        nova_compute_status.setOption(nova_compute_status_option);
        //
        ////cinder
        var cinder_manager_status_option = manager_option;
        cinder_manager_status_option.title.text = 'Cinder Manager';

        cinder_manager_status.setOption(cinder_manager_status_option);
        cinder_volume_status.setOption(volume_status_option);
        //
        //ceph
        var ceph_mon_status_option = manager_option;
        ceph_mon_status_option.title.text = 'Ceph Mon';
        ceph_mon_status.setOption(ceph_mon_status_option);
        ceph_osd_status.setOption(ceph_osd_status_option);




    //}
  //)
