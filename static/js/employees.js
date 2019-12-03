(function (window) {
  EMP = {}
  EMP.employees_list = ko.observableArray([]);
    
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

  EMP.createEmployee = function(){
    window.open('/employee/create');
  }

  EMP.getDetails = function(data, e){
    window.open('/employee/details/'+data.id);
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
      EMP.getEmployeesList();
      ko.applyBindings(EMP);
    }
  }

document.onreadystatechange = init;