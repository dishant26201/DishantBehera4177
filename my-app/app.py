from flask import Flask, request, jsonify
import json
import random  
import string  

app = Flask(__name__)

def getDict(username, email, id):
    return {
        "username": username,
        "email": email,
        "id": id
    }  

userList = []
userList.append(getDict("John Mayer", "johnmayer@gmail.com", "5abf6783"))
userList.append(getDict("Rafael Nadal", "nadal@gmail.com", "5abf674563"))

def idGenerator():  
    sequence = ''.join((random.choice(string.ascii_letters) for x in range(5)))  
    sequence += ''.join((random.choice(string.digits) for x in range(5)))  
  
    listOfSquence = list(sequence)
    random.shuffle(listOfSquence)
    id = ''.join(listOfSquence)  
    return id  

@app.route("/users", methods=['GET', 'POST'])
def getMethod():
    return jsonify({'message': 'Users retrieved', 'success': 'true', 'users': userList}), 200

@app.route("/user/<id>", methods=['GET', 'POST'])
def getMethodId(id):
    flag = False
    user = {}
    for i in userList:
        if i['id'] == id:
            flag = True
            user = i

    if flag == True:
        return jsonify({'success': 'true', 'user': user}), 200
    else:
        return jsonify({'message': 'User not found', 'success': 'false'}), 400


@app.route("/update/<id>", methods=['GET', 'POST', 'PUT'])
def putMethod(id):
    input = request.get_json()
    newEmail = input['email']
    newFirstName = input['username']

    flag = False
    for i in userList:
        if i['id'] == id:
            i['username'] = newFirstName
            i['email'] = newEmail
            flag = True
    
    if flag == True:
        return jsonify({'message': 'User updated', 'success': 'true'}), 200
    else:
        return jsonify({'message': 'User not found', 'success': 'false'}), 400


@app.route("/add", methods=['GET', 'POST', 'PUT'])
def postMethod():
    input = request.get_json()
    newEmail = input['email']
    newFirstName = input['username']

    userList.append(getDict(newFirstName, newEmail, idGenerator()))

    return jsonify({'message': 'User added', 'success': 'true'}), 200


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)