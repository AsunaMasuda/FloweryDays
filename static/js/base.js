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

// Quantity Counter
$(document).ready(function(){
    $(document).on('click', '.plus', function(){
        let id = this.id.split("_")[1]
        let color = this.id.split("_")[2]
        let plus_id = `#number_${id}_${color}`
        $(plus_id).val(parseInt($(plus_id).val()) + 1 );
            if ($(plus_id).val() == 100) {
                $(plus_id).val(99);
            }
    });
    $(document).on('click', '.minus', function(){
        let id = this.id.split("_")[1]
        let color = this.id.split("_")[2]
        let minus_id = `#number_${id}_${color}`
        $(minus_id).val(parseInt($(minus_id).val()) - 1 );
            if ($(minus_id).val() == 0) {
                $(minus_id).val(1);
            }
    });
    $(document).on('change', 'input', function() {
        let id = this.id.split("_")[1]
        let color = this.id.split("_")[2]
        let quantityId = `#number_${id}_${color}`
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