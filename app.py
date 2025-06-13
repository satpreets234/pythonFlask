from flask import Flask , jsonify, request
from dotenv import load_dotenv
import os
app=Flask(__name__)
load_dotenv()
users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
@app.route('/users',methods=["GET"])
def get_users():
    print(request.args)
    return jsonify(users)

@app.route('/users/getOne/<int:user_id>',methods=['GET'])
def getOneUser(user_id):
    print(os.getenv('API_URL'))
    user_id=request.view_args.get('user_id')
    present_user=any(user['id']==user_id for user in users)
    if(present_user):
        present_user=next(user for user in users if user['id']==user_id)
    if not present_user:
        return jsonify('User not present',404)
    return jsonify(present_user,200)


@app.route('/users',methods=["POST"])
def create_user():
    already_exists= any(user['name']==request.json['name'] for user in users)
    if already_exists:
        return jsonify('Name already exists',409)
    new_user=request.json
    new_user['id']=len(users)+1
    users.append(new_user)
    return jsonify(users,201)

if __name__ =='__main__':
    app.run(debug=True, port=5001)
