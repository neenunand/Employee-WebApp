(function (window) {
  EMP = {}
  EMP.username = ko.observable('');
  EMP.password = ko.observable('');
  
  EMP.userLogin = function(){
    var csrftoken = EMP.getCookie('csrftoken');
    var formdata = new FormData();
    formdata.append('username', EMP.username());
    formdata.append('password', EMP.password());
    $.ajax({
      method: 'POST',
      url: '/user/api/login',
      data: formdata,
      contentType: false,
      processData: false,
      beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    .done( function (d, textStatus, jqXHR) {
      window.location = '/employee';
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