from os import environ

from flask import Flask

from wfdb.models import db
from wfdb.controllers.main import main_blueprint
from wfdb.controllers.blog import blog_blueprint

def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(blog_blueprint)

    return app

if __name__ == "__main__":
    app = create_app('project.config.ProdConfig')

    if 'IP' in environ and 'PORT' in environ:
        app.run(host=environ['IP'], port=environ['PORT'])
    else:
        app.run()