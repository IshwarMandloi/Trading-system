$('#search').keyup(function() {
  $.ajax({
    type: "POST",
    url: "/tradeapp/search/",
    data: {
      'search_text' : $('#search').val(),
      'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
    },
    success: searchSuccess,
    dataType: 'html'
     });
    });
  function searchSuccess(data, textStatus, jqXHR)
  {
      $('#search-results').html(data)
  }

  jQuery(document).ready(function($) {
  $(document).ready(function() {
    $('.lab-slide-up').find('a').attr('data-toggle', 'modal');
    $('.lab-slide-up').find('a').attr('data-target', '#lab-slide-bottom-popup');
  });
});

  $(document).ready(function(){
  $("#button").click(function(){
    var x = $("#switch").val();
    if (x=='buy') {
      $("#switch").prop('value','sell')
    }
    else
    {
      $("#switch").prop('value','buy')
    } 
  });
});


  function myFunction1(x,y){
    document.getElementById("company").value=x
    document.getElementById("price").value=y;
       
  }
function myFunction2() {
  document.getElementById("triggerprice").readOnly = true;
  document.getElementById("disclose").style.visibility = "hidden";
  
  var x = document.getElementById("boPopup");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

  function myFunction() {
     
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

$(document).ready(function(){
  $("#market").click(function(){
  $('input[id="price"]').attr('readonly',true).css("background","grey");
  $('input[id="triggerprice"]').attr('readonly',true).css("background","grey");
  });
  $("#limit").click(function(){
  $('input[id="triggerprice"]').attr('readonly',true).css("background","grey");
  });
  $("#slm").click(function(){
  $('input[id="price"]').attr('readonly',true).css("background","grey");
  });
  $("#regular").click(function(){
  $('input[id="price"]').attr('readonly',true).css("background","grey");
  $('input[id="triggerprice"]').attr('readonly',true).css("background","grey");
  });

  $("#co").click(function(){
    $('#day').hide();
    $('#ioc').hide();
    $('#sl').hide();
    $('#slm').hide();
    $('#nrml').attr('disable',true);
    document.getElementById("triggerprice").readOnly = true;
  });
 
  $("#amo").click(function(){
  $('input[id="triggerprice"]').attr('readonly',true).css("background","grey");
  });
});

$

