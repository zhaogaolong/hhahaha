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


function neutron_status(url){
    var url =url;
    $.get(url,function(callback, status){
        //console.log(callback,status);
        if (status == 'success') {
            var data = JSON.parse(callback);
            n_name = "neutron"+"_"+data['status'];
            //console.log(f_name);
            window[n_name]("neutron-status-block","neutron-status-content");

            // 着是neutron栏中的大的block
            window[n_name]("neutron-columns-block-status","neutron-columns-block-content");


            // l3
            neutron_status_list = "neutron"+"_"+"service"+"_"+data['l3'];
            window[neutron_status_list]("neutron-l3-columns-block","neutron-l3-columns-block-content");

            // dhcp
            neutron_status_list = "neutron"+"_"+"service"+"_"+data['dhcp'];
            window[neutron_status_list]("neutron-dhcp-columns-block","neutron-dhcp-columns-block-content");

            // api
            neutron_status_list = "neutron"+"_"+"service"+"_"+data['api'];
            window[neutron_status_list]("neutron-api-columns-block","neutron-api-columns-block-content");

            //// agetnt
            //neutron_status_list = "neutron"+"_"+"service"+"_"+data['agent'];
            //window[neutron_status_list]("neutron-river-columns-block","neutron-river-columns-block-content");

            // compute
            neutron_status_list = "neutron"+"_"+"service"+"_"+data['compute'];
            window[neutron_status_list]("neutron-compute-columns-block","neutron-compute-columns-block-content");
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
