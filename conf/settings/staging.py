from .common import *

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/stage/',  # end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'conf', 'webpack', 'webpack-stats-stage.json'),
    }
}
