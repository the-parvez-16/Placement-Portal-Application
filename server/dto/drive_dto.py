from marshmallow import Schema, fields, EXCLUDE


class PendingDriveDTO(Schema):
    id = fields.Integer(dump_only=True)
    job_title = fields.String(dump_only=True)
    company_name = fields.Function(lambda obj: obj.company.name if obj.company else "Unknown", dump_only=True)


class CreateDriveDTO(Schema):
    class Meta:
        unknown = EXCLUDE
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
    status = fields.Function(lambda obj: obj.status.value if obj.status else None, dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class DriveDTO(Schema):
    id = fields.Integer(dump_only=True)
    job_title = fields.String(dump_only=True)
    company_name = fields.Function(lambda obj: obj.company.name if obj.company else "Unknown", dump_only=True)
    status = fields.Function(lambda obj: obj.status.value if obj.status else None, dump_only=True)
    salary = fields.Integer(dump_only=True)
    min_cgpa = fields.Float(dump_only=True)
    allowed_branches = fields.String(dump_only=True)
    application_deadline = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    job_description = fields.String(dump_only=True)


class SimpleAppDTO(Schema):
    id = fields.Integer()
    student = fields.Method("get_student_info")
    def get_student_info(self, obj):
        return {"name": obj.student.name if obj.student else "Unknown"}

class CompanyDriveListDTO(DriveListDTO):
    applications = fields.Nested(SimpleAppDTO, many=True, dump_only=True)
