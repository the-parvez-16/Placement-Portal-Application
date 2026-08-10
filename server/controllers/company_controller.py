from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from server.services.company_service import update_company_profile, get_company_profile
from server.services.drive_service import create_placement_drive, get_drives_by_company
from server.services.application_service import *
from server.models import UserRole
from server.dto import CompanyProfileDTO, CreateDriveDTO, DriveListDTO, UpdateApplicationStatusDTO, ApplicationListDTO

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


@company.route("/drives", methods=["POST"])
@jwt_required()
def create_drive_api():
    claims = get_jwt()
    if claims.get("role") != UserRole.COMPANY.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    data = CreateDriveDTO().load(request.get_json())
    
    user_id = get_jwt_identity()
    new_drive = create_placement_drive(user_id, data)
    
    response_data = CreateDriveDTO().dump(new_drive)
    
    return jsonify({
        "message": "Drive created successfully!", 
        "drive": response_data
    }), 201


@company.route("/drives", methods=["GET"])
@jwt_required()
def get_drives_by_company_api():
    claims = get_jwt()
    if claims.get("role") != UserRole.COMPANY.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    user_id = get_jwt_identity()
    drives = get_drives_by_company(user_id)
    response_data = DriveListDTO(many=True).dump(drives)
    
    return jsonify(response_data), 200


@company.route("/applications/<int:drive_id>", methods=["GET"])
@jwt_required()
def get_drive_applications_api(drive_id):
    claims = get_jwt()
    if claims.get("role") != UserRole.COMPANY.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    applications = get_drive_applications(drive_id)
    response_data = ApplicationListDTO(many=True).dump(applications)
    
    return jsonify(response_data), 200


@company.route("/applications/<int:application_id>/status", methods=["PUT"])
@jwt_required()
def update_application_status_api(application_id):
    claims = get_jwt()
    if claims.get("role") != UserRole.COMPANY.value:
        return jsonify({"message": "Unauthorized"}), 401
    
    data = UpdateApplicationStatusDTO().load(request.get_json())
    updated_application = update_application_status(application_id, data.get("status"))
    response_data = UpdateApplicationStatusDTO().dump(updated_application)
    
    return jsonify({
        "message": "Application status updated successfully!",
        "application": response_data
    }), 200
    
@company.route("/applications/<int:application_id>", methods=["GET"])
@jwt_required()
def get_single_application_api(application_id):
    app = get_application_by_id(application_id)
    return jsonify(ApplicationListDTO().dump(app)), 200
