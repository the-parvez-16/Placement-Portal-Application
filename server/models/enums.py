from enum import Enum

class UserRole(Enum):
    SUDO = "special_power : sudo"
    ADMIN = "admin"
    COMPANY = "company"
    STUDENT = "student"

class UserStatus(Enum):
    PENDING = "pending"
    APPLIED = "applied"
    APPROVED = "approved"
    BLOCKED = "blocked"

class DriveStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    CLOSED = "closed"
    REJECTED = "rejected"

class ApplicationStatus(Enum):
    APPLIED = "applied"
    SHORTLISTED = "shortlisted"
    INTERVIEW = "interview"
    SELECTED = "selected"
    REJECTED = "rejected"
