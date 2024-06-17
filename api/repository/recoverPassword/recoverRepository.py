from database.user.UserData import UserData
from functions.generateToken import *
from functions.sendEmail import *
from functions.messages import *
import json

userData =  UserData()


# Geração de Token
def get_email(email):
    # Verifica se o e-mail existe, caso exista, gera um token e envia o e-mail.
    if(userData.userExists(email, 'email') is not None):
        token = generateToken()
        # Verificar se o e-mail foi enviado, caso sim, retorna o token
        if (sendEmailOutlook(token, email) is True):
            return token
        
    else:
        return messageError(ERRO_TOKEN_EMAIL)

# Recebe um e-mail e a nova senha, busca o usuário pelo e-mail, se o retorno não for None altera a senha.
def put_password(email, password):
    user = userData.userExists(email, 'email')

    if(user is not None):
        user.password = password
        
        putUser = userData.updateUser(user)
        
        if(putUser is None):
            return messageError(ERRO_ATUALIZAR_PASSWORD)
        
        return messageSuccess(PASSWORD_ATUALIZADO)
    
    return messageError(ERRO_TOKEN_EMAIL)
    
        
        

