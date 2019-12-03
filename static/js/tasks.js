(function (window) {
  EMP = {}
  EMP.tasks_list = ko.observableArray([]);
    
  EMP.getTasksList = function(){
    var csrftoken = EMP.getCookie('csrftoken');
    $.ajax({
      method: 'GET',
      url: '/employee/api/tasks/list',
    })
    .done( function (d, textStatus, jqXHR) {
      EMP.tasks_list([]);
      for(var i=0; i<d.length; i++){
        EMP.tasks_list.push(d[i]);
      }
    })
    .fail( function (jqXHR, textStatus, errorThrown) {
      alert(jqXHR.responseText);
    })
  }

  EMP.createTask = function(){
    window.open('/employee/task/create');
  }

  EMP.getDetails = function(data, e){
    window.open('/employee/task/details/'+data.id);
  }

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
      EMP.getTasksList();
      ko.applyBindings(EMP);
    }
  }

document.onreadystatechange = init;