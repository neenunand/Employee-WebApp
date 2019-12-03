(function (window) {
  EMP = {}
  EMP.employees_list = ko.observableArray([]);
  EMP.taskname = ko.observable('');
  EMP.assignee = ko.observable('');
  EMP.status = ko.observable('');
  EMP.start_date = ko.observable('');
  EMP.end_date = ko.observable('');

  EMP.getEmployeesList = function(){
    var csrftoken = EMP.getCookie('csrftoken');
    $.ajax({
      method: 'GET',
      url: '/employee/api/list',
      beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    .done( function (d, textStatus, jqXHR) {
      EMP.employees_list([]);
      for(var i=0; i<d.length; i++){
        EMP.employees_list.push(d[i]);
      }
    })
    .fail( function (jqXHR, textStatus, errorThrown) {
      alert(jqXHR.responseText);
    })
  }
  
  EMP.createTask = function(){
    EMP.start_date($('#sd').val())
    EMP.end_date($('#ed').val())
    
    var csrftoken = EMP.getCookie('csrftoken');
    var formdata = new FormData();
    formdata.append('taskname', EMP.taskname());
    formdata.append('assignee', EMP.assignee());
    formdata.append('status', EMP.status());
    formdata.append('start_date', EMP.start_date());
    formdata.append('end_date', EMP.end_date());
    $.ajax({
      method: 'POST',
      url: '/employee/api/task/create',
      data: formdata,
      contentType: false,
      processData: false,
      beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    .done( function (d, textStatus, jqXHR) {
      window.location='/employee/tasks';
    })
    .fail( function (jqXHR, textStatus, errorThrown) {
      alert(jqXHR.responseText);
    })
  };

  EMP.getCookie = function(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };
            
})(this);

  function init() {
    if (document.readyState == "interactive") {
      EMP.getEmployeesList();
      ko.applyBindings(EMP);
    }
  }

document.onreadystatechange = init;