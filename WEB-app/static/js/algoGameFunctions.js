
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
        });
    });
});