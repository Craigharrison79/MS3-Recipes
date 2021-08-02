$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown({ hover: false });
    $('.tabs').tabs();
    $('.datepicker').datepicker();
    $('.parallax').parallax();
    $('.collapsible').collapsible();
    $('.carousel.carousel-slider').carousel({
      fullWidth: true,
      indicators: true
    });
  });