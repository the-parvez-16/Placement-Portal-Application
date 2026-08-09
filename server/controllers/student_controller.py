from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from server.services import *
from server.models import UserRole

student = Blueprint("student", __name__, url_prefix="/api/student")

