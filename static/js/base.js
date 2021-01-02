// Search bar for less than medium screens
$(document).ready(function () {
  $('#search-bar-small').hide();
  $('#search-button').click(function () {
    $('#search-bar-small').slideToggle('slow');
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

// Quantity Counter - Cart View
$(document).ready(function(){
    $(document).on('click vclick', '.plus', function(){
        $(this).siblings('.qty_input').val(parseInt($(this).siblings('.qty_input').val()) + 1);
            if ($(this).siblings('.qty_input').val() == 100) {
                $(this).siblings('.qty_input').val(99);
            }
    });
    $(document).on('click vclick', '.minus', function(){
        $(this).siblings('.qty_input').val(parseInt($(this).siblings('.qty_input').val()) - 1);
            if ($(this).siblings('.qty_input').val() == 0) {
                $(this).siblings('.qty_input').val(1);
            }
    });
    $(document).on('change', '.quantity-count', function() {
        $(this).val($(this).val());
            if (($(this).val() > 99)) {
                $('.errorMsg').show();
                $(this).val(99);
            }
            else if (($(this).val() < 1 )) {
                $('.errorMsg').show();
                $(this).val(1);
            }
            else{
                $('.errorMsg').hide();
            }
    });
});

// Back to previous page
$(document).ready(function() {
    $(document).on('click', '.backToPrevious', function(){
        window.history.back();
    })
});

// Customer Review
$(document).ready(function () {
    $('.review_click_arrow_1').click(function() {
        $(this).find('i').toggleClass('fa-chevron-up fa-chevron-down');
        if ($('.review_click_arrow_2').find('i').hasClass('fa-chevron-up')) {
        $('.review_click_arrow_2').find('i').toggleClass('fa-chevron-up fa-chevron-down')
        };
    });
    $('.review_click_arrow_2').click(function() {
        $(this).find('i').toggleClass('fa-chevron-up fa-chevron-down');
        if ($('.review_click_arrow_1').find('i').hasClass('fa-chevron-up')) {
        $('.review_click_arrow_1').find('i').toggleClass('fa-chevron-up fa-chevron-down')
        }
    })
});