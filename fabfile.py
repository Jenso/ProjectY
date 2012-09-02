from fabric.api import sudo, env, cd, run, local
from fabric.contrib.console import confirm
import datetime

# production server, expects accepted ssh key on server
try:
    from fabsettings import host
    env.hosts = host
except:
    env.hosts = ['proxz@lookify.se']
env.directory = '/home/ubuntu/ProjectY'
env.activate = 'source /home/ubuntu/ProjectY/projecty/bin/activate'
env.deploy_user = 'ubuntu'

"""
TODO: Write local deploy script with local()
instead of current bash script.
"""


def _cd_project_root():
    return cd(env.directory)


def _activate():
    return sudo(env.activate, user=env.deploy_user)


# Base commands

def virtualenv(command):
    """
    Execute commands in virtualenv, as env.deploy_user
    """
    with _cd_project_root():
        sudo(env.activate + '&&' + command, user=env.deploy_user)


def manage(cmd):
    with _cd_project_root():
        virtualenv('python manage.py ' + cmd)


def git_pull(remote='origin', branch='master'):
    'Updates the repository.'
    with _cd_project_root():
        sudo('git pull %s %s' % (remote, branch), user=env.deploy_user)


# High-level commands

def install_requirements():
    virtualenv("pip install -r requirements.txt")


def test():
    """ Don't go through with deploy if any test fail """
    local('python manage.py test --settings=settings.test')


def collectstatic():
    virtualenv("./manage.py collectstatic --noinput")

def compress():
    virtualenv("./manage.py compress")

def compile_less():
    """ TODO: Compile all files in a folder instead """
    virtualenv("lessc bootstrap/static/less/bootstrap.less "
                     "bootstrap/static/css/styl.css")


def backup_database():
    """ TODO: Do not require password to backup the db """
    now = datetime.datetime.now()
    filename = ("/home/ubuntu/database_backup/lookify_db_"
                + now.strftime("%y%m%d-%H-%M") + ".sql")
    sudo("mysqldump -u root -p django_stylematch > " + filename)


def migrate():
    manage('migrate')


# Server commands

def restart_nginx():
    sudo("/etc/init.d/nginx restart")


def restart_gunicorn():
    sudo("restart lookify")


def top():
    sudo("top")


def update_git_submodules():
    with _cd_project_root():
        sudo('git submodule init', user=env.deploy_user)
        sudo('git submodule update', user=env.deploy_user)


def revert():
    """ Revert git via reset --hard @{1} """
    with _cd_project_root():
        run('git reset --hard @{1}')
        restart_gunicorn()


def deploy_db_change(branch='master'):
    #backup_database()
    git_pull(branch=branch)
    install_requirements()
    update_git_submodules()
    migrate()
    #compress()
    collectstatic()
    restart_gunicorn()


def deploy(branch='master'):
    git_pull(branch=branch)
    install_requirements()
    update_git_submodules()
    #compress()
    collectstatic()
    restart_gunicorn()
