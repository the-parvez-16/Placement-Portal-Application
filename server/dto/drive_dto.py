from marshmallow import Schema, fields


class PendingDriveDTO(Schema):
    id = fields.Integer(dump_only=True)
    job_title = fields.String(dump_only=True)
    company_name = fields.Function(lambda obj: obj.company.name if obj.company else "Unknown", dump_only=True)


class AdminDriveListDTO(Schema):
    id = fields.Int(dump_only=True)
    job_title = fields.String(dump_only=True)
    company_name = fields.Function(lambda obj: obj.company.name if obj.company else "N/A", dump_only=True)
    status = fields.Function(lambda obj: obj.status.value, dump_only=True)


class CreateDriveDTO(Schema):
    job_title = fields.String(required=True)
    job_description = fields.String(required=True)
    min_cgpa = fields.Float(allow_none=True)
    allowed_branches = fields.String(allow_none=True)
    salary = fields.Integer(allow_none=True)
    application_deadline = fields.DateTime(allow_none=True)


class DriveListDTO(Schema):
    id = fields.Integer(dump_only=True)
    company_name = fields.Function(lambda obj: obj.company.name if obj.company else "Unknown", dump_only=True)
    job_title = fields.String(dump_only=True)
    job_description = fields.String(dump_only=True)
    min_cgpa = fields.Float(dump_only=True)
    allowed_branches = fields.String(dump_only=True)
    salary = fields.Integer(dump_only=True)
    application_deadline = fields.DateTime(dump_only=True)
    status = fields.Function(lambda obj: obj.status.value if obj.status else None, dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    applications = fields.Method("get_apps", dump_only=True)

    def get_apps(self, obj):
        if not obj.applications: return []
        return [{"id": app.id, "student": {"name": app.student.name if app.student else "Unknown"}} for app in obj.applications]

