from .base import *
import os

DEBUG = True

ALLOWED_HOSTS += ['127.0.0.1', 'localhost', 'example.dj']

INTERNAL_IPS = ['127.0.0.1']

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": os.environ.get('REDIS_URL', 'localhost:6379'),
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient"
#         }
#     }
# }

RAVEN_LOGIN = os.environ.get('RAVEN_LOGIN')
RAVEN_PASSWORD = os.environ.get('RAVEN_PASSWORD')

RAVEN_CONFIG = {
    'dsn': 'https://{}:{}@sentry.io/176021'.format(RAVEN_LOGIN, RAVEN_PASSWORD),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.dirname(BASE_DIR)),
}
