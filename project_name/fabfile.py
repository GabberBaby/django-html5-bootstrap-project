from __future__ import with_statement
from fabric.api import local, cd, run, env, sudo, settings
from fabric.context_managers import prefix


def dev():
    env.hosts = ['XXX.XXX.XXX.XXX',]
    env.host_string = env.hosts[0]
    env.project_path = '/projects/{{ project_name }}dev/{{ project_name }}'
    env.virtualenv_path = '/projects/.python-env/{{ project_name }}dev'
    env.activate_cmd = ('source %s/bin/activate' % env.virtualenv_path)
    env.prefix = '%s && cd %s' % (env.activate_cmd, env.project_path)
    env.supervisord_name = '{{ project_name }}dev'

def prod():
    env.hosts = ['XXX.XXX.XXX.XXX',]
    env.host_string = env.hosts[0]
    env.project_path = '/projects/{{ project_name }}prod/{{ project_name }}'
    env.virtualenv_path = '/projects/.python-env/{{ project_name }}prod'
    env.activate_cmd = ('source %s/bin/activate' % env.virtualenv_path)
    env.prefix = '%s && cd %s' % (env.activate_cmd, env.project_path)
    env.supervisord_name = '{{ project_name }}prod'

def deploy():
    pull()
    install_requirements()
    syncdb()
    migrate()
    collectstatic()
    restart_workers()

def pull():
    with prefix(env.prefix):
        run('git pull')

def syncdb():
    with prefix(env.prefix):
        run('manage.py syncdb --noinput')

def migrate():
    with prefix(env.prefix):
        run('manage.py migrate')

def collectstatic():
    with prefix(env.prefix):
        run('manage.py collectstatic --noinput')

def install_requirements():
    with prefix(env.prefix):
        run('pip install -r ../requirements.txt')

def restart_workers():
    sudo("supervisorctl restart %s" % env.supervisord_name)

def restart_webserver():
    sudo('/etc/init.d/nginx reload')
