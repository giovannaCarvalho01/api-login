from flask_restful import Resource
from repository.recoverPassword.recoverRepository import *
from flask import jsonify, make_response, request
from models.user.User import User
from functions.messages import *

class RecoverPassword(Resource):
    
    # recebe o e-mail via URL e caso esteja na base de dados, retorna o token para o front e envia um e-mail para o usuário.
    def get(self, email):
        
        token = get_email(email)

        if ('error' in token):
            return make_response(token, 400)
        
        return make_response(jsonify({'token': token}), 200)
    
    # Atualiza a senha do usuário, o e-mail é enviado via url e a senha via body do json
    def put(self, email):
        
        data = request.get_json()
        
        erros = []
        
        # Verifica se todas as Key's necessárias foram enviadas
        for key in User.REQUIRED_VALUES_RECOVER:
            if key not in data.keys():
                erros.append({
                    'coluna': key,
                    'message': 'Este campo é obrigatório'
                })

        if erros:
            return make_response({
                'erros': erros
            }, 400)
        
        # Para cada key no Json, caso seja igual a senha, irá enviar o put e verificar se o retorno não é None, para enviar o status de retorno
        for key, value in data.items():
            if(key == "password"):
                password = str(value)
                recover = put_password(email, password)
                if 'success' in recover:
                    return make_response(recover, 200)
                
                return make_response(recover, 400)
                
                                    