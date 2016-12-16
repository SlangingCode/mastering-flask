import os

from flask import Flask

from wfdb.models import db
from wfdb.controllers.main import main_blueprint
from wfdb.controllers.blog import blog_blueprint

app = Flask(__name__)
app.config.from_object("wfdb.config.DevConfig")

db.init_app(app)

app.register_blueprint(main_blueprint)
app.register_blueprint(blog_blueprint)

if __name__ == "__main__":
    if hasattr(os.environ, 'IP') and hasattr(os.environ, 'PORT'):
        app.run(host=os.environ['IP'], port=os.environ['PORT'])
    else:
        app.run()