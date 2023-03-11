from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        print(request.form["title"])
    todo = Todo(title="First todo",desc="Start investing in stock market")
    db.session.add(todo)
    db.session.commit()
    allTodo = Todo.query.all()
    return render_template("index.html", allTodo=allTodo)
    # return "<p>Hello, World!</p>"

@app.route("/show")
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return "<p>This is products page</p>"

if __name__ == "__main__":
    app.run(debug=True,port=8000)