function scope() {
    var chosen_album = "none";

    function selectAlbum(element, curr_element) {
        console.log("chosen is: " + chosen_album);
        if (chosen_album != "none") {
            chosen_album.toggle();
        }
        chosen_album = element;
        chosen_album.toggle();
    }

    function getIframe(url, element) {
        console.log("getting iframe for: " + url);
        SC.oEmbed(url, {
            auto_play : false,
            maxheight : 100,
            maxwidth : 600,
            color : "660066",
        }, function(oembed) {
            console.log('embed return: ' + oembed.title)
            console.log('embed return: ' + oembed.html)
            element.html(oembed.html);
        });
    }

    $(document).ready(
            function() {
                $("#dan-body").show()
                $("#button-body").click(function() {
                    $("#dan-contact").hide();
                    $("#dan-body").show();
                });
                $("#button-contact").click(function() {
                    $("#dan-contact").show();
                    $("#dan-body").hide();
                });

                $(".album-table").each(
                        function() {
                            $(this).find(".track").each(
                                    function() {
                                        getIframe($(this).find(".track-url")
                                                .html(), $(this).find(
                                                ".track-title"));
                                    });
                        });
                $(".album-button").click(function() {
                    var row = "album-" + $(this).attr("id");
                    var element = $(document).find("#" + row);
                    selectAlbum(element);
                });
                $(".track").click(function(e) {
                    var url = $(this).find(".track-url").html();
                    getIframe(url, $(this).find(".track-title"));
                })
            });
};
scope();
