from marshmallow import Schema, fields

class PendingCompanyDTO(Schema):
    id = fields.Int(dump_only=True)
    email = fields.String(dump_only=True)

    company_name = fields.Function(lambda obj: obj.company.name if obj.company else "N/A", dump_only=True)
    
class CompanyProfileDTO(Schema):
    name = fields.Function(lambda obj: obj.company.name if obj.company else "N/A", dump_only=True)
    hr_contact = fields.Function(lambda obj: obj.company.hr_contact if obj.company else None, dump_only=True)
    website = fields.Function(lambda obj: obj.company.website if obj.company else None, dump_only=True)
    status = fields.Function(lambda obj: obj.status.value, dump_only=True)