/**
 * Created by Administrator on 2016/1/7.
 */

function nova_status(url, manager_option, compute_option){
    //var url =url;
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
            nova_mg_status_echarts(data['manager_node'], manager_option);
            nova_compute_status_echarts(data['compute_node'], compute_option);
            delete data;
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


function nova_mg_status_echarts(mg_data, manager_option){
    //console.log();
    var nova_manager_status = echarts.init(document.getElementById('nova_manager_status'));
    manager_option.title.text = 'Nova  Mananger';

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
    manager_option.legend.data = host_list;
    manager_option.color = color_list;
    manager_option.series[0]['data'] = host_dic;
    //console.log(nova_manager_status_option);

    nova_manager_status.setOption(manager_option, true);

    delete nova_manager_status;
    delete host_list;
    delete host_dic;
    delete color_list;
    delete mg_data;


}

function nova_compute_status_echarts(compute_data, compute_option){
    var nova_compute_status = echarts.init(document.getElementById('nova_compute_status'));
    compute_option.title.text = 'Nova  Compute';
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
    compute_option.series[0]['data'] = host_data;
    //console.log(nova_compute_status_option);
    nova_compute_status.setOption(compute_option, true);


    //清除垃圾
    delete nova_compute_status;
    delete host_list_up;
    delete host_list_down;
    delete host_list;
    delete host_data;
    delete compute_data;


}
