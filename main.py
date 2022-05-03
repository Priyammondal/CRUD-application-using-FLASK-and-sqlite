import flask
from flask import *

app = Flask(__name__)


details = [
    {
        # "id": id,
        "name": "Mukherjee",
        "age": 24,
        "designation": "mathematician"},
    {
        # "id": id,
        "name": "Priyam Mondal",
        "age": 23,
        "designation": "software engineer"},
    {
        # "id": id,
        "name": "Niloy Das",
        "age": 23,
        "designation": "software developer"}
]


@app.route("/")
def index():
    return ("Hey there, Welcome to the api learning course")


@app.route("/details", methods=['GET'])
def get():
    return jsonify({"details": details})


@app.route("/details/<int:id>", methods=["GET"])
def get_details(id):
    return jsonify({"details": details[id]})


@app.route("/create", methods=["POST"])
def create_data():
    add = {"name": "Ratul Debnath",
           "age": 25,
           "designation": "mechanical engineer"}
    details.append(add)


if __name__ == "__main__":
    app.run(debug=True)
