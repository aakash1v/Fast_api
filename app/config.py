
from pydantic_settings import BaseSettings,SettingsConfigDict
import os

DOTENV = os.path.join(os.path.dirname(__file__), "../.env")

class Settings(BaseSettings):
    database_hostname :str
    database_port :str
    database_password :str
    database_name :str
    database_username :str
    secret_key :str
    algorithm: str
    access_token_expire_minutes :int


    model_config = SettingsConfigDict(env_file=DOTENV)
    # class Config:
    #     env_file = ".env"  # Works with uvicorn run command from my-app/project/
        # env_file = "../.env"  Works with alembic command from my-app/alembic
        # env_file = abs_path_env

    
settings = Settings()


# @lru_cache()
# def get_settings():
#     return Settings()
