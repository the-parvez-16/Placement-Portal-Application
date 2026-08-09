from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from server.services import get_admin_dashboard_stats, get_admin_pending_approvals
from server.models import UserRole

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

    response = get_admin_pending_approvals()

    return jsonify(response), 200