
$(function(){
    $("#game").click(function(){
        $.ajax({
            url: '/runGame',
            data: json,
            type: 'POST',
            success: function(response){
                document.getElementById('result').innerHTML = response
            },
            error: function(error){
                $("#result").text(error);
            }
        });
    });
});
