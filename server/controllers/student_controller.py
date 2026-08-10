from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from server.services.student_service import *
from server.models import UserRole
from server.dto import StudentProfileDTO

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

    data = StudentProfileDTO().load(request.get_json())

    user_id = get_jwt_identity()
    updated_user = update_student_profile(user_id, data)

    response_data = StudentProfileDTO().dump(updated_user)

    return jsonify({
        "message": "Profile updated successfully!", 
        "profile": response_data
    }), 200
