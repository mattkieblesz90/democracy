from fabric.api import env, local, run, task

from .build_static import *


def vault_files(vault_action='encrypt'):
    """
    Encrypt files with passwords before committing to repo.

    """
    files_list = [
        "devops/ansible/env_vars/base.yml",
        "devops/ansible/roles/web/vars/main.yml"
    ]
    local(
        'ansible-vault %s %s --vault-password-file=%s'
        % (vault_action, " ".join(files_list), "~/.vault_pass.txt")
    )


def setup_deploy():
    setup_semantic()
    setup_semantic_react()


def prepare_deploy(vault=False):
    if vault:
        vault_files()

    export_js_bundles()
    export_css_bundles()
