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
        $('.quantity-count').val(parseInt($('.quantity-count').val()) + 1 );
            if ($('.quantity-count').val() == 100) {
                $('.quantity-count').val(99);
            }        
    });
    $(document).on('click', '.minus', function(){
        $('.quantity-count').val(parseInt($('.quantity-count').val()) - 1 );
            if ($('.quantity-count').val() == 0) {
                $('.quantity-count').val(1);
            }
        });
});


// Back to previous page
$(document).ready(function() {
    $(document).on('click', '.backToPrevious', function(){
        window.history.back();
    })
});