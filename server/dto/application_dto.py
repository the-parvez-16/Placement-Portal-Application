from marshmallow import Schema, fields

class RecentApplicationDTO(Schema):
    id = fields.Int()
    studentName = fields.String(attribute="student.name")
    jobTitle = fields.String(attribute="drive.job_title")
    companyName = fields.String(attribute="drive.company.name")
    appliedAt = fields.String(attribute="created_at")

class AdminApplicationListDTO(Schema):
    id = fields.Int(dump_only=True)
    student_name = fields.Function(lambda obj: obj.student.name if obj.student else "N/A", dump_only=True)
    drive_title = fields.Function(lambda obj: obj.drive.job_title if obj.drive else "N/A", dump_only=True)
    applied_at = fields.Function(lambda obj: obj.created_at.strftime("%d-%m-%Y") if obj.created_at else "N/A", dump_only=True)
    status = fields.Function(lambda obj: obj.status.value, dump_only=True)
