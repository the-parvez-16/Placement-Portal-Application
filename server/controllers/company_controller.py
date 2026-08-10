from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from server.services.company_service import update_company_profile, get_company_profile
from server.models import UserRole
from server.dto import CompanyProfileDTO

company = Blueprint("company", __name__, url_prefix="/api/company")

@company.route("/profile", methods=["GET"])
@jwt_required()
def get_company_profile_api():
    claims = get_jwt()
    if claims.get("role") != UserRole.COMPANY.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    user_id = get_jwt_identity()
    company_user = get_company_profile(user_id)
    response_data = CompanyProfileDTO().dump(company_user)
    
    return jsonify(response_data), 200
    
@company.route("/profile", methods=["PUT"])
@jwt_required()
def update_company_profile_api():
    claims = get_jwt()
    if claims.get("role") != UserRole.COMPANY.value:
        return jsonify({"message": "Unauthorized"}), 401

    data = CompanyProfileDTO().load(request.get_json())

    user_id = get_jwt_identity()
    updated_user = update_company_profile(user_id, data)

    response_data = CompanyProfileDTO().dump(updated_user)

    return jsonify({
        "message": "Profile updated successfully!", 
        "profile": response_data
    }), 200
