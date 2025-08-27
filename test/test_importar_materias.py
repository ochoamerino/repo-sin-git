from app import create_app, db
from app.models import Materia  
from scripts.import_materias import importar_materias

import os
import pytest

@pytest.fixture
def app_context():
    os.environ["FLASK_CONTEXT"] = "testing"
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

def test_importar_materias(app_context):
    ruta_archivo = "scripts/materias.xml"
    importar_materias(ruta_archivo)

    materias = Materia.query.all()
    print(f"Se importaron {len(materias)} materias.")
    assert len(materias) > 0
