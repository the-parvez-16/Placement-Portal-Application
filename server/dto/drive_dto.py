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
