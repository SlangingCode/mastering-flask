#!/usr/bin/env python

import os 

from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand
from app import app

manager = Manager(app)

if hasattr(os.environ, 'IP') and hasattr(os.environ, 'PORT'):
    manager.add_command("runserver", Server(host=os.environ['IP'], port=os.environ['PORT']))

manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """

    return dict(app=app)

if __name__ == "__main__":
    manager.run()