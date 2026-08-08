from marshmallow import validates_schema, Schema, fields, validate, ValidationError
from server.models import UserRole

class RegistrationDTO(Schema):
    name = fields.String(required=True, validate=validate.Length(min=4, max=100))

    email = fields.Email(
        required=True,
        error_messages={
            "required": "Please provide your email address.",
            "invalid": "That doesn't look like a valid email address. Please check again!"
        }
    )

    password = fields.String(
        required=True,
        validate=[
            validate.Length(min=8, max=64, error="Password must be at least 8 characters long."),
            validate.Regexp(
                r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,64}$", 
                error="Please choose a stronger password (include uppercase, lowercase, a number, and a special character)."
            )
        ],
        error_messages={
            "required": "Don't forget to enter a password!",
        }
    )
    role = fields.Enum(
        UserRole,
        by_value=True,
        required=True,
        error_messages={
            "required": "Please select if you are registering as a Student or a Company.",
            "invalid": "Invalid role selected."
        }
    )

    confirm_password = fields.String(required=True)

    @validates_schema
    def validate_confirm_password(self, data, **kwargs):
        if data.get("password") != data.get("confirm_password"):
            raise ValidationError("Passwords do not match", field_name="confirm_password")

class LoginDTO(Schema):
    email = fields.Email(
        required=True,
        error_messages={
            "required": "Please provide your email address.",
            "invalid": "That doesn't look like a valid email address. Please check again!"
        }
    )
    
    password = fields.String(
        required=True,
        error_messages={
            "required": "Don't forget to enter a password!",
            "invalid": "Invalid password"
        }
    )
    