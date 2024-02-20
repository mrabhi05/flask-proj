from flask import Flask, request

app = Flask(__name__)



users = {
    1: {'id': 1, 'name': 'Abhishek Nair', 'email': 'abhishekn@example.com'},
    2: {'id': 2, 'name': 'Arnold Pinto', 'email': 'arnoldp@example.com'}
}


@app.route("/users", methods=['GET'])
def get_all_users():
    return users


@app.route('/users/<int:user_id>', methods=['GET'])
def get_users(user_id):
    user = users.get(user_id)
    if user:
        return user
    else:
        return {'error': 'User not found'}
    

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = len(users) + 1
    user = {'id': user_id, 'name': data['name'], 'email': data['email']}
    users[user_id] = user

    if user:
        return {'message':'Successfully added the record',
                'data': user}
    else:
        return {'error': 'User not found'}

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_users(user_id):
    user = users.pop(user_id, None)
    if user:
        return {'message':'User Deleted Successfully'}
    else:
        return {'error':'User Not Found'}



if __name__ == "__main__":
    app.run(debug=True)

