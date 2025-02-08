from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Design HLD", "completed": False},
    {"id": 2, "title": "Implement backend", "completed": False}
]

@app.route('/task_manager', methods=['GET'])
def task_manager():
    action = request.args.get('action')
    
    if action == 'list':
        return jsonify(tasks), 200
    
    elif action == 'create':
        # Példa: ?action=create&title=NewTask
        title = request.args.get('title', 'Unnamed Task')
        new_id = max(task['id'] for task in tasks) + 1 if tasks else 1
        new_task = {
            "id": new_id,
            "title": title,
            "completed": False
        }
        tasks.append(new_task)
        return jsonify(new_task), 200
    
    elif action == 'delete':
        # Példa: ?action=delete&task_id=1
        task_id = request.args.get('task_id', None)
        if not task_id:
            return jsonify({"error": "No task_id provided"}), 400
        task_id = int(task_id)
        
        for task in tasks:
            if task['id'] == task_id:
                tasks.remove(task)
                return jsonify({"message": "Task deleted"}), 200
        
        return jsonify({"error": "Task not found"}), 404
    
    else:
        return jsonify({"error": "Unknown action"}), 400


@app.route('/task_manager_method', methods=["GET", "POST", "DELETE"])
def task_manager_with_method():
    method = request.method

    if method == "GET":
        return jsonify(tasks), 200
    
    elif method == "POST":
        data = request.get_json()
        new_id = max(task['id'] for task in tasks) + 1 if tasks else 1
        new_task = {
            "id": new_id,
            "title": data['title'],
            "completed": False
        }
        tasks.append(new_task)
        return jsonify(new_task), 200
    
    elif method == "DELETE":
        data = request.get_json()
        task_id = int(data['task_id'])

        if not task_id:
            return jsonify({"error": "No task_id provided"}), 400        
        
        for task in tasks:
            if task['id'] == task_id:
                tasks.remove(task)
                return jsonify({"message": "Task deleted"}), 200
        
        return jsonify({"error": "Task not found"}), 404

    else:
        return jsonify({"error": f"Method not allowed - {method}"}), 400


@app.route('/get_tasks', methods=["GET"])
def get_tasks():
    method = request.method

    if method != 'GET':
        return jsonify({"error": f"Method not allowed - {method}"}), 400

    return jsonify(tasks), 200

@app.route('/create_task', methods=["POST"])
def create_task():
    method = request.method
    data = request.get_json()

    if method != 'POST':
        return jsonify({"error": f"Method not allowed - {method}"}), 400
    
    new_id = max(task['id'] for task in tasks) + 1 if tasks else 1
    new_task = {
        "id": new_id,
        "title": data['title'],
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 200

@app.route('/delete_task', methods=["DELETE"])
def delete_task():
    method = request.method
    data = request.get_json()

    if method != 'DELETE':
        return jsonify({"error": f"Method not allowed - {method}"}), 400
    
    task_id = int(data['task_id'])

    if not task_id:
        return jsonify({"error": "No task_id provided"}), 400        
    
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"}), 200
    
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
