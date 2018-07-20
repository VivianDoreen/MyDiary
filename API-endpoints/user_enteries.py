#Import objects from the flask model
from flask import Flask, jsonify, request
#Define your app using flask
app = Flask(__name__)

userEntries = [{'entryId': 1,
                'title':'Meeting',
                'content': 'TuesdayMeetttttttting',
                'date': '23rd July, 2018'
                },
                {'entryId': 2,
                'title':'Birthday',
                'content': 'My BD is very soon',
                'date': '21 may 2018'
                },
               {'entryId': 3,
                'title':'My Dream',
                'content': 'I had a nightmare',
                'date': '23rd July, 2018'
                }
              ]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'User_Entries_API_Implementation'})

#method to get all entries
@app.route('/entries', methods=['GET'])
def viewAllUserEntries():
    return jsonify({'userEntries' : userEntries})

#Get a particular user entry
@app.route('/entries/<int:entryId>', methods=['GET'])
def view_user_entry(entryId):
    singleEntryRetrieve = [userEntry for userEntry in userEntries if userEntry['entryId'] == entryId]
    return jsonify({'singleEntryRetrieve': singleEntryRetrieve[0]})

#A method to add a user entry
@app.route('/entries', methods=['POST'])
def addEntry():
    add_user_entry = {'entryId': request.json['entryId'],
                      'title': request.json['title'],
                      'content': request.json['content'],
                      'date': request.json['date']
                      }

    userEntries.append(add_user_entry)
    return jsonify({'userEntries': userEntries})

@app.route('/entries/<int:entryId>', methods=['PUT'])
def edit_user_entry(entryId):
    singleEntryRetrieve = [userEntry for userEntry in userEntries if userEntry['entryId'] == entryId]
    singleEntryRetrieve[0]['entryId'] = request.json['entryId']
    singleEntryRetrieve[0]['title'] = request.json['title']
    singleEntryRetrieve[0]['content'] = request.json['content']
    singleEntryRetrieve[0]['date'] = request.json['date']
    return jsonify({'singleEntryRetrieve': singleEntryRetrieve[0]})

@app.route('/entries/<int:entryId>', methods=['DELETE'])
def removeOne(entryId):
    singleEntryRetrieve = [userEntry for userEntry in userEntries if userEntry['entryId'] == entryId]
    userEntries.remove(singleEntryRetrieve[0])
    return jsonify({'userEntries': userEntries})

if __name__ == '__main__':
    #run app on port 8080 in debug mode
    app.run(debug=True, port=8080)
