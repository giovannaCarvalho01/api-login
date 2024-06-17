from flask import jsonify, make_response, request
from flask_restful import Resource
from repository.login.loginRepository import *
from models.login.Login import Login
from functions.messages import *

class LoginRoute(Resource):
    
    # TODO: Implementar JWT
    
    # Função responsável por receber o data, verificar se todos os campos obrigatórios foram enviados e tratar o retorno.
    # Mudança feita para passar o login e senha via body, pois, no Flutter não aceita passar no body via GET
    def post(self):
        data = request.get_json()
        
        erros = []
        
        for key in Login.REQUIRED_VALUES:
            if key not in data.keys():
                erros.append({
                    'coluna': key,
                    'message': 'Este campo é obrigatório'
                })

        if erros:
            return make_response({
                'erros': erros
            }, 400)
            
        try:
            login = Login(**data)
            login = getLogin(login)
            
            if 'error' in login:
                return make_response(login, 400)
            
            return make_response(login, 200)
        
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)