/**
 * Created by Administrator on 2016/1/7.
 */
function cinder_status(url){
    var url =url;

    $.get(url,function(callback, status){
        //console.log(callback,status);
        if (status == 'success') {
            var data = JSON.parse(callback);
            //console.log(status);
            f_name = "cinder"+"_"+data['status'];

            //着个类似 python getattr
            window[f_name]("cinder-status-block","cinder-status-content");
            window[f_name]("cinder-columns-block-status","cinder-columns-block-status-content");

            // api
            cinder_mode = "cinder"+"_"+"service"+"_"+data['api'];
            window[cinder_mode]("cinder-api-columns-block","cinder-api-columns-block-content");

            // consoleauth
            cinder_mode = "cinder"+"_"+"service"+"_"+data['scheduler'];
            window[cinder_mode]("cinder-scheduler-columns-block","cinder-scheduler-columns-block-content");

            // scheduler
            cinder_mode = "cinder"+"_"+"service"+"_"+data['volume'];
            window[cinder_mode]("cinder-volume-columns-block","cinder-volume-columns-block-content");

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
