from flask import jsonify, Blueprint, make_response, request
from flask_restful import Resource
from repository.profile.profileRepository import *
from models.profile.Profile import Profile
import json

class ProfileRoute(Resource):

    # Caso a rota não seja com id, irá buscar todos os profiles, caso tenha id, irá chamar a função dessa mesma classe que irá retornar um único profile
    def get(self, id=None):
        if id is not None:
            return self.get_by_id(id)
        else:
            profilers = get_all_profilers()
            newProfilers = []
            for profile in profilers:
                newProfiler = Profile(profile_description=profile['profile_description'], id=profile['id']).json()
                newProfilers.append(newProfiler)

            response = make_response(json.dumps(newProfilers), 200)
            response.headers['Content-Type'] = 'application/json'
            return response

    # Busca somente um profile de acordo com o id informado 
    def get_by_id(self, id):
        try:
            profile = getByIdProfile(id)
            if (isinstance(profile, Profile)):
                
                newProfile = Profile(
                    id=profile.id,
                    profile_description=profile.profile_description
                ).json()
                
                response = make_response(json.dumps(newProfile), 200)
                response.headers['Content-Type'] = 'application/json'
                return response
            
            return make_response(profile, 400)
        
        except Exception as error:
            return make_response(jsonify({'error': str(error)}), 500)

    # Verifica se todas as chaves obrigatórias foram enviadas no json, e salva o profile caso essas chaves sejam enviadas   
    def post(self):
        data = request.get_json()

        erros = []

        for key in Profile.REQUIRED_VALUES:
            if key not in data.keys():
                erros.append({
                    'coluna': key,
                    'message': 'Este campo é obrigatório'
                })

        if erros:
            return make_response({
                'erros': erros
            }, 400)

        profile = Profile(**data)

        profile_id = post_profile(profile)
        if isinstance(profile_id, Profile):
            # É uma instacia de Profile?
            return make_response(profile_id.json(), 201)
        else:
            return make_response(profile_id, 400)

    # Atualiza o profile de acordo com os dados enviados no body da requisição, verifica se é uma instância para tratar o código de retorno
    def put(self, id):

        oldProfile = getByIdProfile(id)
        
        if isinstance(oldProfile, Profile):
            data = request.get_json()
            
            for key, value in data.items():
                if key == 'id':
                    return make_response(messageError(NAO_ATUALIZA_ID), 400)
                if  hasattr(oldProfile, key):
                    setattr(oldProfile, key, value)
                else:
                    return make_response(messageError(KEY_INVALIDA), 400)

            profile = put_profile(oldProfile)
            
            if isinstance(profile, Profile):
                # É uma instacia de Profile?
                profile = Profile(
                    id=oldProfile.id,
                    profile_description=oldProfile.profile_description
                ).json()
                response = make_response(json.dumps(profile), 200)
                response.headers['Content-Type'] = 'application/json' 
                return response
            else:
                return make_response(profile, 400)
        else:
            return make_response(messageError(ID_PROFILE_NOT_EXISTS))

    # Tenta deletar o profile e trata o código de retorno de acordo com a key do json
    def delete(self, id):

        result = delete_profile(id)

        if 'success' in result:
            return make_response(result, 200)
        else:
            return make_response(result, 404)