from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Do laundry", "completed": False}
]

@app.route('/task_manager', methods=['GET'])
def task_manager():
    action = request.args.get('action')
    
    if action == 'list':
        return jsonify(tasks), 200
    
    elif action == 'create':
        # Például paraméterben küldünk címet: ?action=create&title=NewTask
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
        # Például paraméterben adjuk át a task_id-t: ?action=delete&task_id=1
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


if __name__ == '__main__':
    app.run(debug=True)
