from contextlib import contextmanager as _contextmanager  # noqa

from fabric.api import abort, cd, env, local, prefix, prompt, run, sudo
from fabric.colors import green, red, yellow  # noqa
from pyfiglet import Figlet  # noqa

from fabric.api import settings  # noqa; noqa


# env.use_ssh_config = True
env.forward_agent = True
env.user = "ubuntu"
env.hosts = [""]
env.directory = "/home/ubuntu/var/www/{project_name}"
env.activate = "source {}/venv/bin/activate".format(env.directory)
run.replace_env = True

APP_DIR = "~/var/www/{project_name}"
SUPERVISOR_APP_NAME = ["{project_name}"]

figlet = Figlet(font="slant")


def _sudo_patch(*args, **kwargs):
    return sudo(*args, **kwargs)


_sudo = _sudo_patch


@_contextmanager
def _virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            yield


def _pull_master():
    with cd(APP_DIR):
        run("git pull origin master")


def set_requirements():
    run("pip install -r requirements.txt")


def restart_supervisord():
    with cd(APP_DIR):
        with _virtualenv():
            for app in SUPERVISOR_APP_NAME:
                _sudo_patch("supervisorctl restart {}".format(app))


def deploy():
    _confirm()
    with cd(APP_DIR):
        with _virtualenv():
            _pull_master()
            set_requirements()
            run("python src/manage.py migrate")
            run("make css")
            run("python src/manage.py collectstatic --no-input")
            restart_supervisord()


def update_nginx_conf():
    _pull_master()
    _sudo_patch(
        "sudo cp var/www/{project_name}/config/nginx.conf /etc/nginx/sites-available/{{project_name}}"
    )
    _sudo_patch("sudo nginx -t")
    _sudo_patch("sudo service nginx restart")


def _confirm():
    response = prompt(
        """
        SAY YES IN CAPS TO DEPLOY ===>
        """
    )
    if response != "YES":
        abort(red("ABORTING DEPLOYMENT"))

        local("clear")
    print(green(figlet.renderText("DEPLOYING PRODUCTION")))
