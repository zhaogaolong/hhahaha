/**
 * Created by Administrator on 2016/1/7.
 */
function cinder_status(url,  manager_option, compute_option){
    //var url =url;
    $.get(url,function(callback, status){
        //console.log(callback,status);
        if (status == 'success') {
            var data = JSON.parse(callback);
            //console.log(status);
            f_name = "cinder"+"_"+data['status']['status'];

            //着个类似 python getattr
            window[f_name]("cinder-status-block","cinder-status-content");
            window[f_name]("cinder-columns-block-status","cinder-columns-block-status-content");

            // api
            cinder_mode = "cinder"+"_"+"service"+"_"+data['status']['api'];
            window[cinder_mode]("cinder-api-columns-block","cinder-api-columns-block-content");

            // consoleauth
            cinder_mode = "cinder"+"_"+"service"+"_"+data['status']['scheduler'];
            window[cinder_mode]("cinder-scheduler-columns-block","cinder-scheduler-columns-block-content");

            // scheduler
            cinder_mode = "cinder"+"_"+"service"+"_"+data['status']['volume'];
            window[cinder_mode]("cinder-volume-columns-block","cinder-volume-columns-block-content");
            cinder_mg_status_echarts(data['manager_node'], manager_option);
            cinder_volume_status_echarts(compute_option);
            delete data;

        }
    });
}


function cinder_up(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('navy-bg widget block-status text-center');
    $("#"+content).text('Ok');
}

function cinder_warning(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('yellow-bg widget block-status text-center');
    $("#"+content).text('Warning');
}
function cinder_critical(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('pink-bg widget block-status text-center');
    $("#"+content).text('Critical');
}

function cinder_down(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('red-bg widget block-status text-center');
    $("#"+content).text('Error');
}

function cinder_service_up(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn navy-bg btn-xs');
    $("#"+block_id).addClass('label navy-bg');
    $("#"+content_id).text('OK');
}

function cinder_service_warning(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn yellow-bg btn-xs');
    $("#"+block_id).addClass('label yellow-bg');
    $("#"+content_id).text('Warning');
}
function cinder_service_critical(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn pink-bg btn-xs');
    $("#"+block_id).addClass('label pink-bg');
    $("#"+content_id).text('Critical');
}
function cinder_service_down(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn red-bg  btn-xs');
    $("#"+block_id).addClass('label red-bg ');
    $("#"+content_id).text('Error');
}

function cinder_mg_status_echarts(mg_data, mg_option){
    var cinder_manager_status = echarts.init(document.getElementById('cinder_manager_status'));
    mg_option.title.text = 'Cinder Mananger';
    //console.log(neutron_manager_status_option);

    // 主机信息
    var host_list = [];

    //这是主机信息和val
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
    mg_option.legend.data = host_list;
    mg_option.color = color_list;
    mg_option.series[0]['data'] = host_dic;
    //console.log(neutron_manager_status_option);

    cinder_manager_status.setOption(mg_option, true);

    delete cinder_manager_status;
    delete host_list;
    delete host_dic;
    delete color_list;
    delete mg_data;


}

function cinder_volume_status_echarts(compute_option){
    var cinder_volume_status = echarts.init(document.getElementById('cinder_volume_status'));

    timeTicket = setInterval(function (){
      var v = (Math.random() * 100).toFixed(2) - 0;
      //console.log(v);
      compute_option.series[0].data[0].value = v;
      cinder_volume_status.setOption(compute_option, true);
      delete v;
    },2000);
    cinder_volume_status.setOption(compute_option);
}


