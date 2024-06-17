from flask import Flask
from flask_restful import Resource, Api
from routes.login.LoginRoute import LoginRoute
from routes.user.UserRoute import UserRoute
from routes.recoverPassword.RecoverPasswordRoute import *
from routes.profile.ProfileRoute import *
from routes.group.GroupRoute import *
from routes.routine.RoutineRoute import *
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)
CORS(app)

#Endpoint do Login
api.add_resource(LoginRoute, '/login')

#Endpoint User
api.add_resource(UserRoute, '/user', '/user/<int:user_id>')

# Endpoint RecoverPassword
api.add_resource(RecoverPassword, '/recoverPassword/<string:email>')

# Endpoint Profile
api.add_resource(ProfileRoute, '/profile', '/profile/<int:id>')

# Endpoint Group
api.add_resource(GroupRoute, '/group', '/group/<int:id>')

# Endpoint Routine
api.add_resource(RoutineRoute, '/routine', '/routine/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)