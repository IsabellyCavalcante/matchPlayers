import flask
from flask_api import status, exceptions

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#data stored in memory
users = {
    0: {
        "name": "Isabelly Cavalcante",
        "age": 25,
        "accepting_invitations": True,
        "own_games": ["Dead of Winter", "Sagrada", "Abyss"],
        "interest_games": ["Azul", "7 Wonders"]
    }
}

@app.route('/user', methods=['POST'])
def create_user():
    # TODO
    return "<h1>POST user lol</h1>"

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users:
        return "User with id {} doesn't exist".format(user_id), status.HTTP_404_NOT_FOUND
    return flask.jsonify(users.get(user_id))

if __name__ == '__main__':
    app.run()