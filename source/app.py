# Create - Read - Update - Delete

from flask import Flask, request
from source.models.task import Task
app = Flask(__name__)

tasks = []


@app.route("/tasks", methods=['POST'])
def create_task():
    data = request.get_json()
    print(data)
    return 'Teste'


if __name__ == "__main__":
    app.run(debug=True)
