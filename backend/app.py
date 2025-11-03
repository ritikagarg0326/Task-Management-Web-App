from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Task
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Database setup
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

# 🟢 Create a new task
@app.route("/tasks", methods=["POST"])
def create_task():
    session = Session()
    data = request.json
    new_task = Task(
        title=data.get("title"),
        description=data.get("description"),
        status="todo"
    )
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    session.close()
    return jsonify({"message": "Task created", "task": {"id": new_task.id, "title": new_task.title}}), 201

# 🔵 Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    session = Session()
    tasks = session.query(Task).all()
    session.close()
    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status,
            "created_at": t.created_at,
            "updated_at": t.updated_at
        } for t in tasks
    ])

# 🟡 Update a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    session = Session()
    data = request.json
    task = session.query(Task).filter(Task.id == task_id).first()

    if not task:
        session.close()
        return jsonify({"error": "Task not found"}), 404

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)
    task.updated_at = datetime.utcnow()

    session.commit()
    session.close()
    return jsonify({"message": "Task updated successfully"}), 200

# 🔴 Delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    session = Session()
    task = session.query(Task).filter(Task.id == task_id).first()

    if not task:
        session.close()
        return jsonify({"error": "Task not found"}), 404

    session.delete(task)
    session.commit()
    session.close()
    return jsonify({"message": "Task deleted successfully"}), 200

# Run app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
