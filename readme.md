Task Management Web App (Python + Angular + SQLite)
📘 Project Overview

This is a simple Task Management Website built using:

Frontend: Angular

Backend: Python (Flask)

Database: SQLite

The goal is to manage daily tasks — create, update, delete, and mark them as completed — while learning DevOps concepts step by step (Docker, CI/CD, AWS, Kubernetes).

Project-Structure
📁 task-manager/
│
├── 📂 backend/                  ← Flask backend application
│   ├── app.py                   ← Main Flask app entry point
│   ├── models.py                ← Database models (Task schema)
│   ├── database.db              ← SQLite local database
│   ├── requirements.txt         ← Python dependencies
│   └── __init__.py              ← Package initializer
│
├── 📂 frontend/                 ← Angular frontend application
│   ├── src/                     ← Angular source code
│   ├── angular.json             ← Angular configuration file
│   ├── package.json             ← Node dependencies
│   └── tsconfig.json            ← TypeScript configuration
│
├── 🐳 docker-compose.yml         ← Docker Compose configuration
├── 🐍 Dockerfile                 ← Backend Dockerfile
├── 🧱 Dockerfile.frontend        ← Frontend Dockerfile
│
├── ⚙️ .github/
│   └── workflows/
│       └── ci-cd.yml            ← GitHub Actions CI/CD workflow
│
└── 📘 README.md                 ← Project documentation
