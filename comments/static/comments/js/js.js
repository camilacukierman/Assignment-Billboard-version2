/**
 * Created by itc_user on 8/18/2016.
 */


$(document).ready(function(){
    $("#show").click(function(){
        $(".display_form").toggle();
    });

    $("#cancel").click(function(){
        $(".display_form input").each(function(){
            $(this).val("");
        });
        $(".display_form").hide();
    })
});



