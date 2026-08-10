from server.exceptions import ResourceNotFoundException
from flask import jsonify
from marshmallow import ValidationError
from server.exceptions import *

def register_error_handlers(app):

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return jsonify({"error": err.messages}), 400


    @app.errorhandler(IncompleteProfileException)
    def handle_incomplete_profile_exception(err):
        return jsonify({"error": str(err)}), 400


    @app.errorhandler(InvalidCredentialsException)
    def handle_invalid_credentials_exception(err):
        return jsonify({"error": str(err)}), 401


    @app.errorhandler(AccountBlockedException)
    def handle_blocked_exception(err):
        return jsonify({"error": str(err)}), 403


    @app.errorhandler(ResourceNotFoundException)
    def handle_resource_not_found_exception(err):
        return jsonify({"error": str(err)}), 404


    @app.errorhandler(ResourceAlreadyExistsException)
    def handle_resource_already_exists_exception(err):
        return jsonify({"error": str(err)}), 409


    @app.errorhandler(Exception)
    def handle_generic_exception(err):
        app.logger.error(f"Unhandled Server Error: {err}", exc_info=True)
        return jsonify({"error": str(err)}), 500
