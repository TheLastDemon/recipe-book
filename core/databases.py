from peewee import PostgresqlDatabase

from core.settings import settings

postgres_database = PostgresqlDatabase(
    host=settings.POSTGRES_DB_HOST,
    port=settings.POSTGRES_DB_PORT,
    database=settings.POSTGRES_DB_NAME,
    user=settings.POSTGRES_DB_USER,
    password=settings.POSTGRES_DB_PASSWORD
)

cache_redis_database = {
        'CACHE_TYPE': 'redis',
        'CACHE_KEY_PREFIX': 'fcache',
        'CACHE_REDIS_HOST': settings.CACHE_REDIS_DB_HOST,
        'CACHE_REDIS_PORT': settings.CACHE_REDIS_DB_PORT,
        'CACHE_REDIS_PASSWORD': settings.CACHE_REDIS_DB_PASSWORD
}