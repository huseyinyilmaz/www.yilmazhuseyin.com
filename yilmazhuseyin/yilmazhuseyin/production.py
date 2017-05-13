import raven
from os.path import expanduser

from yilmazhuseyin.settings import * # NOQA

DEBUG = False

LOGGING['handlers']['file']['filename'] = expanduser('/var/log/blog_application.log') # noqa

PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.cssmin.CSSMinCompressor' # noqa
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.uglifyjs.UglifyJSCompressor' # noqa

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        'KEY_PREFIX': 'blog',
    }
}


INSTALLED_APPS += [ # noqa
    'raven.contrib.django.raven_compat',
]

RAVEN_CONFIG = {
    'dsn': 'https://ce46e08f3f7e4a6f8c506c56216db533:3b9782e235db408d994323950afc97d5@sentry.io/165504',  # noqa
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.join(os.path.dirname(os.path.dirname(os.pardir)), '..')), # noqa
}
