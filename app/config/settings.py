from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_port: int = 5000
    db_name: str = "test"
    db_password: str
    db_user: str
    db_host: str
    secret_key: str
    algorithm: str
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

settings = Settings()

if __name__== "__main__":
   print(settings.db_name)
