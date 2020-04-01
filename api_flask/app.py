from flask import Flask, abort, request, json
from flask_restful import Api, Resource, reqparse
import json
import TextClassifierFromModel
from flask_responses import json_response, xml_response, auto_response


app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class Users(Resource):
    def get(self):
        return users, 200

 #   def get(self, name):
 #       for user in users:
 #           if(name == user["name"]):
 #               return user, 200
 #       return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

api.add_resource(Users, "/users")
#api.add_resource(Users, "/users/<string:name>")

@app.route('/foo', methods=['GET', 'POST']) 
def foo():
    if not request.json:
        abort(400)
    print request.json
    return json.dumps(request.json)

#text classifier
@app.route('/api/textclassifier', methods=['GET', 'POST']) 
def textclassifier():
    #return request.data
    return TextClassifierFromModel.classify(request.data)

#entity extraction
@app.route('/api/ner', methods=['GET', 'POST']) 
def ner():
    #return request.data
    #response = app.response_class(
    #    response=json.dumps(TextClassifierFromModel.ner(request.data)),
    #    mimetype='application/json'    
    #)
#
    #return response
    result = TextClassifierFromModel.ner(request.data)
    #return result
    #return json_response({"message": "Hello World!"}, status_code=201)
    #result = '{"message": "Hello World!"}';

    return json_response(json.loads(result), status_code=201)


app.run(debug=True)