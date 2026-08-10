from marshmallow import Schema, fields, validate, EXCLUDE

class PendingCompanyDTO(Schema):
    id = fields.Int(dump_only=True)
    email = fields.String(dump_only=True)
    company_name = fields.Function(lambda obj: obj.company.name if obj.company else "N/A", dump_only=True)
    
class CompanyProfileDTO(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Int(dump_only=True)
    email = fields.String(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=4), attribute="company.name")
    location = fields.String(required=True, validate=validate.Length(min=3), attribute="company.location")
    industry = fields.String(required=True, validate=validate.Length(min=2), attribute="company.industry")
    about = fields.String(required=True, validate=validate.Length(min=10), attribute="company.about")
    hr_contact = fields.String(
        required=True, 
        validate=validate.Regexp(
            r"^[6-9]\d{9}$", 
            error="Please enter a valid 10-digit phone number."
        ),
        attribute="company.hr_contact"
    )
    website = fields.URL(required=True, attribute="company.website")

    status = fields.Function(lambda obj: obj.status.value, dump_only=True)
    role = fields.Function(lambda obj: obj.role.value, dump_only=True)


class AdminCompanyListDTO(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Function(lambda obj: obj.company.name if obj.company else "N/A", dump_only=True)
    industry = fields.Function(lambda obj: obj.company.industry if obj.company else "N/A", dump_only=True)
    location = fields.Function(lambda obj: obj.company.location if obj.company else "N/A", dump_only=True)
    status = fields.Function(lambda obj: obj.status.value, dump_only=True)
