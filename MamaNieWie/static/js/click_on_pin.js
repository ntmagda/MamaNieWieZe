jQuery(document).ready(function() {
        jQuery('img.svg').each(function(){
            var $img = jQuery(this);
            var imgID = $img.attr('id');
            var imgURL = $img.attr('src');

            jQuery.get(imgURL, function (data) {
            // Get the SVG tag, ignore the rest
            var $svg = jQuery(data).find('svg');

            // Replace image with new SVG
            $img.replaceWith($svg);

            // Add an handler
            jQuery('#Iceland').each(function () {
                jQuery(this).click(function () {
                    var post_id = jQuery(this).attr('id');
                    var url = '{% url blog_view_post 999 %}'.replace(999, post_id);
                    return url;
                });
            });
        });

    });
 });

        