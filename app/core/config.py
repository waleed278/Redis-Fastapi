from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    redis_url: str = "redis://localhost:6379/0"

    cache_ttl_seconds: int = 60

    rate_limit_requests: int = 60
    rate_limit_window_seconds: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()