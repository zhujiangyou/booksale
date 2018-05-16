$(function(){
    $(".one li").hover(function(){
        $(this).find(".two").show();
    },function(){
        $(this).find(".two").hide();
    });
    $(".tab li").click(function(){
        $(this).addClass("on").siblings().removeClass("on");
    });
    $(".fixnav a").click(function(){
        var index = $(this).attr("title");
        var id = "#item"+index;
        $("html,body").animate({scrollTop: $(id).offset().top}, 500);
    })
})