from models.login.Login import Login
from connector.ConnectorPostgres import ConnectDataBase

class  LoginData:
    
    _TABLE_NAME = 'users'
    _SELECT_LOGIN_PASSWORD = f'SELECT login, password FROM {_TABLE_NAME} WHERE login = %s and password = %s'
    _SELECT_LOGIN = f'SELECT * FROM {_TABLE_NAME} WHERE login = %s'
    
    # Quando o construtor da classe for iniciado, irá chamar a instância do connector
    def __init__(self):
        self.database = ConnectDataBase().get_instance()     

    # Função para fechar a conexão com o banco
    def close_connection(self):
        ConnectDataBase().close_connection()
    
    # Função para validar se o login e password são válidos no banco de dados
    def get_login(self, login):
        try:            
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._SELECT_LOGIN_PASSWORD, (login.login, login.password,))
            login = cursor.fetchone()
            
            if login:
                coluns_name = [desc[0] for desc in cursor.description]
                data = dict(zip(coluns_name, login))
                login = Login(**data)
                cursor.close()
                self.close_connection()
                return login
                
        except Exception as e:
            raise e
    
    # Função para validar se o Login é válido, serve para auxiliar no tratamento de erros no repository
    def validarLogin(self, login):
        try:            
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._SELECT_LOGIN, (login.login,))
            login = cursor.fetchone()
            cursor.close()
            self.close_connection()

            if login:
                return True

            return False
                
        except Exception as e:
            raise e