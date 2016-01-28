/**
 * Created by Administrator on 2016/1/7.
 */

function ceph_status(url, manager_option, compute_option){
    //var url =url;
    $.get(url,function(callback, status){
        //console.log(callback,status);
        if (status == 'success') {
            var data = JSON.parse(callback);
            f_name = "ceph"+"_"+data['status']['status'];
            //着个类似 python getattr
            window[f_name]("ceph-status-block","ceph-status-content");
            window[f_name]("ceph-columns-block-status","ceph-columns-block-status-content");

            // status
            ceph_mode = "ceph"+"_"+"service"+"_"+data['status']['status'];
            window[ceph_mode]("ceph-status-columns-block","ceph-status-columns-block-content");

            // mon
            ceph_mode = "ceph"+"_"+"service"+"_"+data['status']['monitor'];
            window[ceph_mode]("ceph-mon-columns-block","ceph-mon-columns-block-content");

            // osd
            ceph_mode = "ceph"+"_"+"service"+"_"+data['status']['osd'];
            window[ceph_mode]("ceph-osd-columns-block","ceph-osd-columns-block-content");
            ceph_mon_status_echarts(data['mon_node'], manager_option);
            ceph_osd_status_echarts(data['osd_node'], compute_option);

            delete data;
        }
    });
}



function ceph_up(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('navy-bg widget block-status text-center');
    $("#"+content).text('Ok');
}

function ceph_warning(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('yellow-bg widget block-status text-center');
    $("#"+content).text('Warning');
}
function ceph_critical(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('pink-bg widget block-status text-center');
    $("#"+content).text('Critical');
}

function ceph_down(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('red-bg widget block-status text-center');
    $("#"+content).text('Error');
}

function ceph_service_up(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn navy-bg btn-xs');
    $("#"+block_id).addClass('label navy-bg');
    $("#"+content_id).text('OK');
}

function ceph_service_warning(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn yellow-bg btn-xs');
    $("#"+block_id).addClass('label yellow-bg');
    $("#"+content_id).text('Warning');
}
function ceph_service_critical(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn pink-bg btn-xs');
    $("#"+block_id).addClass('label pink-bg');
    $("#"+content_id).text('Critical');
}
function ceph_service_down(block_id,content_id){
    $("#"+content_id).removeClass();
    $("#"+block_id).removeClass();
    $("#"+content_id).addClass('btn red-bg  btn-xs');
    $("#"+block_id).addClass('label red-bg ');
    $("#"+content_id).text('Error');
}



function ceph_mon_status_echarts(mg_data, manager_option){
    var ceph_mon_status = echarts.init(document.getElementById('ceph_mon_status'));
    //var ceph_mon_status_option = manager_option;
    //ceph_mon_status_option.title.text = 'Ceph Monitor';
    manager_option.title.text = 'Ceph Monitor';
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

    ceph_mon_status.setOption(manager_option, true);

    delete ceph_mon_status;
    delete host_list;
    delete host_dic;
    delete color_list;
    delete mg_data;

}

function ceph_osd_status_echarts(compute_data, compute_option){
    var ceph_osd_status = echarts.init(document.getElementById('ceph_osd_status'));
    //var ceph_osd_status_option = compute_option;
    //ceph_osd_status_option.title.text = 'Ceph OSD';
    compute_option.title.text = 'Ceph OSD';
    //console.log(neutron_comput_status_option);
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

    ceph_osd_status.setOption(compute_option, true);

    delete compute_data;
    delete ceph_osd_status;
    delete host_list_up;
    delete host_list_down;
    delete host_list;
    delete host_data;
}
