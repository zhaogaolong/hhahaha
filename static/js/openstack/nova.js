/**
 * Created by Administrator on 2016/1/7.
 */

function nova_status(url){
    var url =url;

    $.get(url,function(callback, status){
        //console.log(callback,status);
        if (status == 'success') {
            var data = JSON.parse(callback);
            f_name = "nova"+"_"+data['status'];
            //着个类似 python getattr
            window[f_name]("nova-status-block","nova-status-content");
            window[f_name]("nova-columns-block-status","nova-columns-block-status-content");


            // api
            nova_mode = "nova"+"_"+"service"+"_"+data['api'];
            window[nova_mode]("nova-api-columns-block","nova-api-columns-block-content");

            // consoleauth
            nova_mode = "nova"+"_"+"service"+"_"+data['consoleauth'];
            window[nova_mode]("nova-consoleauth-columns-block","nova-consoleauth-columns-block-content");

            // scheduler
            nova_mode = "nova"+"_"+"service"+"_"+data['scheduler'];
            window[nova_mode]("nova-scheduler-columns-block","nova-scheduler-columns-block-content");

            // conductor
            nova_mode = "nova"+"_"+"service"+"_"+data['conductor'];
            window[nova_mode]("nova-conductor-columns-block","nova-conductor-columns-block-content");

            // compute
            nova_mode = "nova"+"_"+"service"+"_"+data['compute'];
            window[nova_mode]("nova-compute-columns-block","nova-compute-columns-block-content");
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


