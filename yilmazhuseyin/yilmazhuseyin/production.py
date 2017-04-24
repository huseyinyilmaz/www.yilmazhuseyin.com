from os.path import expanduser

from yilmazhuseyin.settings import * # NOQA

DEBUG = False

LOGGING['handlers']['file']['filename'] = expanduser('/var/log/blog_application.log') # noqa

PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.cssmin.CSSMinCompressor' # noqa
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.uglifyjs.UglifyJSCompressor' # noqa
