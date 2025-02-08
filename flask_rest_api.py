from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Do laundry", "completed": False}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task), 200
    return jsonify({"message": "Task not found"}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_id = max(task['id'] for task in tasks) + 1 if tasks else 1
    new_task = {
        "id": new_id,
        "title": data['title'],
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['completed'] = data.get('completed', task['completed'])
            return jsonify(task), 200
    return jsonify({"message": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    for task in tasks:
        if task['id'] == task_id:
            tasks = [t for t in tasks if t['id'] != task_id]
            return jsonify({"message": "Task deleted"}), 200
    return jsonify({"message": "Task not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
