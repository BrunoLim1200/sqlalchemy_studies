from flask import Flask, request
from flask_restful import Resource, Api
from models import People, Todo

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self, name):
        users = People.query.filter_by(name=name).first()
        try:
            response = {
                'name':users.name,
                'age':users.age,
                'id':users.id
            }
        except AttributeError:
            response = {
                'status':'error',
                'message':'dont find an user'
            }
        return response

    def put(self, name):
        user = People.query.filter_by(name=name).first()
        data = request.json
        if 'nome' in data:
            user.name = data['name']
        if 'age' in data:
            user.age = data['age']
        user.save()
        response  = {
            'id':user.id,
            'name':user.name,
            'age':user.age
        }
        return response

    def delete(self, name):
        user = People.query.filter_by(name=name).first()
        user.delete()
        return {'status':'success', 'message':'user deleted'}

class userList(Resource):
    def get(self):
        users = People.query.all()
        response = [{'id':i.id, 'name':i.name, 'age':i.age}for i in users]
        return response

    def post(self):
        data = request.json
        user = People(name=data['name'], age=data['age'])
        user.save()
        response = {
            'id':user.id,
            'name':user.name,
            'age':user.age
        }
        return response

class todoList(Resource):
    def get(self):
        tasks = Todo.query.all()
        response = [{'id':i.id, 'name':i.name, 'people':i.people.name} for i in tasks]
        return response

    def post(self):
        data = request.json
        users = People.query.filter_by(name=data['name']).first()
        todo = Todo(name=data['name'], user=users)
        todo.save()
        response = {
            'user':todo.user.name,
            'name':todo.name,
            'id':todo.id,
        }
        return response

api.add_resource(User, '/user/<string:name>/')
api.add_resource(userList, '/userlist/')
api.add_resource(todoList, '/todo/')

if __name__ == '__main__':
    app.run(debug=True)