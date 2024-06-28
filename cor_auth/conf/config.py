from pydantic_settings import BaseSettings
import glob

class Settings(BaseSettings):
    sqlalchemy_database_url: str = (
        "postgresql+psycopg2://user:password@localhost:5432/postgres"
    )
    postgres_user: str = "POSTGRES_USER"
    postgres_password: str = "POSTGRES_PASSWORD"
    postgres_host: str = "POSTGRES_HOST"
    postgres_port: int = 5432
    postgres_db: str = "POSTGRES_DB"
    algorithm: str = "ALGORITHM"
    secret_key: str = "SECRET_KEY"
    mail_username: str = "MAIL_USERNAME"
    mail_password: str = "MAIL_PASSWORD"
    mail_from: str = "Cor.Auth@EXAMPLE.COM"
    mail_port: int = 0
    mail_server: str = "MAIL_SERVER"
    pythonpath: str = "PYTHONPATH"
    encryption_key: str = "ENCRYPTION_KEY"
    app_env: str = "ENVIROMENT"
    debug: bool = "FALSE"
    signing_key: bytes = "SIGNING_KEY"
    signing_key_verification: bool = "TRUE"
    allowed_redirect_url_1: str ="ALLOWED_REDIRECT_URL"
    allowed_redirect_url_2: str ="ALLOWED_REDIRECT_URL"
    allowed_redirect_url_3: str ="ALLOWED_REDIRECT_URL"
    reload: bool = "False"

    class Config:

        env_files = glob.glob('./*.env')
        env_file = env_files[0] if env_files else '.env'
        env_file_encoding: str = "utf-8"



settings = Settings()
