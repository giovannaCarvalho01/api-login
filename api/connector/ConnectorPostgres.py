import psycopg2
import dotenv
import os

class ConnectDataBase:
    
    # Para pegar as variveis do arquivo .env
    dotenv.load_dotenv()
    
    # Armazenará uma única instância da classe ConnectDataBase
    _instance = None
    

    # Quando você cria uma instância da classe ConnectDataBase, ela estabelece uma conexão com o banco de dados usando 
    # as credenciais fornecidas no método psycopg2.connect.
    def __init__(self):
        self._connect = psycopg2.connect(
            host= os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
    
    # Este método retorna a instância única da classe ConnectDataBase. Se a instância ainda não existir, ela cria uma nova chamando o construtor.
    def get_instance(self):
        if not ConnectDataBase._instance:
            ConnectDataBase._instance = self
        return ConnectDataBase._instance
    
    # Este método retorna a conexão ativa com o banco de dados.
    def get_connection(self):
        return self._connect

    # Esse método fecha a conexão com o banco de dados. Ele verifica se a conexão existe, caso sim, fecha e define como None.
    def close_connection(self):
        if hasattr(self, "_connect") and self._connect:
            self._connect.close()
            self._connect = None