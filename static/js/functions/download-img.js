function load(content) {

	const view = `
		<div class="d-flex justify-content-center">
		  <div class="spinner-border text-info" style="width: 6rem; height: 6rem;" role="status">
		    <span class="visually-hidden">Loading...</span>
		  </div>
		</div>
	`
	content.innerHTML = view;
}

function after_download_image(path_image, content) {
	
	const new_card = `
		<div class="card" style="width: 18rem;">
		  <div class="card-body">
		    <h5 class="card-title text-center">GENQR</h5>
		   	<p class="card-text">Descarga Exitosa.</p>
 			<a href="/" class="card-link">Ir a inicio</a>
		    <a href="${path_image}" download = "codeqr.png" onclick() class="card-link">Volver a descargar...</a>
		  </div>
		</div>
	`;

	content.innerHTML = new_card;
}


document.getElementById('download-img').addEventListener('click', () => {

	const message = document.getElementById("card-message");
	const tag = document.createElement('a');
	
	tag.href = document.getElementById('data-img').src;
	
	tag.download = "codeqr.png";

	
	document.getElementById("card-content").innerHTML = "";

	load(message)

	setTimeout(() => {
		tag.click();

		after_download_image(tag.href, message)
	}, 1520, tag)

})

