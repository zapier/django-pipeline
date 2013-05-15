from __future__ import unicode_literals

from django.conf import settings

PIPELINE = getattr(settings, 'PIPELINE', not settings.DEBUG)

PIPELINE_ROOT = getattr(settings, 'PIPELINE_ROOT', settings.STATIC_ROOT)
PIPELINE_URL = getattr(settings, 'PIPELINE_URL', settings.STATIC_URL)

PIPELINE_STORAGE = getattr(settings, 'PIPELINE_STORAGE',
                           'pipeline.storage.PipelineFinderStorage')

PIPELINE_CSS_COMPRESSOR = getattr(settings, 'PIPELINE_CSS_COMPRESSOR',
                                  'pipeline.compressors.yuglify.YuglifyCompressor')
PIPELINE_JS_COMPRESSOR = getattr(settings, 'PIPELINE_JS_COMPRESSOR',
                                 'pipeline.compressors.yuglify.YuglifyCompressor')
PIPELINE_COMPILERS = getattr(settings, 'PIPELINE_COMPILERS', [])

PIPELINE_CSS = getattr(settings, 'PIPELINE_CSS', {})
PIPELINE_JS = getattr(settings, 'PIPELINE_JS', {})

PIPELINE_TEMPLATE_NAMESPACE = getattr(settings, 'PIPELINE_TEMPLATE_NAMESPACE', "window.JST")
PIPELINE_TEMPLATE_EXT = getattr(settings, 'PIPELINE_TEMPLATE_EXT', ".jst")
PIPELINE_TEMPLATE_FUNC = getattr(settings, 'PIPELINE_TEMPLATE_FUNC', "template")

PIPELINE_DISABLE_WRAPPER = getattr(settings, 'PIPELINE_DISABLE_WRAPPER', False)

PIPELINE_CSSTIDY_BINARY = getattr(settings, 'PIPELINE_CSSTIDY_BINARY', '/usr/bin/env csstidy')
PIPELINE_CSSTIDY_ARGUMENTS = getattr(settings, 'PIPELINE_CSSTIDY_ARGUMENTS', '--template=highest')

PIPELINE_YUGLIFY_BINARY = getattr(settings, 'PIPELINE_YUGLIFY_BINARY', '/usr/bin/env yuglify')
PIPELINE_YUGLIFY_CSS_ARGUMENTS = getattr(settings, 'PIPELINE_YUGLIFY_CSS_ARGUMENTS', '--terminal')
PIPELINE_YUGLIFY_JS_ARGUMENTS = getattr(settings, 'PIPELINE_YUGLIFY_JS_ARGUMENTS', '--terminal')

PIPELINE_YUI_BINARY = getattr(settings, 'PIPELINE_YUI_BINARY', '/usr/bin/env yuicompressor')
PIPELINE_YUI_CSS_ARGUMENTS = getattr(settings, 'PIPELINE_YUI_CSS_ARGUMENTS', '')
PIPELINE_YUI_JS_ARGUMENTS = getattr(settings, 'PIPELINE_YUI_JS_ARGUMENTS', '')

PIPELINE_CLOSURE_BINARY = getattr(settings, 'PIPELINE_CLOSURE_BINARY', '/usr/bin/env closure')
PIPELINE_CLOSURE_ARGUMENTS = getattr(settings, 'PIPELINE_CLOSURE_ARGUMENTS', '')

PIPELINE_UGLIFYJS_BINARY = getattr(settings, 'PIPELINE_UGLIFYJS_BINARY', '/usr/bin/env uglifyjs')
PIPELINE_UGLIFYJS_ARGUMENTS = getattr(settings, 'PIPELINE_UGLIFYJS_ARGUMENTS', '')

PIPELINE_CSSMIN_BINARY = getattr(settings, 'PIPELINE_CSSMIN_BINARY', '/usr/bin/env cssmin')
PIPELINE_CSSMIN_ARGUMENTS = getattr(settings, 'PIPELINE_CSSMIN_ARGUMENTS', '')

PIPELINE_COFFEE_SCRIPT_BINARY = getattr(settings, 'PIPELINE_COFFEE_SCRIPT_BINARY', '/usr/bin/env coffee')
PIPELINE_COFFEE_SCRIPT_ARGUMENTS = getattr(settings, 'PIPELINE_COFFEE_SCRIPT_ARGUMENTS', '')

PIPELINE_LIVE_SCRIPT_BINARY = getattr(settings, 'PIPELINE_LIVE_SCRIPT_BINARY', '/usr/bin/env lsc')
PIPELINE_LIVE_SCRIPT_ARGUMENTS = getattr(settings, 'PIPELINE_LIVE_SCRIPT_ARGUMENTS', '')

PIPELINE_SASS_BINARY = getattr(settings, 'PIPELINE_SASS_BINARY', '/usr/bin/env sass')
PIPELINE_SASS_ARGUMENTS = getattr(settings, 'PIPELINE_SASS_ARGUMENTS', '')

PIPELINE_STYLUS_BINARY = getattr(settings, 'PIPELINE_STYLUS_BINARY', '/usr/bin/env stylus')
PIPELINE_STYLUS_ARGUMENTS = getattr(settings, 'PIPELINE_STYLUS_ARGUMENTS', '')

PIPELINE_LESS_BINARY = getattr(settings, 'PIPELINE_LESS_BINARY', '/usr/bin/env lessc')
PIPELINE_LESS_ARGUMENTS = getattr(settings, 'PIPELINE_LESS_ARGUMENTS', '')

PIPELINE_MIMETYPES = getattr(settings, 'PIPELINE_MIMETYPES', (
    ('text/coffeescript', '.coffee'),
    ('text/less', '.less'),
    ('text/javascript', '.js'),
    ('text/x-sass', '.sass'),
    ('text/x-scss', '.scss')
))

PIPELINE_EMBED_MAX_IMAGE_SIZE = getattr(settings, 'PIPELINE_EMBED_MAX_IMAGE_SIZE', 32700)
PIPELINE_EMBED_PATH = getattr(settings, 'PIPELINE_EMBED_PATH', r'[/]?embed/')

if PIPELINE_COMPILERS is None:
    PIPELINE_COMPILERS = []
