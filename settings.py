import secrets


class BasicConfig:
	SECRET_KEY = secrets.token_hex()


class DevelopmetConfig(BasicConfig):
	DEBUG = True


config = {
	'development': DevelopmetConfig
}