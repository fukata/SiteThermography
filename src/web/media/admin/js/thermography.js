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
			var x = parseInt(p[0])-25 > 0 ? parseInt(p[0])-25 : 0;
			var y = parseInt(p[1])-25 > 0 ? parseInt(p[1])-25 : 0;

			var per = ~~( (point / max_point) * 100 );
			var color = "#" + (~~( per * 2.55 )).toString(16) + "0000";

			var $div = $(document.createElement('div'));
			$div.attr({
				"title":per + "% " + point
			}).css({
				"background-color": color,
				"position": "absolute",
				"top": y + "px",
				"left": x + "px",
				"width": "50px",
				"height": "50px",
				"filter": "alpha(opacity=50)",
				"-moz-opacity":"0.50",
				"opacity":"0.50",
				"z-index": 10000+per
			}).hover(function(){
				$(this).css({"border":"2px solid #FFFF00"});
			},function(){
				$(this).css({"border":"none"});
			});
			$canvas.append($div);
		});
	});
})(jQuery);
