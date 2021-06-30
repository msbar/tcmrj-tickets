$(document).ready(function () {
    //colapse menu lateral
    $("#btn-menu").click(function () { 
        $("#sidebar").toggleClass('closed');        
    });
    $(".menu-item").click(function () { 
        $(this).toggleClass("opened");
        $("#sidebar").removeClass('closed'); 
    });

    $('.toast').toast('show');
});