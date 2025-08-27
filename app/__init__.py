import os
from dotenv import load_dotenv
from pathlib import Path
basedir = Path(__file__).parent.parent
basedir = Path(__file__).parent.parent

from flask import Flask
from app.db import db
from app.config.config import factory


def create_app():
    app = Flask(__name__)
    context = os.getenv('FLASK_CONTEXT', 'development')
    from app.config.config import factory
    app.config.from_object(factory(context))
    
    


    db.init_app(app)


    from app.routes.materia_routes import materia_bp
    app.register_blueprint(materia_bp)

    from app.routes.alumno_routes import alumno_bp
    app.register_blueprint(alumno_bp)

    from app.cli import register_cli
    register_cli(app)

    return app
