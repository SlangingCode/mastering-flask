#!/usr/bin/env python3

from os import environ

from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand
from wfdb import create_app
from wfdb.models import db

app = create_app('wfdb.config.DevConfig')

migrate = Migrate(app, db)

manager = Manager(app)

if 'IP' in environ and 'PORT' in environ:
    manager.add_command('runserver', Server(host=environ['IP'], port=environ['PORT']))

manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """

    return dict(app=app)

if __name__ == "__main__":
    manager.run()