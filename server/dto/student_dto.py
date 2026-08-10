from marshmallow import Schema, fields, validate, EXCLUDE

class StudentProfileDTO(Schema):
    class Meta:
        unknown = EXCLUDE
    
    id = fields.Int(dump_only=True)
    email = fields.String(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=4), attribute="student.name")
    branch = fields.String(required=True, validate=validate.Length(min=2), attribute="student.branch")
    cgpa = fields.Float(required=True, validate=validate.Range(min=0, max=10), attribute="student.cgpa")
    skills = fields.String(required=True, validate=validate.Length(min=1), attribute="student.skills")
    expectedGraduationYear = fields.Int(required=True, validate=validate.Range(min=2020, max=2030), attribute="student.expected_graduation_year")
    resumeFile = fields.String(required=True, validate=validate.Length(min=1), attribute="student.resume_file")
    status = fields.Function(lambda obj: obj.status.value, dump_only=True)
    role = fields.Function(lambda obj: obj.role.value, dump_only=True)


class AdminStudentListDTO(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Function(lambda obj: obj.student.name if obj.student else "N/A", dump_only=True)
    branch = fields.Function(lambda obj: obj.student.branch if obj.student else "N/A", dump_only=True)
    cgpa = fields.Function(lambda obj: obj.student.cgpa if obj.student else "N/A", dump_only=True)
    status = fields.Function(lambda obj: obj.status.value, dump_only=True)
