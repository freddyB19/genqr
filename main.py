import pyqrcode

from flask import Flask
from flask import request
from flask import url_for
from flask import session
from flask import redirect
from flask import send_file
from flask import render_template
from flask_wtf.csrf import CSRFProtect


import settings
from forms import GenCodeQr


app = Flask(__name__)
app.config.from_object(settings.config['development'])

csrf = CSRFProtect(app)

@app.before_request
def before():
	if request.endpoint == 'get_code_qr' and 'codeqr' not in session:
		return redirect( url_for ('index') )


@app.route("/", methods = ['GET', 'POST'])
def index():
	form = GenCodeQr(request.form)

	if request.method == 'POST' and form.validate():
		session['codeqr'] = form.data.get('url')
		return redirect( url_for ('get_code_qr') )

	context = {
		'form': form
	}
	return render_template('index.html', **context)


@app.route("/qrcode", methods = ['GET'])
def get_code_qr():
	path = session.pop('codeqr')
	img = pyqrcode.create(path, mode="binary")
	path_img = img.png_as_base64_str(scale = 8)

	context = {
		'img': path_img
	}
	return render_template('codeqr.html', **context)


if __name__ == "__main__":
	app.run()