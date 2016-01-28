/**
 * Created by Administrator on 2016/1/7.
 */

//status_dic = {
//    'up':up(),
//    'warning': warning(),
//    'critical': critical(),
//    'down': down()
//};
//RefreshMsgs = setInterval(function(){},3000);


function neutron_status(url, manager_option, compute_option){
    //var url =url;
    $.get(url,function(callback, status){
        //console.log(callback,status);
        if (status == 'success') {
            var data = JSON.parse(callback);
            console.log(data);
            n_name = "neutron"+"_"+data['status']['status'];
            //console.log(f_name);
            window[n_name]("neutron-status-block","neutron-status-content");

            // 着是neutron栏中的大的block
            window[n_name]("neutron-columns-block-status","neutron-columns-block-content");

            // l3
            neutron_status_list = "neutron"+"_"+"service"+"_"+data['status']['l3'];
            window[neutron_status_list]("neutron-l3-columns-block","neutron-l3-columns-block-content");

            // dhcp
            neutron_status_list = "neutron"+"_"+"service"+"_"+data['status']['dhcp'];
            window[neutron_status_list]("neutron-dhcp-columns-block","neutron-dhcp-columns-block-content");

            // api
            neutron_status_list = "neutron"+"_"+"service"+"_"+data['status']['api'];
            window[neutron_status_list]("neutron-api-columns-block","neutron-api-columns-block-content");

            //// agetnt
            //neutron_status_list = "neutron"+"_"+"service"+"_"+data['agent'];
            //window[neutron_status_list]("neutron-river-columns-block","neutron-river-columns-block-content");

            // compute
            neutron_status_list = "neutron"+"_"+"service"+"_"+data['status']['compute'];
            window[neutron_status_list]("neutron-compute-columns-block","neutron-compute-columns-block-content");
            neutron_mg_status_echarts(data['manager_node'], manager_option);
            neutron_compute_status_echarts(data['compute_node'], compute_option);
            delete data;
        }
    });
}

function neutron_up(block_id,content){
    $("#"+block_id).removeClass();
    //console.log(content);
    $("#"+block_id).addClass('navy-bg widget block-status text-center ');
    $("#"+content).text('OK');
}

function neutron_warning(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('yellow-bg widget block-status text-center ');
    $("#"+content).text('Warning');
}

function neutron_critical(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('pink-bg widget block-status text-center ');
    $("#"+content).text('Critical');
}

function neutron_down(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('red-bg widget block-status text-center ');
    $("#"+content).text('Error');
}


function neutron_service_up(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn navy-bg btn-xs');
    $("#"+block_id).addClass('label navy-bg');
    $("#"+content_id).text('OK');
}

function neutron_service_warning(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn yellow-bg btn-xs');
    $("#"+block_id).addClass('label yellow-bg');
    $("#"+content_id).text('Warning');
}
function neutron_service_critical(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn pink-bg  btn-xs');
    $("#"+block_id).addClass('label pink-bg');
    $("#"+content_id).text('Critical');
}
function neutron_service_down(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn red-bg btn-xs');
    $("#"+block_id).addClass('label red-bg');
    $("#"+content_id).text('Error');
}


function neutron_mg_status_echarts(mg_data, manager_option){
    var neutron_manager_status = echarts.init(document.getElementById('neutron_manager_status'));
    manager_option.title.text = 'Neutron Mananger';
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
    manager_option.legend.data = host_list;
    manager_option.color = color_list;
    manager_option.series[0]['data'] = host_dic;
    //console.log(neutron_manager_status_option);

    neutron_manager_status.setOption(manager_option, true);

    delete host_list;
    delete host_dic;
    delete color_list;
    delete neutron_manager_status;
    delete mg_data;
}

function neutron_compute_status_echarts(compute_data, compute_option){
    var neutron_comput_status = echarts.init(document.getElementById('neutron_comput_status'));
    compute_option.title.text = 'Neutron Compute';
    //console.log(compute_option);
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

    compute_option.series[0]['data'] = host_data;
    //console.log(neutron_comput_status_option);
    neutron_comput_status.setOption(compute_option, true);

    delete host_list_up;
    delete host_list_down;
    delete host_list;
    delete host_data;
    delete neutron_comput_status;
    delete compute_data;

}
