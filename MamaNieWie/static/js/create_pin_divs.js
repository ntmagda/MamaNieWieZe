/**
 * Created by ntmagda on 4/20/2016.
 */

for (var i = 0; i < pin_slugs.length; i++) {
    var popup = document.createElement("div");
    var popup_title = document.createElement("div");
    var thumbnail = document.createElement('img');

    thumbnail.src = pin_thumbnails[i];
    popup.id = "popup_".concat(pin_slugs[i]);
    //popup_title.id = "pop_title_".concat(pin_slugs[i]);
    popup_title.innerHTML = pin_slugs[i];

    popup.appendChild(thumbnail);
    popup.appendChild(popup_title);
    document.body.appendChild(popup);
}
//
//<figure class="effect-lily">
//		<img src="img/1.jpg" alt="img01"/>
//		<figcaption>
//			<h2>Nice <span>Lily</span></h2>
//			<p>Lily likes to play with crayons and pencils</p>
//			<a href="#">View more</a>
//		</figcaption>
//	</figure>
