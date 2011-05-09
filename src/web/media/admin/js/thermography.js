(function($){
	var $frame = $("#thermography_frame");
	$frame.height($(window).height()-20);
	var $fw = $($frame[0].contentWindow);
	$frame.bind('load.thermography', function(){
		var $fb = $($frame[0].contentWindow.document.body);
		$fb.heatmap({}, points, max_point);
	});
})(jQuery);
