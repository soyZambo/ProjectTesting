from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.users_controller import Basequery
from controller.follows import Fquery
from controller.block import Blockquery


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# USERS------------------------------------------------------------------------
@app.route('/Piti-Cloud/users', methods=['GET', 'POST'])
def handlerUsers():
    if request.method == 'POST':
        return Basequery().addNewUser(request.json)
    else:
        return Basequery().getAllUsers()


@app.route('/Piti-Cloud/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def handleUserById(user_id):
    if request.method == 'GET':
        return Basequery().getUserById(user_id)
    elif request.method == 'PUT':
        return Basequery().updateUsers(request.json)
    elif request.method == 'DELETE':
        return Basequery().deleteUser(user_id)
    else:
        return jsonify(Error="Method Not Allowed")


# FOLLOWS----------------------------------------------------------------------

@app.route('/Piti-Cloud/follow/<int:following_user_id>', methods=['POST'])
def handlerFollow(following_user_id):
    if request.method == 'POST':
        return Fquery().getFollowUser(following_user_id, request.json)
    else:
        return jsonify(Error='Method Not allowed')


@app.route('/Piti-Cloud/followedby/<int:following_user_id>', methods=['GET'])
def handleFollowById(following_user_id):
    if request.method == 'GET':
        return Fquery().getFollowersby(following_user_id)
    else:
        return jsonify(Error='Method Not Allowed for followed by')

@app.route('/Piti-Cloud/follows/<int:followed_user_id>', methods=['GET'])
def handleFollows(followed_user_id):
    if request.method == 'GET':
        return Fquery().getFollows(followed_user_id)
    else:
        return jsonify(Error='Method Not Allowed for followed by')


@app.route('/Piti-Cloud/unfollow/<int:following_user_id>', methods=['POST'])
def handleunFollow(following_user_id):
    if request.method == 'POST':
        return Fquery().getunFollow(following_user_id, request.json)
    else:
        return jsonify(Error='Method Not Allowed for followed by')

#Block Use---------------------------------------------------------------------


@app.route('/Piti-Cloud/unblock/<int:user_id>', methods=['POST'])
def handleUnblock(user_id):
    if request.method == 'POST':
        return Blockquery().getunBlock(user_id, request.json)
    else:
        return jsonify(Error='Method Not Allowed for followed by')

#ALL BLocks
@app.route('/Piti-Cloud/block/<int:blocked_user_id>', methods=['POST'])
def handleBlockB(blocked_user_id):
    if request.method == 'POST':
        return Blockquery().blockUser(blocked_user_id, request.json)
    else:
        return jsonify(Error="Method Not Allowed")

@app.route('/Piti-Cloud/blockedby/<int:user_id>', methods=['GET'])
def handleBlockById(user_id):
    if request.method == 'GET':
        return Blockquery().blockedBy(user_id)
    else:
        return jsonify(Error="Method Not Allowed")

@app.route('/Piti-Cloud/blocking/<int:blocked_user_id>', methods=['GET'])
def handleBlocking(blocked_user_id):
    if request.method == 'GET':
        return Blockquery().blockingUser(blocked_user_id)
    else:
        return jsonify(Error="Method Not Allowed")


if __name__ == '__main__':
    app.run()
