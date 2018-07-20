#Import objects from the flask model
from flask import Flask, jsonify, request
#Define your app using flask
app = Flask(__name__)

userDetails = [{
                'userId': 1,
                'fullName':'NabuloVivianDoreen',
                'userName': 'nabulo',
                'email': 'nabulov@yahoo.com',
                'password':'viv'
                },
                {
                'userId': 2,
                'fullName':'Nabwire Cedella',
                'userName': 'cedella',
                'email': 'cedella@gmail.com',
                'password':'ced'
                },
               {
                'userId': 3,
                'fullName':'Mukuwa Goefrey',
                'userName': 'mukuwa',
                'email': 'gmukuwa@yahoo.com',
                'password':'muk'
                }
              ]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'User_API_Implementation'})

#Retrieve all users
@app.route('/users', methods=['GET'])
def viewAllUserEntries():
    return jsonify({'userEntries' : userDetails})

#Retrieve a particular user
@app.route('/users/<int:userId>', methods=['GET'])
def view_user(userId):
    singleUser = [user for user in userDetails if user['userId'] == userId]
    return jsonify({'singleUser': singleUser[0]})

#A method to add a user entry
@app.route('/users', methods=['POST'])
def addEntry():
    add_user = {'userId': request.json['userId'],
                'fullName': request.json['fullName'],
                'userName': request.json['userName'],
                'email': request.json['email'],
                'password': request.json['password']
                }

    userDetails.append(add_user)
    return jsonify({'userEntries': userDetails})

#Update a particular user
@app.route('/users/<int:userId>', methods=['PUT'])
def edit_user(userId):
    update_user = [userUpdate for userUpdate in userDetails if userUpdate['userId'] == userId]
    update_user[0]['userId'] = request.json['userId']
    update_user[0]['fullName'] = request.json['fullName']
    update_user[0]['userName'] = request.json['userName']
    update_user[0]['email'] = request.json['email']
    return jsonify({'update_user': update_user[0]})

@app.route('/users/<int:userId>', methods=['DELETE'])
def delete_user(userId):
    userDelete = [userRemove for userRemove in userDetails if userRemove['userId'] == userId]
    userDetails.remove(userDelete[0])
    return jsonify({'userDetails': userDetails})

if __name__ == '__main__':
    #run app on port 8080 in debug mode
    app.run(debug=True, port=8080)
