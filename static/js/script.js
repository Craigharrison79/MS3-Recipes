$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown({ hover: false });
    $('.tabs').tabs();
    $('.datepicker').datepicker({
      format: 'd mmm, yyyy',
      yearRange: 2,
      showClearBtn: true,
      i18n: {
        done: "select"
      }
    });
    $('.parallax').parallax();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.carousel.carousel-slider').carousel({
      fullWidth: true,
      indicators: true
    });
  });