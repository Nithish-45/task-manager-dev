from flask import Flask, request, jsonify
from db import get_tasks, add_task

app = Flask(__name__)

@app.route("/tasks")
def tasks():
    return jsonify(get_tasks())

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    add_task(data["task"])
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)
