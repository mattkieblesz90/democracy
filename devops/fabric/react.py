from fabric.api import local


def webpack():
    """
    Clears the /static/bundles folders and re-creates the bundles.

    This should be run every time we made changes to ReactJS before we commit
    and push our code.

    """
    local('rm -rf src/django/static/bundles/local/*')
    local('rm -rf src/django/static/bundles/stage/*')
    local('rm -rf src/django/static/bundles/prod/*')
    local('./node_modules/.bin/webpack --config conf/webpack/webpack.local.config.js --progress --colors')
    local('./node_modules/.bin/webpack --config conf/webpack/webpack.stage.config.js --progress --colors')
    local('./node_modules/.bin/webpack --config conf/webpack/webpack.prod.config.js --progress --colors')
