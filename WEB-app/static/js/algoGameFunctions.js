
$(function(){
    $("#game").click(function(){
        $.ajax({
            url: '/runGame',
            type: 'POST',
            success: function(){
			}
        });
    });
});

$(function(){
    $("#algo").click(function(){
		$('#msgAlgo').html('<span style="color:blue">Please wait until the algorithm completes</span>');
        $.ajax({
            url: '/runAlgorithm',
            type: 'POST',
            success: function (response) { // display success response
				$('#msgAlgo').html('');
				$.each(response, function (key, data) {							
					if(key !== 'message') {
						$('#msgAlgo').append(key + ' -> ' + data + '<br/>');
					} else {
						$('#msgAlgo').append(data + '<br/>');
					}
				})
			},
			error: function (response) {
				$('#msgAlgo').html(response.message); // display error response
			}
        });
    });
});

function emptyMsg() {
	$('#msg').html('<span></span>')
	$('#msgAlgo').html('<span></span>')
}