jQuery(document).ready(function() {
        jQuery('img.svg').each(function(){
            var mouseX;
            var mouseY;
            var $img = jQuery(this);
            var imgURL = $img.attr('src');

            jQuery.get(imgURL, function (data) {
            // Get the SVG tag, ignore the rest
            var $svg = jQuery(data).find('svg');

            // Replace image with new SVG
            $img.replaceWith($svg);

            // Add an handler
            jQuery('#pins path').each(function () {

                var post_slug = jQuery(this).attr('id');
                var post_id = "popup_".concat(post_slug);
                var mouseX;
                var mouseY;
                jQuery(this).click(function () {
                    var url = "http://127.0.0.1:8000/posts/post_slug".replace("post_slug", post_slug); //TODO
                    window.location = url;
                });

                $(this).hover(function(e) {
                    mouseX = e.pageX;
                    mouseY = e.pageY;
                    $('#'+ post_id).fadeIn();
                    $('#'+ post_id).css({top: (mouseY - 150) + "px", left: (mouseX - 150) + "px"});
                });

                $('#'+ post_id).mouseleave(function(){
                    setTimeout(function () {
                      $('#'+ post_id).fadeOut();
                    },500);
                });

                jQuery('#'+ post_id).mouseover(function () {
                    // using string concat due to name conficts with "path id" in svg map
                    document.getElementById("popup_".concat(post_slug)).style.display = 'block';

                });

            });
        });
    });
 });

        