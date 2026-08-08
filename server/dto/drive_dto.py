from marshmallow import Schema, fields

class PendingDriveDTO(Schema):
    id = fields.Integer(dump_only=True)
    job_title = fields.String(dump_only=True)
    
    company_name = fields.Function(lambda obj: obj.company.name if obj.company else "Unknown", dump_only=True)
