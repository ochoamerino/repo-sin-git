from flask import Blueprint, jsonify, make_response
from app.services.alumno_service import get_alumnos
from app.models.alumno import Alumno
from app.database import SessionLocal
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

alumno_bp = Blueprint('alumno_bp', __name__)

@alumno_bp.route('/alumnos')
def listar_alumnos():
    db = SessionLocal()
    alumnos = db.query(Alumno).all()
    db.close()
    return jsonify([
        {
            "id": a.id,
            "nombre": a.nombre,
            "apellido": a.apellido,
            "dni": a.dni,
            "email": a.email,
            "fecha_nacimiento": a.fecha_nacimiento.isoformat() if a.fecha_nacimiento else None,
            "carrera": a.carrera,
            "año_ingreso": a.año_ingreso,
        }
        for a in alumnos
    ])

@alumno_bp.route('/alumno/<int:alumno_id>/json')
def alumno_json(alumno_id):
    db = SessionLocal()
    alumno = db.query(Alumno).get(alumno_id)
    db.close()
    if not alumno:
        return jsonify({"error": "Alumno no encontrado"}), 404

    return jsonify({
        "id": alumno.id,
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "dni": alumno.dni,
        "email": alumno.email,
        "fecha_nacimiento": alumno.fecha_nacimiento.isoformat() if alumno.fecha_nacimiento else None,
        "carrera": alumno.carrera,
        "año_ingreso": alumno.año_ingreso,
    })
