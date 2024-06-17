from database.user.UserData import UserData
from functions.messages import *

userData =  UserData()

def get_all_users():
    users = userData.get_all()
    return users

def getById(id):
    user = userData.getById(id)
    
    if user is not None:
        return user
    
    return messageError(ID_NOT_EXISTS)
    
def post_user(user):
    
    try:
        # Login, name e email que não existem na base são enviados para realizar o post do usuário no banco de dados   
        if (
            userData.userExists(user.login, 'login') is None and
            userData.userExists(user.name, 'name') is None and 
            userData.userExists(user.email, 'email') is None
            ):
            if userData.getProfileById(user.id_profile) is True:
                return userData.post(user)
            
            else:
                return messageError(ID_PROFILE_NOT_EXISTS)
        else:
            return messageError(ERRO_USUARIO_EXISTENTE) 
    
    except:
        return messageError(ERRO_SALVAR_USUARIO) 
    
def put_user(user):
    try:
        oldUser = getById(user.id)
        if (user.id is None) or (getById(user.id) is None):
            return messageError(ID_EM_BRANCO) 
        
        elif (oldUser==user):
            return messageError(ERRO_SEM_ALTERACAO)
        else:
            # Login, name e email que não existem na base (retirando do filtro o usuário atual) são enviados para atualização do usuário no banco de dados   
            if (
            userData.userExistsUpdate(user.login, 'login', user.id) is None and
            userData.userExistsUpdate(user.name, 'name', user.id) is None and 
            userData.userExistsUpdate(user.email, 'email', user.id) is None
            ):
                if userData.getProfileById(user.id_profile) is True:
                    return userData.updateUser(user)
                
                else:
                    return messageError(ID_PROFILE_NOT_EXISTS)                
            
            else:
                return messageError(ERRO_ATUALIZAR_USUARIO)
            
    except Exception as e:
        raise e

def delete_user(id):
    # Se o ID informado não existe no banco, é retornada uma mensagem de erro
    if userData.getById(id) is None:
        return messageError(ID_NOT_EXISTS)
        
    try:
        
        deletedUser = userData.deleteUser(id)

        if deletedUser is True:
            return messageSuccess(REGISTRO_EXCLUIDO)
        
        return messageError(ERRO_EXCLUSAO)
    
    except Exception as e:
        raise e