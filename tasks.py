import shlex

from invoke import task
from invoke.main import program
from livereload import Server
from pelican import main as pelican_main
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file


ROOT_DIR = 'sbau2021/'

SETTINGS_FILE = ROOT_DIR + 'settings.py'
PROD_SETTINGS_FILE = ROOT_DIR + 'settings_prod.py'

EXTENTIONS = {
    'static': ('.scss', '.css', '.js'),
    'content': ('.md', '.rst'),
}

HOST = 'localhost'
PORT = 8000


def get_settings(prod=False):
    settings = {}
    settings.update(DEFAULT_CONFIG)
    settings.update(get_settings_from_file(
        PROD_SETTINGS_FILE if prod else SETTINGS_FILE
    ))
    return settings


def pelican_run(cmd):
    import sbau2021
    # Allows to pass-through arguments to Pelican
    pelican_main(shlex.split(cmd + ' ' + program.core.remainder))


@task
def build(c):
    """Build dev version of site."""
    pelican_run(f'-s {SETTINGS_FILE} -D --verbose')

@task
def release(c):
    """Build production version of site."""
    pelican_run(f'-s {PROD_SETTINGS_FILE} --verbose')

@task
def runserver(c):
    """Automatically reload browser tab upon file modification."""
    def cached_build():
        pelican_run(
            f'-s {SETTINGS_FILE} -D '
            '-e CACHE_CONTENT=True LOAD_CONTENT_CACHE=True '
            'DELETE_OUTPUT_DIRECTORY=True'
        )

    settings = get_settings()
    path = ROOT_DIR + settings['PATH']
    theme_path = ROOT_DIR + settings['THEME']

    watched_globs = [
        SETTINGS_FILE,
        f'{theme_path}/templates/**/*.html',
    ]
    watched_globs += [
        f'{theme_path}/static/**/*{ext}' for ext in EXTENTIONS['static']
    ]
    watched_globs += [
        f'{path}/**/*{ext}' for ext in EXTENTIONS['content']
    ]
    watched_globs += [
        f'{path}/static/**/*{ext}' for ext in EXTENTIONS['static']
    ]

    server = Server()
    cached_build()

    for glob in watched_globs:
        server.watch(glob, cached_build)

    server.serve(
        host=HOST, port=PORT, root=settings['OUTPUT_PATH']
    )
