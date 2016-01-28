// echarts的 control_options
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

// echarts的 control_options
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
