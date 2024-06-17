from database.login.LoginData import LoginData
from functions.messages import *

loginData = LoginData()

# Função para validar se o Login é válido, caso seja, retorna uma mensagem positiva, caso contrário, 
# valida somente o Login para fazer o tratamento do retorno do erro (Se é senha ou login).
def getLogin(login):
    
    loginIsValid = loginData.get_login(login)
    
    if loginIsValid:
        return messageSuccess(LOGIN_AUTENTICADO)
    
    else:
        loginExists = loginData.validarLogin(login)
        
        if loginExists:
            return messageError(SENHA_INVALIDA)
        
        return messageError(LOGIN_INVALIDO)
        