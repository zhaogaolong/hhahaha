/**
 * Created by Administrator on 2016/1/7.
 */

/**
 * 获取cloudstatus的信息
 */
function cloud_status(get_url){
    $.get(get_url, function(callback,status){
        //console.log(callback,status);
        if (status == 'success') {
            var data = JSON.parse(callback);
            //console.log(status);
            f_name = "cloud"+"_"+data['status'];

            //着个类似 python getattr
            window[f_name]("cloud-status-block","cloud-status-content");
            delete data;
            delete callback;

        }
    });
}


function cloud_up(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('navy-bg widget block-status text-center');
    $("#"+content).text('Ok');
}

function cloud_warning(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('yellow-bg widget block-status text-center');
    $("#"+content).text('Warning');
}
function cloud_critical(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('pink-bg widget block-status text-center');
    $("#"+content).text('Critical');
}

function cloud_down(block_id,content){
    $("#"+block_id).removeClass();
    $("#"+block_id).addClass('red-bg widget block-status text-center');
    $("#"+content).text('Error');
}


