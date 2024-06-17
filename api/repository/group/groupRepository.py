from database.group.GroupData import *
import json
from functions.messages import *
from database.GetAllTables import GetAllTables

groupData =  GroupData()
getAllTables = GetAllTables()

def get_all_groups():

    groups = groupData.get_all_groups()
    return groups

def getByIdGroup(id):

    group = groupData.getById(id)
    if group is not None:
        return group
    return messageError(ID_NOT_EXISTS)
    
def post_group(group):

    if validaFk(table='profile', id_profile=group.id_profile) is True:
        try:
            return groupData.post(group)    
        
        except Exception as e:
            return messageError(ERRO_SALVAR_GROUP) 
    else:
        return messageError(ID_PROFILE_NOT_EXISTS)
        
def put_group(group):
    
    if validaFk(table='profile', id_profile=group.id_profile) is True:
        try:
            oldGroup = getByIdGroup(group.id)
            if (getByIdGroup(group.id) is None):
                return messageError(ID_NOT_EXISTS) 
            
            if oldGroup==group:
                print(oldGroup)
                print(group)
                return messageError(ERRO_SEM_ALTERACAO)
            else:
                return groupData.update(group)
                
        except Exception as e:
            raise e
    else:
        return messageError(ID_NOT_EXISTS)

def delete_group(id):
    
    if getAllTables.existsFK(table_name='routine', filter_type='id_group', filter_value=id) is False:
        if (getByIdGroup(id) is None):
            return messageError(ID_NOT_EXISTS)            
        try:
            
            deletedGroup = groupData.delete(id)
            
            if deletedGroup is True:
                return messageSuccess(REGISTRO_EXCLUIDO)
            
            return messageError(ERRO_EXCLUSAO)
        
        except Exception as e:
            raise e
    else:
        return messageError(EXISTS_GROUP_IN_ROUTINE)

def validaFk(table, id_profile):
    if getAllTables.existsFK(table_name=table, filter_type='id', filter_value=id_profile) is True:
        return True
    return False