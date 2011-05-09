(function($){
	function getR(c) {
		if(c < 128){
			color = 0;
		}else if(c > 127 && c < 191){
			color = (c-127)*4;
		}else if(c > 190){
			color = 255;
		}
		return color;
	}
	function getG(c) {
		if(c >= 64 && c <= 191){
			color = 255;
		}else if(c < 64){
			color =  c * 4;
		}else{
			color = 256-(c-191)*4;
		}
		return color;
	}
	function getB(c) {
		if(c <= 64){
			color = 255;
		}else if(c > 64 && c < 127){
			color = 255-(c-64)*4;
		}else if(c >= 127){
			color = 0;
		}
		return color;
	}
	function toHex(h) {
		return h > 16 ? h.toString(16) : "0"+h.toString(16);
	}
	function getColor(c) {
		var r = getR(c);
		var g = getG(c);
		var b = getB(c);
		return "#" + toHex(r) + toHex(g) + toHex(b);
	}

	var pointScale = 10;
	var pointScaleHalf = pointScale/2;
	
	var $frame = $("#thermography_frame");
	$frame.height($(window).height()-20);
	var $fw = $($frame[0].contentWindow);
	$frame.bind('load.thermography', function(){
//		console.log("thermography_frame loaded.");
		var $fb = $($frame[0].contentWindow.document.body);
		var $canvasDiv = $(document.createElement('div')).css({
			"z-index":1000,
			"position":"absolute",
			"top":0,
			"left":0,
			"width":"100%",
			"height":$($frame[0].contentWindow.document).height()+"px",
			"background":"#000",
			"opacity":"0.45",
			"-moz-opacity":"0.45",
			"filter":"alpha(opacity=45)"
		}).attr("id","thermography_canvas");
		$fb.prepend($canvasDiv);
	
		var $canvas = $("#thermography_canvas", $fb);
		jQuery.each(points, function(position, point){
			var p = position.split(":");
			var x = parseInt(p[0])-pointScaleHalf > 0 ? parseInt(p[0])-pointScaleHalf : 0;
			var y = parseInt(p[1])-pointScaleHalf > 0 ? parseInt(p[1])-pointScaleHalf : 0;

			var per = ~~( (point / max_point) * 100 );
			var color = getColor( ~~( per * 2.55 ) );
//			console.log("color=%s", color);

			var $div = $(document.createElement('div'));
			$div.attr({
				"title":per + "% " + point
			}).css({
				"background-color": color,
				"position": "absolute",
				"top": y + "px",
				"left": x + "px",
				"width": pointScale + "px",
				"height": pointScale + "px",
				"filter": "alpha(opacity=75)",
				"-moz-opacity":"0.75",
				"opacity":"0.75",
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
