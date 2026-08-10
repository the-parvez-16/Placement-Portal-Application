from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from server.services.admin_service import *
from server.models import UserRole, UserStatus, DriveStatus

admin = Blueprint("admin", __name__, url_prefix="/api/admin")

@admin.route("/dashboard/stats", methods=["GET"])
@jwt_required()
def admin_dashboard_stats():
    claims = get_jwt()
    if claims.get("role") != UserRole.SUDO.value and claims.get("role") != UserRole.ADMIN.value:
        return jsonify({"message": "Unauthorized"}), 401

    response = get_admin_dashboard_stats()

    return jsonify(response), 200


@admin.route("/dashboard/pending", methods=["GET"])
@jwt_required()
def admin_dashboard_pending():
    claims = get_jwt()
    if claims.get("role") != UserRole.SUDO.value and claims.get("role") != UserRole.ADMIN.value:
        return jsonify({"message": "Unauthorized"}), 401

    search_query = request.args.get("q","")

    response = get_admin_pending_approvals(search_query)

    return jsonify(response), 200


@admin.route("/dashboard/recent", methods=["GET"])
@jwt_required()
def admin_dashboard_recent_applications():
    claims = get_jwt()
    if claims.get("role") != UserRole.SUDO.value and claims.get("role") != UserRole.ADMIN.value:
        return jsonify({"message": "Unauthorized"}), 401

    response = get_admin_recent_applications()

    return jsonify(response), 200


@admin.route("/users/<int:id>/status", methods=["PUT"])
@jwt_required()
def update_user_status_api(id):
    claims = get_jwt()
    if claims.get("role") != UserRole.SUDO.value and claims.get("role") != UserRole.ADMIN.value:
        return jsonify({"message": "Unauthorized"}), 401

    data = request.get_json()
    new_status = data.get("status")

    valid_user_statuses = [status.value for status in UserStatus]  
    if new_status not in valid_user_statuses:
        return jsonify({"error": "Invalid status value!"}), 400
    
    response = update_user_status(id, new_status)

    return jsonify(response), 200


@admin.route("/drives/<int:id>/status", methods=["PUT"])
@jwt_required()
def update_drive_status_api(id):
    claims = get_jwt()
    if claims.get("role") != UserRole.SUDO.value and claims.get("role") != UserRole.ADMIN.value:
        return jsonify({"message": "Unauthorized"}), 401

    data = request.get_json()
    new_status = data.get("status")

    valid_drive_statuses = [status.value for status in DriveStatus]
    if new_status not in valid_drive_statuses:
        return jsonify({"error": "Invalid status value!"}), 400
    
    response = update_drive_status(id, new_status)

    return jsonify(response), 200


@admin.route("/companies", methods=["GET"])
@jwt_required()
def admin_get_companies():
    claims = get_jwt()
    if claims.get("role") != UserRole.SUDO.value and claims.get("role") != UserRole.ADMIN.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    page = request.args.get("page", 1, type=int)
    query = request.args.get("q", "")
    
    response = get_admin_companies(page, query)
    
    return jsonify(response), 200


@admin.route("/students", methods=["GET"])
@jwt_required()
def admin_get_students():
    claims = get_jwt()
    if claims.get("role") != UserRole.SUDO.value and claims.get("role") != UserRole.ADMIN.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    page = request.args.get("page", 1, type=int)
    query = request.args.get("q", "")
    
    response = get_admin_students(page, query)
    
    return jsonify(response), 200


@admin.route("/drives", methods=["GET"])
@jwt_required()
def admin_get_drives():
    claims = get_jwt()
    if claims.get("role") != UserRole.SUDO.value and claims.get("role") != UserRole.ADMIN.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    page = request.args.get("page", 1, type=int)
    query = request.args.get("q", "")
    
    response = get_admin_drives(page, query)
    
    return jsonify(response), 200


@admin.route("/applications", methods=["GET"])
@jwt_required()
def admin_get_applications():
    claims = get_jwt()
    if claims.get("role") != UserRole.SUDO.value and claims.get("role") != UserRole.ADMIN.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    page = request.args.get("page", 1, type=int)
    query = request.args.get("q", "")
    
    response = get_admin_applications(page, query)
    
    return jsonify(response), 200


from server.workers.tasks import export_csv_task

@admin.route("/export-csv", methods=["POST"])
@jwt_required()
def export_csv_api():
    task = export_csv_task.delay()
    return jsonify({"message": "CSV Export started in the background!", "task_id": task.id}), 200
