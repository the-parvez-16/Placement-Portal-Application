from server.services.auth_service import *
from flask import Blueprint, request, jsonify
from server.dto import RegistrationDTO, LoginDTO
from flask_jwt_extended import jwt_required, get_jwt_identity

auth = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    validated_data = RegistrationDTO().load(data)

    response = register_user_service(validated_data)

    return jsonify(response), 201


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    validated_data = LoginDTO().load(data)

    response = login_user_service(validated_data)

    return jsonify(response), 201

@auth.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()

    response = refresh_user_service(user_id)

    return jsonify(response), 201
    
@auth.route("/users/<int:id>", methods=["GET"])
@jwt_required()
def get_user_details(id):
    response = get_user_details_service(id)

    return jsonify(response), 200
    