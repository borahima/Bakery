$(document).ready(function(){
    $(".toggle-btn").click(function(){
        var moreText = $(".more-text");
        if (moreText.is(":visible")) {
            moreText.slideUp();
            $(this).text("Show More");
        } else {
            moreText.slideDown();
            $(this).text("Show Less");
        }
    });
});
