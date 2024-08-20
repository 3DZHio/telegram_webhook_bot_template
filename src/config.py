from dotenv import load_dotenv
from pydantic import SecretStr, PostgresDsn, RedisDsn, HttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings, case_sensitive=True):
	load_dotenv()
	
	## MAIN ##
	# Pending Updates #
	DROP: int
	
	# Logging #
	LOG_LEVEL: int
	
	# Admin #
	ADMIN_IDS: SecretStr
	
	## PREREQUISITES ##
	# Bot #
	BOT_TOKEN: SecretStr
	
	# WebHook #
	WEBHOOK_HOST: SecretStr
	WEBHOOK_PORT: SecretStr
	WEBHOOK_PATH: SecretStr
	WEBHOOK_DOMAIN: SecretStr
	WEBHOOK_SECRET: SecretStr
	
	# Storage #
	STG_HOST: SecretStr
	STG_PORT: SecretStr
	STG_NAME: SecretStr
	
	# DataBase #
	DB_USER: SecretStr
	DB_PASSWORD: SecretStr
	DB_HOST: SecretStr
	DB_PORT: SecretStr
	DB_NAME: SecretStr
	
	## PROPRETIES ##
	@property
	def webhook_url(self) -> HttpUrl:
		return f"https://{self.WEBHOOK_DOMAIN.get_secret_value()}/{settings.WEBHOOK_PATH.get_secret_value()}"
	
	@property
	def storage_dsn(self) -> PostgresDsn:
		return (
			"redis"
			f"://{settings.STG_HOST.get_secret_value()}"
			f":{settings.STG_PORT.get_secret_value()}"
			f"/{settings.STG_NAME.get_secret_value()}"
		)
	
	@property
	def database_dsn(self) -> RedisDsn:
		return (
			"postgres"
			f"://{settings.DB_USER.get_secret_value()}"
			f":{settings.DB_PASSWORD.get_secret_value()}"
			f"@{settings.DB_HOST.get_secret_value()}"
			f":{settings.DB_PORT.get_secret_value()}"
			f"/{settings.DB_NAME.get_secret_value()}"
		)


settings = Settings()
