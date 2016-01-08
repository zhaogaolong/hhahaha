/**
 * Created by Administrator on 2016/1/7.
 */

function ceph_status(url){
    var url =url;

    $.get(url,function(callback, status){
        //console.log(callback,status);
        if (status == 'success') {
            var data = JSON.parse(callback);
            f_name = "ceph"+"_"+data['status'];
            //着个类似 python getattr
            window[f_name]("ceph-status-block","ceph-status-content");
            window[f_name]("ceph-columns-block-status","ceph-columns-block-status-content");

            // status
            ceph_mode = "ceph"+"_"+"service"+"_"+data['status'];
            window[ceph_mode]("ceph-status-columns-block","ceph-status-columns-block-content");

            // mon
            ceph_mode = "ceph"+"_"+"service"+"_"+data['monitor'];
            window[ceph_mode]("ceph-mon-columns-block","ceph-mon-columns-block-content");

            // osd
            ceph_mode = "ceph"+"_"+"service"+"_"+data['osd'];
            window[ceph_mode]("ceph-osd-columns-block","ceph-osd-columns-block-content");
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

