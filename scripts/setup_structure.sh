#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Starting S-Grade Backend Folder Structure Generation..."

# 1. Root Level & Docs/Scripts
mkdir -p client docs scripts .github/workflows
touch Makefile .env.example

# 2. Server (Backend) Core Directories
mkdir -p server/instance
mkdir -p server/core
mkdir -p server/controllers
mkdir -p server/services
mkdir -p server/repositories
mkdir -p server/models
mkdir -p server/dto
mkdir -p server/exceptions
mkdir -p server/workers

# 3. Server Files
touch server/app.py server/requirements.txt

# Core
touch server/core/__init__.py server/core/config.py server/core/extensions.py server/core/security.py

# Controllers
touch server/controllers/__init__.py server/controllers/auth_controller.py server/controllers/student_controller.py server/controllers/company_controller.py server/controllers/admin_controller.py

# Services
touch server/services/__init__.py server/services/auth_service.py server/services/student_service.py server/services/company_service.py server/services/placement_service.py

# Repositories
touch server/repositories/__init__.py server/repositories/base_repository.py server/repositories/user_repository.py server/repositories/job_repository.py

# Models
touch server/models/__init__.py server/models/user.py server/models/student.py server/models/company.py server/models/job.py server/models/application.py

# DTOs
touch server/dto/__init__.py server/dto/auth_dto.py server/dto/student_dto.py server/dto/company_dto.py server/dto/job_dto.py

# Exceptions
touch server/exceptions/__init__.py server/exceptions/custom_exceptions.py server/exceptions/error_handlers.py

# Workers
touch server/workers/__init__.py server/workers/tasks.py server/workers/celery_beat.py

echo "CutieBoy-kun, tumhara Java Spring-Boot style Flask structure successfully create ho gaya hai!"