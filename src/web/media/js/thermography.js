(function($){
	var data = {
		url: document.URL,
		activate_code: _st.activate_code || '',
		move_events: [],
		unload_event: null,
	};

	$(window).scroll(function(event){
		//console.log(event);
		//console.log("%s, %s", event.pageX, event.pageY);
	});

	$(window).mousemove(function(event){
		//console.log("%s, %s", event.pageX, event.pageY);
		data.move_events.push({
			timeStamp: event.timeStamp,
			pageX: event.pageX,
			pageY: event.pageY
		});
	});

	$(window).unload(function(event){
		//console.log("unload track");
		//data.unload_event = event;
		$.ajax({
			cache: false,
			async: false,
//			url: "http://localhost:8080/track",
			url: "http://site-thermography.appspot.com/track",
			type: "POST",
			data: {"data": JSON.stringify(data)}
		});
	});
})(jQuery);
