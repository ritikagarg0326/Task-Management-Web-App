Task Management Web App (Python + Angular + SQLite)
📘 Project Overview

This is a simple Task Management Website built using:

Frontend: Angular

Backend: Python (Flask)

Database: SQLite

The goal is to manage daily tasks — create, update, delete, and mark them as completed — while learning DevOps concepts step by step (Docker, CI/CD, AWS, Kubernetes).

Project-Structure
task-manager/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── database.db
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   └── (Angular app files)
│
├── docker-compose.yml
├── Dockerfile (for backend)
├── Dockerfile.frontend (for Angular)
├── .github/workflows/ci-cd.yml (later)
└── README.md
