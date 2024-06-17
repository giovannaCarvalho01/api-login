import json

# Padronização de json para retorno

# Retornos Gerais

REGISTRO_EXCLUIDO = 'Registro excluído com sucesso!'
ERRO_EXCLUSAO = 'Erro ao excluir o registro!'
ID_NOT_EXISTS = 'ID não existe!'
NAO_ATUALIZA_ID = 'Violação! Não é possível atualizar o id!'
ERRO_SEM_ALTERACAO = 'Sem alterações de dados!'
ID_EM_BRANCO ='Id em branco!'
KEY_INVALIDA = 'Key inválida!'

# Retornos de Login
LOGIN_INVALIDO = 'Login inválido!'
SENHA_INVALIDA = 'Senha inválida!'
LOGIN_AUTENTICADO = 'Usuário autenticado!'

# Retornos de User
ERRO_USUARIO_EXISTENTE = 'Usuário já existe!'
ERRO_SALVAR_USUARIO = 'Não foi possível salvar o usuário!'
ERRO_ATUALIZAR_USUARIO = 'Chaves já existentes!'
ID_PROFILE_NOT_EXISTS = 'Perfil não existe!'

# Retornos RecoverPassword
ERRO_ATUALIZAR_PASSWORD = 'Erro ao atualizar senha!'
PASSWORD_ATUALIZADO = 'Senha atualizada com sucesso!'
ERRO_TOKEN_EMAIL = 'E-mail não cadastrado!'

# Perfis
PROFILE_EXISTS = 'Perfil já existe!'
ERRO_SALVAR_PROFILE = 'Não foi possível salvar o perfil!'
PROFILE_IN_USER = 'Perfil está associado a um ou mais usuários, por favor, ajuste o cadastro para prosseguir com a exclusão!'
PROFILE_GROUP_USER = 'Perfil está associado a um ou mais grupos e usuários, por favor, ajuste os cadastros para prosseguir com a exclusão!'
PROFILE_IN_GROUP =  'Perfil está associado a um ou mais grupos, por favor, ajuste o cadastro para prosseguir com a exclusão!'

# GROUPS
GROUP_EXISTS = 'Grupo já existe!'
ERRO_SALVAR_GROUP = 'Não foi possível salvar o Grupo!'
ID_GROUP_NOT_EXISTS = 'Grupo não existe!'
EXISTS_GROUP_IN_ROUTINE = 'Esse grupo está associado a uma rotina, por favor, ajuste o cadastro para prosseguir com a exclusão!'
ID_PROFILE_NOT_EXISTS = 'ID do perfil não existe!'

#MENUS
MENU_EXISTS = 'Menu já existe!'
ERRO_SALVAR_MENU = 'Não foi possível salvar o menu!'
EXISTS_MENU_IN_ROUTINE = 'Esse menu está associado a uma rotina, por favor, ajuste o cadastro para prosseguir com a exclusão!'

#ROUTINE

ROUTINE_EXISTS = 'Rotina já existe!'
ERRO_SALVAR_ROUTINE = 'Não foi possível salvar a rotina!'

def messageError(error):
    return json.loads(f'{{"error":"{error}"}}')

def messageSuccess(success):
    return json.loads(f'{{"success":"{success}"}}')