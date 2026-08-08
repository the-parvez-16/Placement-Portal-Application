from flask import jsonify
from marshmallow import ValidationError
from server.exceptions import ResourceAlreadyExistsError, InvalidCredentialsError

def register_error_handlers(app):

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return jsonify({"errors": err.messages}), 400


    @app.errorhandler(InvalidCredentialsError)
    def handle_auth_error(err):
        return jsonify({"error": str(err)}), 401


    @app.errorhandler(ResourceAlreadyExistsError)
    def handle_exists_error(err):
        return jsonify({"error": str(err)}), 409


    @app.errorhandler(IncompleteProfileError)
    def handle_incomplete_error(err):
        return jsonify({"error": str(err)}), 400

    @app.errorhandler(Exception)
    def handle_generic_error(err):
        return jsonify({"error": str(err)}), 500
