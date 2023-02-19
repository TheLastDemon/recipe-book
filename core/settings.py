from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB_HOST = 'localhost'
    POSTGRES_DB_PORT = 5432
    POSTGRES_DB_NAME = 'postgres'
    POSTGRES_DB_USER = 'postgres'
    POSTGRES_DB_PASSWORD = 'postgres'

    CACHE_REDIS_DB_HOST = 'localhost'
    CACHE_REDIS_DB_PORT = 1234
    CACHE_REDIS_DB_NAME = '_db'
    CACHE_REDIS_DB_USER = 'redis'
    CACHE_REDIS_DB_PASSWORD = 'redis'
    CACHE_REDIS_URL = '?'


settings = Settings(_env_file='.env')
