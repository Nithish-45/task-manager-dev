from flask import Flask, request, jsonify
from flask_cors import CORS   # <--- import CORS
from db import get_tasks, add_task

app = Flask(__name__)
CORS(app)  # <--- allow cross-origin requests

@app.route("/tasks")
def tasks():
    return jsonify(get_tasks())

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    add_task(data["task"])
    return {"status": "ok"}

@app.route("/delete", methods=["POST"])
def delete():
    data = request.json
    index = data["index"]
    tasks = get_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return {"status": "deleted"}


if __name__ == "__main__":
    app.run(debug=True)
