(function (window) {
  EMP = {}
  EMP.firstname = ko.observable('');
  EMP.lastname = ko.observable('');
  EMP.emp_id = ko.observable('');
  
  EMP.createEmployee = function(){
    var csrftoken = EMP.getCookie('csrftoken');
    var formdata = new FormData();
    formdata.append('firstname', EMP.firstname());
    formdata.append('lastname', EMP.lastname());
    formdata.append('emp_id', EMP.emp_id());
    $.ajax({
      method: 'POST',
      url: '/employee/api/create',
      data: formdata,
      contentType: false,
      processData: false,
      beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    .done( function (d, textStatus, jqXHR) {
      window.location='/employee';
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
      ko.applyBindings(EMP);
    }
  }

document.onreadystatechange = init;