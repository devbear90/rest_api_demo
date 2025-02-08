from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Design HLD", "completed": False},
    {"id": 2, "title": "Implement backend", "completed": False}
]

def add_links_to_task(task):
    task['links'] = {
        'self': f"/tasks/{task['id']}",
        'update': f"/tasks/{task['id']}",
        'delete': f"/tasks/{task['id']}"
    }
    return task

@app.route('/tasks_restful', methods=['GET'])
def get_tasks():
    tasks_with_links = [add_links_to_task(task.copy()) for task in tasks]
    return jsonify(tasks_with_links), 200

@app.route('/tasks_restful/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task_with_links = add_links_to_task(task.copy())
        return jsonify(task_with_links), 200
    return jsonify({"message": "Task not found"}), 404

@app.route('/tasks_restful', methods=['POST'])
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
    
    new_task_with_links = add_links_to_task(new_task)
    
    return jsonify(new_task_with_links), 201


@app.route('/tasks_restful/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((task for task in tasks if task['id'] == task_id), None)
    
    if task:
        task['title'] = data.get('title', task['title'])
        task['completed'] = data.get('completed', task['completed'])
        
        # Adding links to the updated task
        task_with_links = add_links_to_task(task)
        
        return jsonify(task_with_links), 200
    
    return jsonify({"message": "Task not found"}), 404


@app.route('/tasks_restful/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((task for task in tasks if task['id'] == task_id), None)
    
    if task:
        tasks = [t for t in tasks if t['id'] != task_id]
        return jsonify({"message": "Task deleted"}), 200
    
    return jsonify({"message": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
