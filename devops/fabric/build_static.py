from fabric.api import local, lcd
from fabric.context_managers import cd


__all__ = [
    "setup_semantic", "setup_semantic_react", "export_js_bundles", "export_css_bundles",
    "run_styleguide"]


def setup_semantic():
    """
    Clone Semantic-UI and Semantic-UI-Docs repos (specific stable tags).
    """
    # Create vendors folder in tmp directory if not present.
    local("mkdir -p tmp/vendors")

    # Clone Semantic-UI repo if not present
    local("if cd tmp/vendors/semantic-ui; then git pull; else git clone --branch 2.2.2 \
        https://github.com/Semantic-Org/Semantic-UI.git tmp/vendors/semantic-ui; fi")
    # Clone Semantic-UI-Docs repo if not present
    local("if cd tmp/vendors/semantic-ui-docs; then git pull; else git clone \
        https://github.com/Semantic-Org/Semantic-UI-Docs.git tmp/vendors/semantic-ui-docs; fi")
    # Directory for built docs
    local("mkdir -p tmp/vendors/docs")

    # Copy theme.config and semantic.json files to Semantic-UI repo
    with cd("tmp/vendors/semantic-ui"):
        local("npm install")

    # let's install dockpad locally in docs folder
    local("cp tmp/vendors/semantic-ui-docs/package.json tmp/vendors/docs/package.json")
    with lcd("tmp/vendors/docs"):
        local("npm install")


def setup_semantic_react():
    # Clone semantic-react repo if not present and install node modules (for JS replacement)
    # this is just for docs
    with lcd("tmp/vendors"):
        local("if cd semantic-react; then git pull; else git clone \
        https://github.com/mattkieblesz/semantic-react.git semantic-react; fi")

    with lcd("tmp/vendors/semantic-react"):
        local("npm install react react-dom react-addons-shallow-compare")
        local("npm install")


def export_js_bundles():
    """
    Clears the /static/bundles folders and re-creates the bundles.

    This should be run every time we made changes to ReactJS before we commit
    and push our code.

    """
    local("mkdir -p src/react/libs/semantic-react")
    local('rm -rf src/react/libs/semantic-react/*')
    local("cp -r tmp/vendors/semantic-react/src/components/* src/react/libs/semantic-react/")

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
    # copy configs
    local("cp conf/semantic/semantic.json tmp/vendors/semantic-ui/semantic.json")
    local("cp conf/semantic/theme.config tmp/vendors/semantic-ui/src/theme.config")
    local("cp conf/semantic/docs.js tmp/vendors/semantic-ui/tasks/config/docs.js")

    # run gulp build-css and build-assets
    with lcd("tmp/vendors/semantic-ui"):
        local("gulp build-css")
        local("cp dist/semantic.css ../../../src/django/static/bundles/local/styles.css")
        local("cp dist/semantic.min.css ../../../src/django/static/bundles/stage/styles.css")
        local("cp dist/semantic.min.css ../../../src/django/static/bundles/prod/styles.css")

        local("gulp build-assets")
        local("cp -r dist/themes ../../../src/django/static/bundles/local/")
        local("cp -r dist/themes ../../../src/django/static/bundles/stage/")
        local("cp -r dist/themes ../../../src/django/static/bundles/prod/")


def setup_styleguide():
    # Build docs for semantic-ui
    with lcd("tmp/vendors/semantic-ui"):
        local("gulp build-docs")


def run_styleguide():
    """
    Runs styleguide servers provided by Semantic-UI-Docs and semantic-react
    on different ports.
    """
    # watch for changes
    with lcd("tmp/vendors/semantic-ui"):
        local("gulp serve-docs")

    # serve docs for semantic ui
    with lcd("tmp/vendors/docs"):
        local("dockpad run")

    # serve docs for semantic-react
    # ...
