from database.profile.ProfileData import ProfileData
from database.GetAllTables import GetAllTables
import json
from functions.messages import *

profileData =  ProfileData()
getAllTables = GetAllTables()

_TABLE_USERS = 'users'
_TABLE_GROUP = 'group_profile'

def get_all_profilers():
    profilers = profileData.get_all()
    return profilers

def getByIdProfile(id):
    profile = profileData.getById(id)
    if profile is not None:
        return profile
    return messageError(ID_NOT_EXISTS)
    
def post_profile(profile):
    
    try:
        if (
            profileData.profileExists(profile.profile_description, 'profile_description') is None
            ):
            return profileData.post(profile)    
        else:
            return messageError(PROFILE_EXISTS) 
    
    except Exception as e:
        print(e)
        return messageError(ERRO_SALVAR_PROFILE) 
    
def put_profile(profile):
    try:
        oldProfile = getByIdProfile(profile.id)
        if (getByIdProfile(profile.id) is None):
            return messageError(ID_NOT_EXISTS) 
        
        elif (oldProfile==profile):
            return messageError(ERRO_SEM_ALTERACAO)
        else:
            return profileData.update(profile)
            
    except Exception as e:
        raise e
    
# id que não estão relacionados nas tabelas de usuários e grupos, serão redirecionados para exclusão
def delete_profile(id):
    
    if getByIdProfile(id) is None:
        return messageError(ID_NOT_EXISTS)
    
    result = validarFks(_TABLE_USERS, _TABLE_GROUP, id)
    
    if result is True:
        try:
            
            deletedProfile = profileData.delete(id)
            
            if deletedProfile is True:
                return messageSuccess(REGISTRO_EXCLUIDO)
            
            return messageError(ERRO_EXCLUSAO)
        
        except Exception as e:
            raise e
    
    return messageError(result)
        
        
def validarFks(TABLE_USERS, TABLE_GROUP, id):
        # Tratamento da mensagem de erro 
    if (getAllTables.existsFK(table_name=TABLE_USERS, filter_type='id_profile', filter_value=id) is True and 
        getAllTables.existsFK(table_name=TABLE_GROUP, filter_type='id_profile', filter_value=id) is True ):
        
        return PROFILE_GROUP_USER
    
    if (getAllTables.existsFK(table_name=TABLE_USERS, filter_type='id_profile', filter_value=id) is True):
        return PROFILE_IN_USER
    
    if (getAllTables.existsFK(table_name=TABLE_GROUP, filter_type='id_profile', filter_value=id) is True):
        return PROFILE_IN_GROUP
    
    return True