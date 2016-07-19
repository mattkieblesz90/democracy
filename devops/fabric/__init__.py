from fabric.api import env, local, run, task
from fabtools.vagrant import vagrant

from .react import *


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


@task
def uname():
    run('uname -a')
