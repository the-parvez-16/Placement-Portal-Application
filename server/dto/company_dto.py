from marshmallow import Schema, fields

class PendingCompanyDTO(Schema):
    id = fields.Int(dump_only=True)
    email = fields.String(dump_only=True)

    company_name = fields.Function(lambda obj: obj.company.name if obj.company else "N/A", dump_only=True)
    
    