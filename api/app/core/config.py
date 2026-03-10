from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_env: str = "development"
    secret_key: str = "change-me"
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 60

    database_url: str = "postgresql+asyncpg://revfort:revfort@localhost:5432/revfort"
    redis_url: str = "redis://localhost:6379/0"

    allowed_origins: list[str] = ["http://localhost:3000", "http://localhost:3001"]

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
