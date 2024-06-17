from flask import jsonify, Blueprint, make_response, request
from flask_restful import Resource
from repository.routine.routineRepository import *
from models.routine.Routine import Routine
import json

class RoutineRoute(Resource):

    # Caso a rota não seja com id, irá buscar todos os routines, caso tenha id, irá chamar a função dessa mesma classe que irá retornar um único routine
    def get(self, id=None):
        if id is not None:
            return self.get_by_id(id)
        else:
            routines = get_all_routines()
            newRoutines = []
            for routine in routines:
                newRoutine = Routine(routine_description=routine['routine_description'], id_group=routine['id_group'], id=routine['id']).json()
                newRoutines.append(newRoutine)

            response = make_response(json.dumps(newRoutines), 200)
            response.headers['Content-Type'] = 'application/json'
            return response

    # Busca somente um routine de acordo com o id informado 
    def get_by_id(self, id):
        try:
            routine = getByIdRoutine(id)
            
            if (isinstance(routine, Routine)):
                
                newRoutine = Routine(
                    id=routine.id,
                    routine_description=routine.routine_description,
                    id_group=routine.id_group
                ).json()
                
                response = make_response(json.dumps(newRoutine), 200)
                response.headers['Content-Type'] = 'application/json'
                return response
            
            return make_response(routine, 400)
        
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)

    # Verifica se todas as chaves obrigatórias foram enviadas no json, e salva o routine caso essas chaves sejam enviadas   
    def post(self):
        data = request.get_json()

        erros = []

        for key in Routine.REQUIRED_VALUES:
            if key not in data.keys():
                erros.append({
                    'coluna': key,
                    'message': 'Este campo é obrigatório'
                })

        if erros:
            return make_response({
                'erros': erros
            }, 400)

        routine = Routine(**data)

        routine_id = post_routine(routine)
        if isinstance(routine_id, Routine):
            # É uma instacia de Routine?
            return make_response(routine_id.json(), 201)
        else:
            return make_response(routine_id, 400)

    # Atualiza o routine de acordo com os dados enviados no body da requisição, verifica se é uma instância para tratar o código de retorno
    def put(self, id):

        oldRoutine = getByIdRoutine(id)
        
        try:
            if isinstance(oldRoutine, Routine):
                data = request.get_json()
                
                for key, value in data.items():
                    
                    if key == 'id':
                        return make_response(messageError(NAO_ATUALIZA_ID), 400)
                    
                    if hasattr(oldRoutine, key):
                        setattr(oldRoutine, key, value)
                    
                    else:
                        return make_response(messageError(KEY_INVALIDA), 400)

                routine = put_routine(oldRoutine)
                
                if isinstance(routine, Routine):

                    # É uma instacia de Routine?
                    routine = Routine(
                        id=oldRoutine.id,
                        routine_description=oldRoutine.routine_description,
                        id_group=oldRoutine.id_group
                    ).json()
                    
                    
                    response = make_response(json.dumps(routine), 200)
                    response.headers['Content-Type'] = 'application/json' 
                    return response
                else:
                    return make_response(routine, 400)
            else:
                return make_response(messageError(ID_NOT_EXISTS))
        
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)

    # Tenta deletar o routine e trata o código de retorno de acordo com a key do json
    def delete(self, id):

        result = delete_routine(id)

        if 'success' in result:
            return make_response(result, 200)
        else:
            return make_response(result, 404)