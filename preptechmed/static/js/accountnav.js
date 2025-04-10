$(document).ready(function() {

        $(".account-btn").click(function(){

            $("#account-panel").slideToggle();

        });

        $(window).click(function() {

            $("#account-panel").hide();

            $("#account-panel, .account-btn").click(function (event) {
                event.stopPropagation();
            });

        });

});
