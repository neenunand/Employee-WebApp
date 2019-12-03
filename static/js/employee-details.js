(function (window) {
  EMP = {}
  EMP.id = ko.observable('');
  EMP.firstname = ko.observable('');
  EMP.lastname = ko.observable('');
  EMP.emp_id = ko.observable('');
    
  EMP.getEmployeeDetails = function(){
    var csrftoken = EMP.getCookie('csrftoken');
    $.ajax({
      method: 'GET',
      url: '/employee/api/details/'+EMP.id(),
      beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    .done( function (d, textStatus, jqXHR) {
      EMP.firstname(d.firstname);
      EMP.lastname(d.lastname);
      EMP.emp_id(d.emp_id);
    })
    .fail( function (jqXHR, textStatus, errorThrown) {
      alert(jqXHR.responseText);
    })
  }

  EMP.updateEmployee = function(){
    var csrftoken = EMP.getCookie('csrftoken');
    var formdata = new FormData();
    formdata.append('firstname', EMP.firstname());
    formdata.append('lastname', EMP.lastname());
    $.ajax({
      method: 'POST',
      url: '/employee/api/edit/'+EMP.id(),
      data: formdata,
      contentType: false,
      processData: false,
      beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    .done( function (d, textStatus, jqXHR) {
      location.reload()
    })
    .fail( function (jqXHR, textStatus, errorThrown) {
      alert(jqXHR.responseText);
    })
  }

  EMP.deleteEmployee = function(data, e){
    var csrftoken = EMP.getCookie('csrftoken');
    $.ajax({
      method: 'POST',
      url: '/employee/api/delete/'+EMP.id(),
      beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    .done( function (d, textStatus, jqXHR) {
      window.location = '/employee'
    })
    .fail( function (jqXHR, textStatus, errorThrown) {
      alert(jqXHR.responseText);
    })
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
      var docUrlArr = document.URL.split('/');
      var id = docUrlArr[docUrlArr.length - 1];
      EMP.id(id);
      EMP.getEmployeeDetails();
      ko.applyBindings(EMP);
    }
  }

document.onreadystatechange = init;