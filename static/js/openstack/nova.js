/**
 * Created by Administrator on 2016/1/7.
 */

function nova_status(url){
    var url =url;

    $.get(url,function(callback, status){
        //console.log(callback,status);
        if (status == 'success') {
            var data = JSON.parse(callback);
            f_name = "nova"+"_"+data['status']['status'];
            //着个类似 python getattr
            window[f_name]("nova-status-block","nova-status-content");
            window[f_name]("nova-columns-block-status","nova-columns-block-status-content");


            // api
            nova_mode = "nova"+"_"+"service"+"_"+data['status']['api'];
            window[nova_mode]("nova-api-columns-block","nova-api-columns-block-content");

            // consoleauth
            nova_mode = "nova"+"_"+"service"+"_"+data['status']['consoleauth'];
            window[nova_mode]("nova-consoleauth-columns-block","nova-consoleauth-columns-block-content");

            // scheduler
            nova_mode = "nova"+"_"+"service"+"_"+data['status']['scheduler'];
            window[nova_mode]("nova-scheduler-columns-block","nova-scheduler-columns-block-content");

            // conductor
            nova_mode = "nova"+"_"+"service"+"_"+data['status']['conductor'];
            window[nova_mode]("nova-conductor-columns-block","nova-conductor-columns-block-content");

            // compute
            nova_mode = "nova"+"_"+"service"+"_"+data['status']['compute'];
            window[nova_mode]("nova-compute-columns-block","nova-compute-columns-block-content");
            nova_mg_status_echarts(data['manager_node']);
            nova_compute_status_echarts(data['compute_node']);
        }
    });
}



function nova_up(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('navy-bg widget block-status text-center');
    $("#"+content).text('Ok');
}

function nova_warning(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('yellow-bg widget block-status text-center');
    $("#"+content).text('Warning');
}
function nova_critical(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('pink-bg widget block-status text-center');
    $("#"+content).text('Critical');
}

function nova_down(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('red-bg widget block-status text-center');
    $("#"+content).text('Error');
}

function nova_service_up(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn navy-bg btn-xs');
    $("#"+block_id).addClass('label navy-bg');
    $("#"+content_id).text('OK');
}

function nova_service_warning(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn yellow-bg btn-xs');
    $("#"+block_id).addClass('label yellow-bg');
    $("#"+content_id).text('Warning');
}
function nova_service_critical(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn pink-bg btn-xs');
    $("#"+block_id).addClass('label pink-bg');
    $("#"+content_id).text('Critical');
}
function nova_service_down(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn red-bg  btn-xs');
    $("#"+block_id).addClass('label red-bg ');
    $("#"+content_id).text('Error');
}


function nova_mg_status_echarts(mg_data){
    //console.log();
    var nova_manager_status = echarts.init(document.getElementById('nova_manager_status'));
    var nova_manager_status_option = new control_option();
    nova_manager_status_option.title.text = 'Nova  Mananger';

    // 主机信息
    var host_list = [];
    var host_dic = [];
    var color_list = [];
    $.each(mg_data,function(host, status){
        host_list.push(host);
        host_dic.push({name: host});
        if(status == 'up') {
            color_list.push("#1ab394")
        }
        if(status == 'warning') {
            color_list.push("#f8ac59")
        }
        if(status == 'down') {
            color_list.push("#ea394c")
        }
    });
    //console.log(host_list);
    //console.log(host_dic);
    nova_manager_status_option.legend.data = host_list;
    nova_manager_status_option.color = color_list;
    nova_manager_status_option.series[0]['data'] = host_dic;
    //console.log(nova_manager_status_option);

    nova_manager_status.setOption(nova_manager_status_option, true);
}

function nova_compute_status_echarts(compute_data){
    var nova_compute_status = echarts.init(document.getElementById('nova_compute_status'));
    var nova_compute_status_option = new compute_option();
    nova_compute_status_option.title.text = 'Nova  Compute';
    // 主机信息
    var host_list_up = [];
    var host_list_down = [];
    var host_list = [];
    $.each(compute_data,function(host, status){
        host_list.push(host);
        if(status == 'up') {
            host_list_up.push(host)
        }
        if(status == 'down') {
            host_list_down.push(host)
        }
    });

    var host_data = [
        {value: host_list_up.length, name:'UP'},
        {value: host_list_down.length, name:'DOWN'},

    ];

    //console.log(host_list);
    //console.log(host_dic);
    //nova_compute_status_option.legend.data = host_list;
    //nova_compute_status_option.color = color_list;
    nova_compute_status_option.series[0]['data'] = host_data;
    //console.log(nova_compute_status_option);
    nova_compute_status.setOption(nova_compute_status_option, true);
}
