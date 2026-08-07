from server.services import register_user_service, login_user_service
from flask import Blueprint, request, jsonify
from server.dto import RegistrationDTO, LoginDTO
from marshmallow import ValidationError

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
