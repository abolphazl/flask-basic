from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(SECRET_KEY="dev")

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

    db.init_app(app)

    migrate.init_app(app, db)

    from project_name import models

    # ensure the instance dir exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # apply the blueprints to the app
    from project_name.apps import test, root 
    app.register_blueprint(test.bp)
    app.register_blueprint(root.bp)

    return app
