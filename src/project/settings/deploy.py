import raven

from .base import *

ALLOWED_HOSTS += [

]

DEBUG = False

RAVEN_LOGIN = os.environ.get('RAVEN_LOGIN')
RAVEN_PASSWORD = os.environ.get('RAVEN_PASSWORD')

RAVEN_CONFIG = {
    'dsn': 'https://{}:{}@sentry.io/176021'.format(RAVEN_LOGIN, RAVEN_PASSWORD),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.dirname(BASE_DIR)),
}
