from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from server.services import get_admin_dashboard_stats
from server.models import UserRole

admin = Blueprint("admin", __name__, url_prefix="/api/admin")

@admin.route("/dashboard", methods=["GET"])
@jwt_required()
def admin_dashboard():
    claims = get_jwt()
    if claims.get("role") != UserRole.SUDO.value and claims.get("role") != UserRole.ADMIN.value:
        return jsonify({"msg": "Unauthorized"}), 403

    response = get_admin_dashboard_stats()

    return jsonify(response), 201
    