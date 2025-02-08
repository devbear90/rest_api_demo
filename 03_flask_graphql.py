from flask import Flask
from strawberry.flask.views import GraphQLView
import strawberry

@strawberry.type
class Task:
    id: int
    title: str
    completed: bool

tasks = [
    Task(id=1, title="Design HLD", completed=False),
    Task(id=2, title="Implement backend", completed=False),
]

@strawberry.type
class Query:
    all_tasks: list[Task] = strawberry.field(lambda: tasks)

    @strawberry.field
    def get_task(self, id: int) -> Task | None:
        return next((task for task in tasks if task.id == id), None)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_task(self, title: str) -> Task:
        new_task = Task(id=len(tasks) + 1, title=title, completed=False)
        tasks.append(new_task)
        return new_task
    
    @strawberry.mutation
    def delete_task(self, id: int) -> Task:
        for idx, task in enumerate(tasks):
            if id == task.id:
                break
        return tasks.pop(idx)
    
    @strawberry.mutation
    def update_task(self, id: int, title: str = None, completed: bool = None) -> Task | None:
        for task in tasks:
            if task.id == id:
                if title is not None:
                    task.title = title
                if completed is not None:
                    task.completed = completed
                return task
        return None


schema = strawberry.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
app.add_url_rule(
    "/tasks_graphql", view_func=GraphQLView.as_view("tasks_graphql", schema=schema)
)

if __name__ == "__main__":
    app.run(debug=True)
