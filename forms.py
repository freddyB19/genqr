from flask_wtf import FlaskForm
from wtforms import URLField
from wtforms import SubmitField
from wtforms import validators
from wtforms import StringField


class GenCodeQr(FlaskForm):
	url = URLField("URL", validators = [
			validators.DataRequired(message = 'es requerido este campo.')
		]
	)

	class Meta:
		csrf = True
