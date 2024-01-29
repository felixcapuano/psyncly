from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_type: str = "sqlite"
    database: str = "./psyncly.db"


settings = Settings()
