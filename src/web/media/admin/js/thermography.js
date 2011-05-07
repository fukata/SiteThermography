(function($){
	var $frame = $("#thermography_frame");
	$frame.height($(window).height()-20);
	var $fw = $($frame[0].contentWindow);
	//var $fb = $($frame[0].contentWindow.document.body);
	$frame.ready(function(){
		console.log("thermography_frame ready.");
	});
	$frame.bind('load.thermography', function(){
		console.log("thermography_frame loaded.");
		var $fb = $($frame[0].contentWindow.document.body);
		var $baseDiv = $(document.createElement('div')).css({
			"position": "absolute",
			"top": "0px",
			"left": "0px"
		}).attr("id","thermography_canvas");
		$fb.prepend($baseDiv);
	
		var $canvas = $("#thermography_canvas", $fb);
		jQuery.each(points, function(position, point){
			var p = position.split(":");
			var x = p[0];
			var y = p[1];

			var per = ~~( ~~( (point / maxPoint) * 100 ) * 2.55 )
			var color = "#" + per.toString(16) + "0000";

			var $div = $(document.createElement('div'));
			$div.css({
				"background-color": color,
				"position": "absolute",
				"top": (y*20)+"px",
				"left": (x*20)+"px",
				"width": "20px",
				"height": "20px",
				"filter": "alpha(opacity=50)",
				"-moz-opacity":"0.50",
				"opacity":"0.50",
				"z-index": "10000"
			});
			$canvas.append($div);
		});
	});
})(jQuery);
