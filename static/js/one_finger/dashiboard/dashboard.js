//var neutron_manager_status = ec.init(document.getElementById('neutron_manager_status'));
//var neutron_manager_status = echarts.init(document.getElementById('neutron_manager_status'));

//var neutron_comput_status = ec.init(document.getElementById('neutron_comput_status'));
//var neutron_comput_status = echarts.init(document.getElementById('neutron_comput_status'));
//
//var nova_manager_status = ec.init(document.getElementById('nova_manager_status'));\
//var nova_manager_status = echarts.init(document.getElementById('nova_manager_status'));

//var nova_compute_status = ec.init(document.getElementById('nova_compute_status'));
//var nova_compute_status = echarts.init(document.getElementById('nova_compute_status'));

//var cinder_manager_status = ec.init(document.getElementById('cinder_manager_status'));
//var cinder_manager_status = echarts.init(document.getElementById('cinder_manager_status'));


//var cinder_volume_status = ec.init(document.getElementById('cinder_volume_status'));
//var cinder_volume_status = echarts.init(document.getElementById('cinder_volume_status'));

//var ceph_mon_status = ec.init(document.getElementById('ceph_mon_status'));
//var ceph_mon_status = echarts.init(document.getElementById('ceph_mon_status'));

//var ceph_osd_status = ec.init(document.getElementById('ceph_osd_status'));
//var ceph_osd_status = echarts.init(document.getElementById('ceph_osd_status'));

function control_option(){
    this.backgroundColor = '#e7eaec';
    this.title = {
        text: 'Ntueron Manager',
        x: 'center'

    };

    this.tooltip = {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
    };

    this.legend = {
            orient: 'vertical',
            x: 'left',
            //left: 'left',
            //top : 'bottom',

            data:['node-x','node-y','node-z']
    };
    this.color = ['#1ab394', '#ea394c', '#1ab394'];
    this.series = [
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
                }
            },

            center:['50%', '60%'],
            data:[
                  {name:'node-x'},
                  {name:'node-y'},
                  {name:'node-z'}
            ]
        }
    ]

}

function compute_option(){
    this.backgroundColor = '#e7eaec';
    this.title = {
        text: 'Compute',
        //subtext: '纯属虚构',
        x:'center'
    };
    this.tooltip = {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    };
    this.legend = {
        orient: 'vertical',
        x: 'left',
        //left: 'left',
        //top : 'bottom',
        data:['DOWN','UP']
    };
    this.color = ['#1ab394', '#ea394c'];
    this.series = [
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
                }
            },
            center:['50%', '60%'],
            data:[
                  {value:10, name:'DOWN'},
                  {value:90, name:'UP'}

            ]
        }
    ]

}

function gauge_option(){
    this.backgroundColor = '#e7eaec';
    this.tooltip = {
        formatter: "{a} <br/>{b} : {c}%"
    };
    this.toolbox = {
        show : true,
        feature : {
            mark : {show: true},
            restore : {show: false},
            saveAsImage : {show: false}
        }
    };

    this.series = [
        {
            name:'使用率',
            type:'gauge',
            detail : {
                formatter:'{value}%',
                show : true,
                offsetCenter: ['0', 70], // 设置数据% 的方向位置
                textStyle: {
                   // 其余属性默认使用全局文本样式，详见TEXTSTYLE
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

}



// 为echarts对象加载数据
//neutron manager
//var neutron_manager_status_option = new control_option();
//neutron_manager_status_option.title.text = 'Nutron Mananger';
//neutron_manager_status.setOption(neutron_manager_status_option);

//neutron compute
//var neutron_comput_status_option = new compute_option();
//neutron_comput_status_option.title.text = 'Nutron Compute';
//neutron_comput_status.setOption(neutron_comput_status_option);

//nova control
//var nova_manager_status_option = new control_option();
//nova_manager_status_option.title.text = 'Nova  mananger';
//nova_manager_status.setOption(nova_manager_status_option);

// nova compute
//var nova_compute_status_option = new compute_option();
//nova_compute_status_option.title.text = 'Nova Compute';
//nova_compute_status.setOption(nova_compute_status_option);

//cinder control
//var cinder_manager_status_option = new control_option();
//cinder_manager_status_option.title.text = 'Cinder Manager';
//cinder_manager_status.setOption(cinder_manager_status_option);

// cinder volume
//var volume_status_option = new gauge_option();

//timeTicket = setInterval(function (){
//  var v = (Math.random() * 100).toFixed(2) - 0;
//  //console.log(v);
//  volume_status_option.series[0].data[0].value = v;
//  cinder_volume_status.setOption(volume_status_option, true);
//},2000);
//cinder_volume_status.setOption(volume_status_option);


//ceph
//var ceph_mon_status_option = new control_option();
//ceph_mon_status_option.title.text = 'Ceph Mon';
//ceph_mon_status.setOption(ceph_mon_status_option);

//ceph_osd_status.setOption(ceph_osd_status_option);

//var ceph_osd_status_option = new gauge_option();
//ceph_osd_status.setOption(ceph_osd_status_option);
//
//timeTicket = setInterval(function (){
//    var v = (Math.random() * 100).toFixed(2) - 0;
//    //console.log(v);
//    ceph_osd_status_option.series[0].data[0].value = v;
//    ceph_osd_status.setOption(ceph_osd_status_option, true);
//},2000);
