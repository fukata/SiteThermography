(function($){
	var $frame = $("#thermography_frame");
	$frame.height($(window).height()-20);
	var $fw = $($frame[0].contentWindow);
	$frame.bind('load.thermography', function(){
		console.log("thermography_frame loaded.");
		var $fb = $($frame[0].contentWindow.document.body);
		$fb.heatmap({scale:30}, points, max_point);
	});
})(jQuery);
