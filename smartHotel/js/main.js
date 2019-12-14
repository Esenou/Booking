(function($) {

//$(window).on('load', function() { // makes sure the whole site is loaded
    $('#status').fadeOut(); // will first fade out the loading animation
    $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
    $('body').delay(350).css({'overflow':'visible'});
//});

/**
Header
*/
var viewportWidth = $(window).width();
  $(window).scroll(function() {
      if ($(this).scrollTop() >= 100) { // this refers to window
        if( viewportWidth > 767 ){
          $('.hrdgap').addClass('hrdgapsmall');
          $('header').addClass('hrdsmall');
        }else{
          $('header').addClass('hrdresponsive');
        }
      }else{
          $('.hrdgap').removeClass('hrdgapsmall');
          $('header').removeClass('hrdsmall');
          $('header').removeClass('hrdresponsive');        
      }
  });

$('.navbar-toggle').on('click', function(){
	$('#mobile-nav').slideToggle(300);
});
	

$('.navtoggle').on('click', function(){
  $(this).toggleClass('menu-expend');
  $('.sm-main-nav').fadeToggle(500);
});

$('.mnh-close').on('click', function(){
  $(this).removeClass('menu-expend');
  $('.sm-main-nav').fadeOut(500);
});



/**
Responsive on 767px
*/
var windowWidth = $(window).width();
// if (windowWidth <= 767) {

  $('.toggle-btn').on('click', function(){
    $(this).toggleClass('menu-expend');
    $('.toggle-bar ul').slideToggle(500);
  });


// }

/**
Main Slider
*/
if( $('.home-slider-outer').length ){
  $('.home-slider-outer').slick({
    autoplay: true,
    autoplaySpeed: 5000,
    fade: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false
  });
}
/**
Home promo slider
*/
if( $('.hpromoslider').length ){
  $('.hpromoslider').slick({
    autoplay: true,
    autoplaySpeed: 5000,
    fade: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    dots: true
  });
}
/**
Client slider
*/
if( $('.hcslider-in').length ){
  $('.hcslider-in').slick({
    autoplay: true,
    autoplaySpeed: 5000,
    slidesToShow: 5,
    slidesToScroll: 1,
    arrows: true,
    prevArrow: '<button type="button" class="slick-prev"><i class="fa fa-angle-left" aria-hidden="true"></i></button>',
    nextArrow: '<button type="button" class="slick-next"><i class="fa fa-angle-right" aria-hidden="true"></i></button>',
      responsive: [
        { breakpoint: 991, settings: { slidesToShow: 3 } },
        { breakpoint: 600, settings: { slidesToShow: 2 } },
        { breakpoint: 380, settings: { slidesToShow: 1 } }
      ]
  });
}

/**
Cozy Rooms slider
*/
var crlh = $('.cozy-rooms .cr-left').outerHeight();

if( $('.cr-right-slider').length ){
  $('.cr-right-slider').slick({
    autoplay: true,
    autoplaySpeed: 5000,
    speed: 1000,
    fade: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    asNavFor: '.cr-left-scroller ul',
  });
}

if( $('.cr-left-scroller ul').length ){
  $('.cr-left-scroller ul').slick({
    autoplay: true,
    autoplaySpeed: 5000,
    speed: 1000,
    slidesToShow: 3,
    arrows: false,
    draggable: false,
    infinite: true,
    pauseOnHover: false,
    swipe: false,
    touchMove: false,
    vertical: true,
    focusOnSelect: true,
    asNavFor: '.cr-right-slider',
    prevArrow: '<button type="button" class="slick-prev"><i class="fa fa-angle-left" aria-hidden="true"></i></button>',
    nextArrow: '<button type="button" class="slick-next"><i class="fa fa-angle-right" aria-hidden="true"></i></button>',
      responsive: [
        { breakpoint: 991, settings: { slidesToShow: 1, autoplay: false, vertical: false, arrows: true} },
        { breakpoint: 600, settings: { slidesToShow: 1, autoplay: false, vertical: false, arrows: true } },
        { breakpoint: 380, settings: { slidesToShow: 1, autoplay: false, vertical: false, arrows: true } }
      ]
  });
}

/**
offerslider
*/
if( $('.offerslider ul').length ){
  $('.offerslider ul').slick({
    autoplay: true,
    autoplaySpeed: 5000,
    speed: 1000,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    /*centerMode: true,*/
    /*variableWidth: true,*/
    prevArrow: '<button type="button" class="slick-prev"><i class="fa fa-angle-left" aria-hidden="true"></i></button>',
    nextArrow: '<button type="button" class="slick-next"><i class="fa fa-angle-right" aria-hidden="true"></i></button>',
  });
}


/**
offerslider
*/
if( $('.myoffersld').length ){
  $('.myoffersld').slick({
    autoplay: false,
    arrows: true,
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    prevArrow: '<button type="button" class="slick-prev"><i class="fa fa-angle-left" aria-hidden="true"></i></button>',
    nextArrow: '<button type="button" class="slick-next"><i class="fa fa-angle-right" aria-hidden="true"></i></button>',
    responsive: [
        { breakpoint: 1199, settings: { slidesToShow: 2 } }
      ]
  });
}




/**
tripadvisorreview
*/
if( $('.taslider').length ){
  $('.taslider').slick({
    autoplay: true,
    autoplaySpeed: 5000,
    speed: 1000,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    dots: false,
    prevArrow: $('.myprev'),
    nextArrow: $('.mynext'),
      responsive: [
        { breakpoint: 768, settings: { autoplay: false, arrows: true,dots: true } }
      ]
  });
}


if( $('.adsislider').length ){
  $('.adsislider').slick({
    autoplay: false,
    autoplaySpeed: 5000,
    slidesToShow: 7,
    slidesToScroll: 1,
    arrows: false,
    prevArrow: '<button type="button" class="slick-prev"><i class="fa fa-angle-left" aria-hidden="true"></i></button>',
    nextArrow: '<button type="button" class="slick-next"><i class="fa fa-angle-right" aria-hidden="true"></i></button>',
      responsive: [
        { breakpoint: 991, settings: { slidesToShow: 3, arrows: true } },
        { breakpoint: 600, settings: { slidesToShow: 2, arrows: true } },
        { breakpoint: 380, settings: { slidesToShow: 1, arrows: true } }
      ]
  });
}


/**
videoplay
*/
// Inject YouTube API script

$('.videoplay').on('click', function(ev) {
  $('.fullwvideo').addClass('playing');
  $("#hvideo")[0].src += "&autoplay=1";
  ev.preventDefault();

});

/**
Datepicker
*/
var dateToday = new Date();
var currentMonth = dateToday.getMonth();
var currentDate = dateToday.getDate();
var currentYear = dateToday.getFullYear();

$( "#quickbook .checkindate" ).datepicker({
  //dayNames: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
  monthNames: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
  showOtherMonths: true,
  numberOfMonths: 1,
  minDate: dateToday,
  maxDate: new Date(currentYear, currentMonth+3),
    //dateFormat: "dd", 
    onSelect: function(dateText){
    
    var selectedDate = $('.checkindate').datepicker('getDate');
    //var dayNames = $('.checkindate').datepicker('option', 'dayNames');
    var monthNames = $('.checkindate').datepicker('option', 'monthNames');
    var date = selectedDate.getDate();
    //var day = selectedDate.getDay();
    var fdate = $.datepicker.formatDate("dd-m-yy", selectedDate);
    var month = monthNames[selectedDate.getMonth()];
    var year = selectedDate.getFullYear();

    //var selected = $(this).val();
    var output = '<span class="date">'+date+'</span> <span class="dsep">/</span> <span class="month"> '+month+'</span>';
    $('.checkinhandle').html(output);
    $('#quickbook #checkindate').val(fdate);

    $('.checkindate').slideUp();
    console.log(fdate);
  },
  onClose: function (dateText) {
    $('.checkindate').slideUp();
  }
});

$( "#quickbook .checkoutdate" ).datepicker({
  //dayNames: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
  monthNames: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
  showOtherMonths: true,
  numberOfMonths: 1,
  minDate: dateToday,
  maxDate: new Date(currentYear, currentMonth+3),
    //dateFormat: "dd", 
    onSelect: function(dateText){
    var selectedDate = $('.checkoutdate').datepicker('getDate');

    var monthNames = $('.checkoutdate').datepicker('option', 'monthNames');
    var date = selectedDate.getDate();

    var fdate = $.datepicker.formatDate("dd-mm-yy", selectedDate);
    var month = monthNames[selectedDate.getMonth()];
    var year = selectedDate.getFullYear();

    //var selected = $(this).val();
    var output = '<span class="date">'+date+'</span> <span class="dsep">/</span> <span class="month"> '+month+'</span>';
    $('.checkouthandle').html(output);
    $('#quickbook #checkoutdate').val(fdate);

    $('.checkoutdate').slideUp();
    console.log(fdate);
  },
  onClose: function (dateText) {
    $('.checkoutdate').slideUp();
  }
});





$('#quickbook .checkinhandle').on('click', function(){
  $('.checkoutdate').slideUp();
  $('.checkindate').slideToggle();
});
$('#quickbook .checkouthandle').on('click', function(){
  $('.checkindate').slideUp();
  $('.checkoutdate').slideToggle();
});

$('#quickbook .rcapacity').on('click', function(){
  $('.capacityselect').slideToggle();
  
});

$('.capacityselect ul li').on('click', function(){
  var adultdate = $(this).data('adult');
  var childdate = $(this).data('child');

  $('.rcapacity .adult').text(adultdate);
  $('.rcapacity .child').text(childdate);
  $('.third-col #capacityadult').val(adultdate);
  $('.third-col #capacitychild').val(childdate);
});









/**
Slick slider
*/
if( $('responsive-slider').length ){
    $('.responsive-slider').slick({
      dots: true,
      infinite: false,
      speed: 300,
      slidesToShow: 4,
      slidesToScroll: 4,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
        // You can unslick at a given breakpoint now by adding:
        // settings: "unslick"
        // instead of a settings object
      ]
    });
}

/**
Meet Event Slider
**/
if( $('.meetev-slider').length ){
 $('.meetev-slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    dots: false,
    arrows: false,
    centerMode: false,
    focusOnSelect: true,
    asNavFor: '.meetev-slider-padding'
  });
}

if( $('.meetev-slider-padding').length ){
 $('.meetev-slider-padding').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    dots: false,
    arrows: false,
    centerMode: false,
    focusOnSelect: true,
    asNavFor: '.meetev-slider',
     responsive: [
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 4,
          slidesToScroll: 4
        }
      }
    ]

  });
}

/*slick slider adv-custom-pager6*/
if( $('.adv-custom-pager6').length ){
 $('.adv-custom-pager6').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    dots: false,
    arrows: false,
    centerMode: false,
    focusOnSelect: true,
    asNavFor: '.for-adv-custom-pager6',
     responsive: [
      {
        breakpoint: 767,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1
        }
      }
    ]

  });
}

if( $('.for-adv-custom-pager6').length ){
 $('.for-adv-custom-pager6').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: true,
  fade: true,
  asNavFor: '.adv-custom-pager6',
  controls:true
});
}

/*slick slider adv-custom-pager5*/
if( $('.adv-custom-pager5').length ){
 $('.adv-custom-pager5').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    dots: false,
    centerMode: false,
    arrows: false,
    focusOnSelect: true,
    asNavFor: '.for-adv-custom-pager5',
    responsive: [
      {
        breakpoint: 767,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1
        }
      }
    ]
  });
}

if( $('.for-adv-custom-pager5').length ){
 $('.for-adv-custom-pager5').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: true,
  fade: true,
  asNavFor: '.adv-custom-pager5'
});
}


 /*slick slider adv-custom-pager4*/
if( $('.adv-custom-pager4').length ){
 $('.adv-custom-pager4').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    dots: false,
    centerMode: false,
    focusOnSelect: true,
    arrows: false,
    asNavFor: '.for-adv-custom-pager4',
    responsive: [
      {
        breakpoint: 767,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1
        }
      }
    ]
  });
}

if( $('.for-adv-custom-pager4').length ){
   $('.for-adv-custom-pager4').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    fade: true,
    asNavFor: '.adv-custom-pager4'
  });
}


 /*slick slider adv-custom-pager3*/
if( $('.adv-custom-pager3').length ){
 $('.adv-custom-pager3').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    dots: false,
    arrows: false,
    centerMode: false,
    focusOnSelect: true,
    asNavFor: '.for-adv-custom-pager3',
    responsive: [
      {
        breakpoint: 767,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1
        }
      }
    ]
  });
}

if( $('.for-adv-custom-pager3').length ){
 $('.for-adv-custom-pager3').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: true,
  fade: true,
  asNavFor: '.adv-custom-pager3'
});
}

/*light gallery*/

if( $('.lightgallery1').length ){
  $(".lightgallery1").lightGallery({
    zoom: false,
    share: false,
    download: false
  }); 
}
if( $('.lightgallery2').length ){
  $(".lightgallery2").lightGallery({
    zoom: false,
    share: false,
    download: false
  });
}
if( $('.lightgallery3').length ){
  $(".lightgallery3").lightGallery({
    zoom: false,
    share: false,
    download: false
  }); 
}

/*fencybox*/
if( $('[data-fancybox="gallery3"]').length ){
  $('[data-fancybox="gallery3"]').fancybox();
}

if( $('[data-fancybox="gallery4"]').length ){
  $('[data-fancybox="gallery4"]').fancybox();
}

if( $('[data-fancybox="gallery5"]').length ){
  $('[data-fancybox="gallery5"]').fancybox();
}

if( $('[data-fancybox="gallery6"]').length ){
  $('[data-fancybox="gallery6"]').fancybox();
}



/**
Google Map
*/

if( $('#ftrMapID').length ){
  var latitude = $('#ftrMapID').data('latitude');
  var longitude = $('#ftrMapID').data('longitude');
  var marker = $('#ftrMapID').data('marker');

  var myCenter= new google.maps.LatLng(latitude,  longitude);

  function initialize(){
      var mapProp = {
        center:myCenter,

        mapTypeControl:true,
        scrollwheel: false,

        zoomControl: true,
        disableDefaultUI: true,
        zoom:16,
        streetViewControl: false,
        rotateControl: true,
        mapTypeId:google.maps.MapTypeId.ROADMAP,
        styles : [{"featureType":"administrative","elementType":"labels.text.fill","stylers":[{"color":"#0c0b0b"}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f6f6f6"}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"all","stylers":[{"saturation":-100},{"lightness":45}]},{"featureType":"road","elementType":"labels.text.fill","stylers":[{"color":"#090909"}]},{"featureType":"road.highway","elementType":"all","stylers":[{"visibility":"simplified"}]},{"featureType":"road.arterial","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"all","stylers":[{"color":"#d4e4eb"},{"visibility":"off"}]},{"featureType":"water","elementType":"geometry.fill","stylers":[{"visibility":"off"},{"color":"#fef7f7"}]},{"featureType":"water","elementType":"labels.text.fill","stylers":[{"color":"#9b7f7f"}]},{"featureType":"water","elementType":"labels.text.stroke","stylers":[{"color":"#fef7f7"}]}],
        };

      var map= new google.maps.Map(document.getElementById('ftrMapID'),mapProp);

      var marker= new google.maps.Marker({
        position:myCenter,
          icon: '/images/marker.png'
        });
      marker.setMap(map);
      //styles: [{"featureType":"administrative","elementType":"labels.text.fill","stylers":[{"color":"#0c0b0b"}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f2f2f2"}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"all","stylers":[{"saturation":-100},{"lightness":45}]},{"featureType":"road","elementType":"labels.text.fill","stylers":[{"color":"#090909"}]},{"featureType":"road.highway","elementType":"all","stylers":[{"visibility":"simplified"}]},{"featureType":"road.arterial","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"all","stylers":[{"color":"#d4e4eb"},{"visibility":"on"}]},{"featureType":"water","elementType":"geometry.fill","stylers":[{"visibility":"on"},{"color":"#fef7f7"}]},{"featureType":"water","elementType":"labels.text.fill","stylers":[{"color":"#9b7f7f"}]},{"featureType":"water","elementType":"labels.text.stroke","stylers":[{"color":"#fef7f7"}]}]
      
  }

  google.maps.event.addDomListener(window, 'load', initialize);

}



if (windowWidth <= 767 && $('#ftrMapIDXs').length ) {

var latitude = $('#ftrMapIDXs').data('latitude');
var longitude = $('#ftrMapIDXs').data('longitude');
var marker = $('#ftrMapIDXs').data('marker');

var myCenter= new google.maps.LatLng(latitude,  longitude);

function initialize(){
    var mapProp = {
      center:myCenter,

      mapTypeControl:true,
      scrollwheel: false,

      zoomControl: true,
      disableDefaultUI: true,
      zoom:7,
      streetViewControl: false,
      rotateControl: true,
      mapTypeId:google.maps.MapTypeId.ROADMAP,
      styles : [{"featureType":"administrative","elementType":"labels.text.fill","stylers":[{"color":"#0c0b0b"}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f6f6f6"}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"all","stylers":[{"saturation":-100},{"lightness":45}]},{"featureType":"road","elementType":"labels.text.fill","stylers":[{"color":"#090909"}]},{"featureType":"road.highway","elementType":"all","stylers":[{"visibility":"simplified"}]},{"featureType":"road.arterial","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"all","stylers":[{"color":"#d4e4eb"},{"visibility":"off"}]},{"featureType":"water","elementType":"geometry.fill","stylers":[{"visibility":"off"},{"color":"#fef7f7"}]},{"featureType":"water","elementType":"labels.text.fill","stylers":[{"color":"#9b7f7f"}]},{"featureType":"water","elementType":"labels.text.stroke","stylers":[{"color":"#fef7f7"}]}],
      };

    var map= new google.maps.Map(document.getElementById('ftrMapIDXs'),mapProp);

    var marker= new google.maps.Marker({
      position:myCenter,
        icon: '/images/marker.png'
      });
    marker.setMap(map);
    //styles: [{"featureType":"administrative","elementType":"labels.text.fill","stylers":[{"color":"#0c0b0b"}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f2f2f2"}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"all","stylers":[{"saturation":-100},{"lightness":45}]},{"featureType":"road","elementType":"labels.text.fill","stylers":[{"color":"#090909"}]},{"featureType":"road.highway","elementType":"all","stylers":[{"visibility":"simplified"}]},{"featureType":"road.arterial","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"all","stylers":[{"color":"#d4e4eb"},{"visibility":"on"}]},{"featureType":"water","elementType":"geometry.fill","stylers":[{"visibility":"on"},{"color":"#fef7f7"}]},{"featureType":"water","elementType":"labels.text.fill","stylers":[{"color":"#9b7f7f"}]},{"featureType":"water","elementType":"labels.text.stroke","stylers":[{"color":"#fef7f7"}]}]
    
}

google.maps.event.addDomListener(window, 'load', initialize);


}
var wow = new WOW(
  {
    mobile:       false       // trigger animations on mobile devices (true is default)
  }
);
wow.init();

/**
File upload button
*/
$('#browse_btn').click(function(){ $('#openfile').trigger('click'); });



/**
Vacancies Modal Show
*/
$('.vacancies_modal_btn').on('click', function (e) {
  e.preventDefault();
  var parent = $(this).parents('.jobs-item');
  var title = parent.find('h4').text();
  var content = parent.find('.modal-des').html();

  $('#vacancies_modal h4.modal-bx-title').text(title);
  $('#vacancies_modal .modal-des-open').html(content);

  $('#vacancies_modal').modal('show');
    //console.log(content);
});


/**
Vacancies Modal Show
*/
$('.standard-amenities .feature-items .feature-itm').on('click', function (e) {
  e.preventDefault();
  if( $(this).next('.popupitems:hidden').length ){
    var popupitems = $(this).next('.popupitems').html();
    var title = $(this).find('p').text();

    $('#standard_amenities_modal h4.modal-bx-title').text(title);
    $('#standard_amenities_modal .modal-des-open').html(popupitems);

    $('#standard_amenities_modal').modal('show');
      //console.log(content);
  }
});



})(jQuery);