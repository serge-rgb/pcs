function getIframe(url, element) {
	console.log("getting iframe for: " + url);
	SC.oEmbed(url, {
		auto_play : false
	}, function(oembed) {
		console.log('embed return: ' + oembed.title)
		console.log('embed return: ' + oembed.html)
		element.html(oembed.html);
	});
}

$(document).ready(function() {
	$(".album-table").each(function() {
		$(this).find(".track").each(function() {
			getIframe($(this).find(".track-url").html(),
					$(this).find(".track-title"));
		});
	});
	$(".album-button").click(function() {
		var row = "album-" + $(this).attr("id");
		var element = $(document).find("#"+row);
		element.toggle();
	});
	$(".track").click(function(e) {
		var url = $(this).find(".track-url").html();
		getIframe(url, $(this).find(".track-title"));
	})
});