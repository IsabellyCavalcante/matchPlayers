from flask import Flask, abort, request, make_response, jsonify
from flask_api import status
from userRepository import UserRepository

app = Flask(__name__)
user_repository = UserRepository()


@app.route('/user', methods=['POST'])
def create_user():
    """
        Create a user in the system.
    """
    content = request.get_json(silent=True)
    if content == None:
        abort(status.HTTP_400_BAD_REQUEST,
              "No content found. The user's info must be passed.")

    user = user_repository.create_user(content)
    return jsonify(user), status.HTTP_201_CREATED


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """ 
        Returns a specific user on the system.
        If the user is not found return the 404 status code.
    """
    if not user_repository.has_user(user_id):
        abort(status.HTTP_404_NOT_FOUND,
              "User with id {} doesn't exist.".format(user_id))

    user = user_repository.get_user(user_id)
    return jsonify(user)


@app.route('/user/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    """ 
        Delete a specific user on the system.
    """
    if not user_repository.has_user(user_id):
        abort(status.HTTP_404_NOT_FOUND,
              "User with id {} doesn't exist.".format(user_id))

    user_repository.remove_user(user_id)
    return "User with id {} removed with sucess!".format(user_id)


@app.route('/users', methods=['GET'])
def get_users():
    """ 
        Returns all the users on the system.
    """
    users = user_repository.get_users()
    return jsonify(users)


@app.errorhandler(status.HTTP_404_NOT_FOUND)
def not_found(error):
    return make_response(jsonify({'error': error.get_description()}),
                         status.HTTP_404_NOT_FOUND)


@app.errorhandler(status.HTTP_400_BAD_REQUEST)
def bad_request(error):
    return make_response(jsonify({'error': error.get_description()}),
                         status.HTTP_400_BAD_REQUEST)


if __name__ == '__main__':
    app.run(debug=True)
