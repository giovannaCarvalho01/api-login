from flask import jsonify, make_response, request
from flask_restful import Resource
from repository.user.userRepository import *
from models.user.User import User
import json
from functions.messages import *

class UserRoute(Resource):
    
    # Função responsável por buscar todos os usuários e retornar um array com todos, caso no endpoint tenha o id preenchido, chama a função get_by_id 
    def get(self, user_id=None):
        if user_id is not None:
            return self.get_by_id(user_id)
        else:
            users = get_all_users()
            newUsers = []
            for user in users:
                newUser = User(
                    name=user['name'], 
                    login=user['login'], 
                    password=user['password'], 
                    email=user['email'], 
                    phone=user['phone'], 
                    code_sales_person=user['code_sales_person'], 
                    id_profile=user['id_profile'], 
                    type_sales=user['type_sales'], 
                    tbl_price=user['tbl_price'], 
                    id=user['id']
                ).json()
                newUsers.append(newUser)
            
            response = make_response(json.dumps(newUsers), 200)
            response.headers['Content-Type'] = 'application/json'
            return response

    # Função responsável por buscar o usuário por id e retornar o objeto
    def get_by_id(self, user_id):
        try:
            user = getById(user_id)
            if isinstance(user, User):
                newUser = User(
                    name=user.name,
                    login=user.login,
                    password=user.password,
                    email=user.email,
                    phone=user.phone,
                    code_sales_person=user.code_sales_person,
                    id_profile=user.id_profile,
                    type_sales=user.type_sales,
                    tbl_price=user.tbl_price,
                    id=user.id
                ).json()
                response = make_response(json.dumps(newUser), 200)
                response.headers['Content-Type'] = 'application/json'        
                return response
            else:
                return make_response(user, 400)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
        
    # Função responsável por receber o data, verificar se todos os campos obrigatórios foram enviados e tratar o retorno.
    def post(self):
        data = request.get_json()
        
        erros = []
        
        for key in User.REQUIRED_VALUES:
            if key not in data.keys():
                erros.append({
                    'coluna': key,
                    'message': 'Este campo é obrigatório'
                })

        if erros:
            return make_response({
                'erros': erros
            }, 400)
            
        user = User(**data)
        
        user_id = post_user(user)
        
        if isinstance(user_id, User):
            # É uma instacia de User?
            response = make_response(json.dumps(user_id.json()), 201)
            response.headers['Content-Type'] = 'application/json'
            return response
        else:
            return make_response(user_id, 400)

    # Função responsável por verificar quais keys foram enviadas no json, realizar a atualização no banco de dados e tratar o retorno
    def put(self, user_id):
        try:
            # OldUser
            userExists = getById(user_id)
            
            if isinstance(userExists, User):
                data = request.get_json()
                
                for key, value in data.items():
                    # Verifica se a chave existe nos atributos do objeto User, caso exista, seta o novo valor para o atributo de usuário
                    if key == 'id':
                        return make_response(jsonify({'error': NAO_ATUALIZA_ID}), 400) 
                    if hasattr(userExists, key):
                        setattr(userExists, key, value)
                    else:
                        # TODO: RETORNAR UMA MENSAGEM
                        print(f"Atributo '{key}' não existe para o usuário.")
                
                # Atualiza o usuário no banco de dados
                updateUser = put_user(userExists)
                
                if isinstance(updateUser, User):
                    # É uma instacia de User?
                    updateUser = User(
                    name=updateUser.name,
                    login=updateUser.login,
                    password=updateUser.password,
                    email=updateUser.email,
                    phone=updateUser.phone,
                    code_sales_person=updateUser.code_sales_person,
                    id_profile=updateUser.id_profile,
                    type_sales=updateUser.type_sales,
                    tbl_price=updateUser.tbl_price,
                    id=updateUser.id
                    ).json()
                    response = make_response(json.dumps(updateUser), 200)
                    response.headers['Content-Type'] = 'application/json' 
                    return response
                else:
                    return make_response(updateUser, 400)
            else:
                return make_response(userExists, 400)
            
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)

    # Função responsável por tratar o retorno da exclusão do usuário
    def delete(self, user_id):

        result = delete_user(user_id)


        if 'success' in result:
            return make_response(result, 200)
        else:
            return make_response(result, 404)
        