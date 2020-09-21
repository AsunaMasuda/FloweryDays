// Navbar
$(document).ready(function () {
  var navberExtension = $("#navber-extension");
  $(window).scroll(function () {
    if (
      $(this).scrollTop() > 100 &&
      navberExtension.hasClass("navber-extension")
    ) {
      navberExtension
        .removeClass("navber-extension")
        .addClass("fixed-top");
    } else if (
      $(this).scrollTop() <= 100 &&
      navberExtension.hasClass("fixed-top")
    ) {
      navberExtension
        .removeClass("fixed-top")
        .addClass("navber-extension");
    }
  });
});

// Wow.js
$(document).ready(function () {
    new WOW().init();
});

$(window).scroll(function () {
  if ($(window).scrollTop() <= 100) {
    $("#logo").css("display", "block");
  } else {
    $("#logo").css("display", "none");
  }
});

$(window).scroll(function () {
  if ($(window).scrollTop() > 100) {
    $("#logo-small").css("display", "block");
  } else {
    $("#logo-small").css("display", "none");
  }
});

// Quantity Counter
$(document).ready(function(){
    $(document).on('click', '.plus', function(){
        let id = this.id.split("_")[1]
        let plus_id = `#number_${id}`
        $(plus_id).val(parseInt($(plus_id).val()) + 1 );
            if ($(plus_id).val() == 100) {
                $(plus_id).val(99);
            }
    });
    $(document).on('click', '.minus', function(){
        let id = this.id.split("_")[1]
        let minus_id = `#number_${id}`
        $(minus_id).val(parseInt($(minus_id).val()) - 1 );
            if ($(minus_id).val() == 0) {
                $(minus_id).val(1);
            }
    });
    $(document).on('change', 'input', function() {
        let id = this.id.split("_")[1]
        let quantityId = `#number_${id}`
        $(quantityId).val(parseInt($(quantityId).val()));
            if (($(quantityId).val() > 99)) {
                $('#errorMsg').show();
                $(quantityId).val(99);
            }
            else if (($(quantityId).val() < 1 )) {
                $('#errorMsg').show();
                $(quantityId).val(1);
            }
            else{
                $('#errorMsg').hide();
            }
    });
});

// Back to previous page
$(document).ready(function() {
    $(document).on('click', '.backToPrevious', function(){
        window.history.back();
    })
});