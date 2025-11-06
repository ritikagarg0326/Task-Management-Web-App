from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # ✅ Allow requests from Angular frontend

DB_NAME = "database.db"

# --- Helper functions ---
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# --- Routes ---

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return jsonify([dict(task) for task in tasks])


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data.get("title", "")
    completed = data.get("completed", False)
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tasks (title, completed) VALUES (?, ?)", (title, int(completed))
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Task added successfully!"}), 201


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.get_json()
    completed = data.get("completed", False)
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET completed = ? WHERE id = ?", (int(completed), id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task updated successfully!"})


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task deleted successfully!"})


if __name__ == "__main__":
    conn = get_db_connection()
    # ✅ Ensure tasks table exists
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()

   # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

