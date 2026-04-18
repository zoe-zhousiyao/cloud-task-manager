import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done
        }


@app.route("/")
def home():
    return jsonify({"message": "Cloud Task Manager is running"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_task = Task(title=data["title"], done=False)
    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.to_dict()), 201


def seed_data():
    if Task.query.count() == 0:
        sample_tasks = [
            Task(title="Learn Docker", done=False),
            Task(title="Build cloud project", done=False)
        ]
        db.session.add_all(sample_tasks)
        db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_data()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)