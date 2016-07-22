from fabric.api import local


def setup_semantic():
    """
    Clone Semantic-UI and Semantic-UI-Docs repos (specific stable tags).
    """
    # Create vendors folder in tmp directory if not present.

    # Clone Semantic-UI repo if not present and install node modules

    # Clone Semantic-UI-Docs repo if not present and install node modules

    # Copy theme.config and semantic.json files to Semantic-UI repo

    # Rebuild docs
    pass


def setup_semantic_react():
    # Clone semantic-react repo if not present and install node modules (for JS replacement)

    # Build docs for semantic-react

    # copy semantic-react files to src/react/libs/semantic folder
    pass


def export_js_bundles():
    """
    Clears the /static/bundles folders and re-creates the bundles.

    This should be run every time we made changes to ReactJS before we commit
    and push our code.

    """
    local('rm -rf src/django/static/bundles/local/*.js')
    local('rm -rf src/django/static/bundles/stage/*.js')
    local('rm -rf src/django/static/bundles/prod/*.js')
    local('./node_modules/.bin/webpack --config conf/webpack/webpack.local.config.js --progress --colors')
    local('./node_modules/.bin/webpack --config conf/webpack/webpack.stage.config.js --progress --colors')
    local('./node_modules/.bin/webpack --config conf/webpack/webpack.prod.config.js --progress --colors')


def export_css_bundles():
    """
    For css UI we use Semantic-UI framework with it's configuration variables and
    overrides.
    """
    # run gulp build-css and build-assets

    # copy min files to stage and bundle and non minified to local bundle

    # copy assets to each assets bundle folders
    pass


def run_styleguide():
    """
    Runs styleguide servers provided by Semantic-UI-Docs and semantic-react
    on different ports.
    """
    # serve docs for semantic ui

    # serve docs for semantic-react
    pass
