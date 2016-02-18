function check_select(checkAll, checkboxes){
  checkAll.on('ifChecked ifUnchecked', function(event) {
    if (event.type == 'ifChecked') {
      checkboxes.iCheck('check');
    } else {
      checkboxes.iCheck('uncheck');
    }
  });
  checkboxes.on('ifChanged', function(event){
    if(checkboxes.filter(':checked').length == checkboxes.length) {
      checkAll.prop('checked', 'checked');
    } else {
      checkAll.removeProp('checked');
    }
    checkAll.iCheck('update');
  });
}

function select_check_action(checkboxes){
  var str="";
  var ids="";
  checkboxes.each(function(index, element){
    if(true == $(element).is(':checked')){
      str+=$(element).parent().parent().siblings(".mail-ontact").text()+",";
    }
  });
  if(str.substr(str.length-1)== ','){
    ids = str.substr(0,str.length-1);
  }
  console.log(str);
  console.log(ids);
}


//
//$("#manager_click").parent().siblings(".btn-primary").click(function(){
//  // var url = $(this).attr('data-url');
//  var str="";
//  var ids="";
//  $("#manager_table td.check-mail input").each(function(){
//    if(true == $(this).is(':checked')){
//      str+=$(this).parent().parent().siblings(".mail-ontact").text+",";
//    }
//  });
//  if(str.substr(str.length-1)== ','){
//    ids = str.substr(0,str.length-1);
//  }
//  console.log(str);
//  console.log(ids);
//});

