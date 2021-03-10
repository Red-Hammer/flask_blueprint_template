from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
import logging
from logging.handlers import RotatingFileHandler
import os
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    bootstrap.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')

        file_handler = RotatingFileHandler('logs/app_name.log', maxBytes=10240, backupCount=50)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Your App Startup')

    return app


from app import models
