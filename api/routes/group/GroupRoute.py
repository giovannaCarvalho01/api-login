from flask import jsonify, Blueprint, make_response, request
from flask_restful import Resource
from repository.group.groupRepository import *
from models.group.Group import *
import json

class GroupRoute(Resource):

    def get(self, id=None):
        if id is not None:
            return self.get_by_id(id)
        else:
            groups = get_all_groups()
            newGroups = []
            for group in groups:
                newGroup = Group(group_description=group['group_description'], id_profile=group['id_profile'],id=group['id']).json()
                newGroups.append(newGroup)

            response = make_response(json.dumps(newGroups), 200)
            response.headers['Content-Type'] = 'application/json'
            return response

    def get_by_id(self, id):
        try:
            group = getByIdGroup(id)
            
            if isinstance(group, Group):
                newGroup = Group(
                    id=group.id,
                    group_description=group.group_description,
                    id_profile=group.id_profile
                ).json()
                response = make_response(json.dumps(newGroup), 200)
                response.headers['Content-Type'] = 'application/json'
                return response
            
            return make_response(group, 400)
        except Exception as error:
            return make_response(jsonify({'error': str(error)}), 500)

    def post(self):
        data = request.get_json()

        erros = []

        for key in Group.REQUIRED_VALUES:
            if key not in data.keys():
                erros.append({
                    'coluna': key,
                    'message': 'Este campo é obrigatório'
                })

        if erros:
            return make_response({
                'erros': erros
            }, 400)

        group = Group(**data)

        # O método post_group retorna o objeto já com o id que foi gravado no banco
        group_id = post_group(group)

        if isinstance(group_id, Group):
            return make_response(group_id.json(), 201)
        else:
            return make_response(group_id, 400)

    def put(self, id):
        
        oldGroup = getByIdGroup(id)
        
        if isinstance(oldGroup, Group):
            data = request.get_json()
            
            for key, value in data.items():
                if key == 'id':
                    return make_response(messageError(NAO_ATUALIZA_ID), 400)
                if hasattr(oldGroup, key):
                    setattr(oldGroup, key, value)
                else:
                    return make_response(messageError(KEY_INVALIDA), 400)

            group = put_group(oldGroup)

            if isinstance(group, Group):
                
                group = Group(
                    id=oldGroup.id,
                    group_description=oldGroup.group_description,
                    id_profile=oldGroup.id_profile
                ).json()
                response = make_response(json.dumps(group), 200)
                response.headers['Content-Type'] = 'application/json' 
                return response
            else:
                return make_response(group, 400)
        else:
            return make_response(messageError(ID_GROUP_NOT_EXISTS))

    def delete(self, id):

        result = delete_group(id)

        if 'success' in result:
            
            return make_response(result, 200)
        
        else:
            return make_response(result, 404)