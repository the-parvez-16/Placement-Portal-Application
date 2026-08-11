from marshmallow import Schema, fields

class RecentApplicationDTO(Schema):
    id = fields.Int()
    studentName = fields.String(attribute="student.name")
    jobTitle = fields.String(attribute="drive.job_title")
    companyName = fields.String(attribute="drive.company.name")
    appliedAt = fields.String(attribute="created_at")


class ApplicationListDTO(Schema):
    id = fields.Int(dump_only=True)
    student_name = fields.String(attribute="student.name", dump_only=True)
    company_name = fields.String(attribute="drive.company.name", dump_only=True)
    drive_title = fields.String(attribute="drive.job_title", dump_only=True)
    status = fields.Function(lambda obj: obj.status.value, dump_only=True)
    applied_at = fields.DateTime(attribute="created_at", dump_only=True)
    
class ApplicationReviewDTO(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Function(lambda obj: obj.status.value, dump_only=True)
    applied_at = fields.DateTime(attribute="created_at", dump_only=True)
    
    drive = fields.Method("get_drive_info", dump_only=True)
    def get_drive_info(self, obj):
        if not obj.drive: return None
        return {
            "id": obj.drive.id,
            "job_title": obj.drive.job_title,
            "company": {"name": obj.drive.company.name if obj.drive.company else "Unknown"}
        }

    student = fields.Method("get_student_info", dump_only=True)
    def get_student_info(self, obj):
        if not obj.student: return None
        return {
            "name": obj.student.name,
            "email": obj.student.user.email if obj.student.user else "N/A",
            "branch": obj.student.branch,
            "cgpa": obj.student.cgpa,
            "graduation_year": obj.student.expected_graduation_year,
            "skills": obj.student.skills,
            "resume_file": obj.student.resume_file
        }


class UpdateApplicationStatusDTO(Schema):
    status = fields.String(required=True)


class ApplicationDTO(Schema):
    id = fields.Int(dump_only=True)
    drive_id = fields.Int(dump_only=True)
    student_id = fields.Int(dump_only=True)
    status = fields.Function(lambda obj: obj.status.value, dump_only=True)
