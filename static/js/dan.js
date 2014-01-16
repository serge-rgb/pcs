function getTitle(url, element) {
	console.log("getting title for: " + url);
	SC.get(url, function(tracks) {
		console.log("title is: " + tracks[0].title);
	});
}

function getIframe(url, element) {
	console.log("getting iframe for: " + url);
	var html = "<iframe/>";
	SC.oEmbed(url, {}, function(oembed) {
		console.log('embed return: ' + oembed.title)
		console.log('embed return: ' + oembed.html)
		element.html(oembed.html);
	});
} 

$(document).ready(function() {
	$("#foo").click(function() {
		var id = $("#foo-last-time-url").html();
		getTitle(id, $("#foo-last-time-title"));
	});
	$("#foo-last-time-table").click(function() {
		console.log($("#foo-last-time-url").html());
	})
});