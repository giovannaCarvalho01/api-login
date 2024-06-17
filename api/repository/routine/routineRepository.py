from database.routine.RoutineData import RoutineData
from database.GetAllTables import GetAllTables
import json
from functions.messages import *

routineData =  RoutineData()
getAllTables = GetAllTables()

def get_all_routines():
    routines = routineData.get_all()
    return routines

def getByIdRoutine(id):
    routine = routineData.getById(id)

    if routine is not None:
        return routine
    
    return messageError(ID_NOT_EXISTS)


def post_routine(routine):
    
    try:
        # Valida se a descrição e o id_group já existem, para não gravar duplicado, caso não exista, irá verificar se o id_group é válido, caso seja,
        # Vai cadastrar a rotina
        if routineData.validaGroupDescription(routine) is False:
            
            if (getAllTables.existsFK(table_name='group_profile', filter_type='id', filter_value=routine.id_group)):
                return routineData.post(routine)    
            
            return messageError(ID_GROUP_NOT_EXISTS)
        
        return messageError(ROUTINE_EXISTS)
    
    except Exception as e:
        return messageError(ERRO_SALVAR_ROUTINE) 

     
def put_routine(routine):
    try:
        
        oldRoutine = getByIdRoutine(routine.id)
        
        if (oldRoutine is None):
            return messageError(ID_NOT_EXISTS) 
        
        elif (oldRoutine==routine):
            return messageError(ERRO_SEM_ALTERACAO)
        else:
            
            # Valida se a descrição e o id_group já existem, para não gravar duplicado, caso não exista, irá verificar se o id_group é válido, caso seja,
            # Vai atualizar a rotina
            if (routineData.validaGroupDescription(routine) is False):
                
                if (getAllTables.existsFK(table_name='group_profile', filter_type='id', filter_value=routine.id_group)):
                    return routineData.update(routine)
                
                return messageError(ID_GROUP_NOT_EXISTS)
            
            return messageError(ROUTINE_EXISTS)
        
    except Exception as e:
        return messageError(str(e))
    
def delete_routine(id):
    
    if getByIdRoutine(id) is None:
        return messageError(ID_NOT_EXISTS)
    
    try:
        
        deletedRoutine = routineData.delete(id)
        
        if deletedRoutine is True:
            return messageSuccess(REGISTRO_EXCLUIDO)
        
        return messageError(ERRO_EXCLUSAO)
    
    except Exception as e:
        return messageError(str(e))