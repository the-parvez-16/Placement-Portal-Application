from server.services.application_service import apply_for_drive
from flask import Blueprint, request, jsonify, current_app, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from server.services.student_service import *
from server.services.drive_service import *
from server.services.application_service import *
from server.models import UserRole
from server.dto import *
import os
from werkzeug.utils import secure_filename
from server.core.extensions import cache
from server.core.utils import invalidate_cache


student = Blueprint("student", __name__, url_prefix="/api/student")


@student.route("/profile", methods=["GET"])
@jwt_required()
def get_student_profile_api():
    claims = get_jwt()
    if claims.get("role") != UserRole.STUDENT.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    user_id = get_jwt_identity()
    student_user = get_student_profile(user_id)
    response_data = StudentProfileDTO().dump(student_user)
    
    return jsonify(response_data), 200
    
@student.route("/profile", methods=["PUT"])
@jwt_required()
def update_student_profile_api():
    claims = get_jwt()
    if claims.get("role") != UserRole.STUDENT.value:
        return jsonify({"message": "Unauthorized"}), 401

    user_id = get_jwt_identity()

    form_data = request.form.to_dict()
    data = {
        "student": {
            "name": form_data.get("name"),
            "branch": form_data.get("branch"),
            "cgpa": float(form_data.get("cgpa")) if form_data.get("cgpa") else None,
            "expected_graduation_year": int(form_data.get("expectedGraduationYear")) if form_data.get("expectedGraduationYear") else None,
            "skills": form_data.get("skills")
        }
    }

    file = request.files.get("resumeFile")
    if file and file.filename:
        filename = secure_filename(f"user_{user_id}_{file.filename}")
        upload_dir = os.path.join(current_app.root_path, "static", "resumes")
        os.makedirs(upload_dir, exist_ok=True)
        file.save(os.path.join(upload_dir, filename))
        data["student"]["resume_file"] = f"http://localhost:5000/static/resumes/{filename}"
    else:
        data["student"]["resume_file"] = form_data.get("resumeFile")

    updated_user = update_student_profile(user_id, data)
    response_data = StudentProfileDTO().dump(updated_user)
    
    return jsonify({
        "message": "Profile updated successfully!",
        "profile": response_data
    }), 200


@student.route("/drives", methods=["GET"])
@jwt_required()
@cache.cached(timeout=60, query_string=True)
def get_approved_drives_api():
    claims = get_jwt()
    if claims.get("role") != UserRole.STUDENT.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    query = request.args.get("q", "")
    page = request.args.get("page", 1, type=int)
    drives = get_approved_drives(page, query)
    response_data = DriveListDTO(many=True).dump(drives)
    
    return jsonify(response_data), 200


@student.route("/apply/<int:drive_id>", methods=["POST"])
@jwt_required()
def apply_drive_api(drive_id):
    claims = get_jwt()
    if claims.get("role") != UserRole.STUDENT.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    user_id = get_jwt_identity()
    application = apply_for_drive(user_id, drive_id)
    response_data = ApplicationDTO().dump(application)

    invalidate_cache("/api/student/applications")
    
    return jsonify({
        "message": "Applied successfully!",
        "application": response_data
    }), 201


@student.route("/applications", methods=["GET"])
@jwt_required()
@cache.cached(timeout=60, query_string=True)
def get_my_applications_api():
    claims = get_jwt()
    if claims.get("role") != UserRole.STUDENT.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    user_id = get_jwt_identity()
    applications = get_student_applications(user_id)
    response_data = ApplicationListDTO(many=True).dump(applications)
    
    return jsonify(response_data), 200

@student.route("/drive/<int:drive_id>", methods=["GET"])
@jwt_required()
def get_drive_api(drive_id):
    claims = get_jwt()
    if claims.get("role") != UserRole.STUDENT.value:
        return jsonify({"message": "Unauthorized"}), 401

    drive = get_drive_by_id(drive_id)
    return jsonify(DriveDTO().dump(drive)), 200


@student.route("/drive/<int:drive_id>/check-application", methods=["GET"])
@jwt_required()
def check_application_api(drive_id):
    claims = get_jwt()
    if claims.get("role") != UserRole.STUDENT.value:
        return jsonify({"message": "Unauthorized"}), 401
        
    user_id = get_jwt_identity()
    application = check_student_application(user_id, drive_id)
    
    if application:
        return jsonify({"applied": True, "status": application.status.value}), 200
    else:
        return jsonify({"applied": False}), 200


@student.route("/companies", methods=["GET"])
@jwt_required()
@cache.cached(timeout=60, query_string=True)
def get_student_companies_api():
    claims = get_jwt()
    if claims.get("role") != UserRole.STUDENT.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    from server.services.admin_service import get_admin_companies
    query = request.args.get("q", "")
    response = get_admin_companies(1, query)
    approved_companies = [c for c in response["companies"] if c["status"] == "approved"]
    
    return jsonify(approved_companies), 200


@student.route("/export", methods=["POST"])
@jwt_required()
def trigger_export_api():
    claims = get_jwt()
    if claims.get("role") != UserRole.STUDENT.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    user_id = get_jwt_identity()
    from server.repositories import StudentRepository
    student_record = StudentRepository.get_by_user_id(user_id)
    
    from server.workers.tasks import export_student_applications_task
    # .delay() is Celery method that sends it to the background instantly!
    task = export_student_applications_task.delay(student_record.id)
    
    return jsonify({"message": "Export started", "task_id": task.id}), 202

@student.route("/export-status/<task_id>", methods=["GET"])
def get_export_status(task_id):
    from server.core.extensions import celery_app
    task_result = celery_app.AsyncResult(task_id)
    
    if task_result.state == 'SUCCESS':
        return jsonify({"status": "SUCCESS", "download_url": task_result.result}), 200
    elif task_result.state == 'FAILURE':
        return jsonify({"status": "FAILURE"}), 500
    else:
        return jsonify({"status": "PENDING"}), 202


@student.route("/download/<task_id>", methods=["GET"])
def download_export_file(task_id):
    export_dir = os.path.join(current_app.root_path, 'static', 'exports')
    return send_from_directory(export_dir, f"{task_id}.csv", as_attachment=True)

