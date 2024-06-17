from models.user.User import User
from connector.ConnectorPostgres import ConnectDataBase

class UserData:
    
    # Variáveis privadas que armazenam as querys que serão utilizadas nas funções abaixo
    _TABLE_NAME = 'users'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME} ORDER BY ID'
    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME} (name, login, password, email, phone, code_sales_person, type_sales, id_profile, tbl_price)' \
        f'values(%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id'
    _SELECT_FILTERED = f'SELECT * FROM {_TABLE_NAME} WHERE %s = %%s'
    _SELECT_BY_ID = f'SELECT * FROM {_TABLE_NAME} WHERE id = %s'
    _UPDATE = f'UPDATE {_TABLE_NAME} SET name = %s, login = %s, password = %s, email = %s, phone = %s, code_sales_person = %s, type_sales = %s, id_profile = %s, tbl_price = %s WHERE id = %s'
    _DELETE = f'DELETE FROM {_TABLE_NAME} WHERE id = %s'
    _SELECT_FILTERED_UPDATE = 'SELECT * FROM {} WHERE {} = %s AND id <> %s'.format(_TABLE_NAME, '{}')
    _SELECT_BY_ID_PROFILE = f'SELECT * FROM profile WHERE id = %s'
 
    # Quando o construtor da classe for iniciado, irá chamar a instância do connector             
    def __init__(self):
        self.database = ConnectDataBase().get_instance()     

    # Função para fechar a conexão com o banco
    def close_connection(self):
        ConnectDataBase().close_connection()
        
    # Função para buscar todos os usuários do banco de dados, e retornar um array em formato de json, caso não tenha usuários, irá retornar um array vazio     
    def get_all(self):
        users = []

        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._SELECT_ALL)
            all_users = cursor.fetchall()
            coluns_name = [desc[0] for desc in cursor.description]      
            
            for user in all_users:
                data = dict(zip(coluns_name, user))
                user = User(**data)
                users.append(user.json())

            connection.commit()
            cursor.close()
            self.close_connection()
            return users
                
        except Exception as e:
            raise e
    
    # Função para buscar o usuário por ID, caso exista um registro, irá retornar o objeto de User, caso contrário, retorna None
    def getById(self, id):
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._SELECT_BY_ID, (id,))
            user = cursor.fetchone()
            
            if user:
                coluns_name = [desc[0] for desc in cursor.description]
                data = dict(zip(coluns_name, user))
                user = User(**data)
                connection.commit()
                cursor.close()
                self.close_connection()
                return user
            
            return None
        except Exception as e:
            raise e 
        
    # Função para salvar o User no banco de dados, após a inclusão, pegamos o ID que foi gerado, modificamos o objeto para receber esse ID e retornamos o objeto completo     
    def post(self, user):

        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._INSERT_INTO, (user.name, user.login, user.password, user.email, user.phone, user.code_sales_person, user.type_sales, user.id_profile, user.tbl_price))
            id = cursor.fetchone()[0]
            connection.commit()
            cursor.close()
            self.close_connection()
            user.id = id
            return user
        except Exception as e:
            raise e
    
    # Função que recebe dois parâmetros, o filter_type que é o tipo de filtro que será realizado na query e o valor que será buscado, caso exista alguma registro
    # irá retornar o objeto completo, caso contrário, retorna None.
    def userExists(self, filter_value, filter_type):
        
        if filter_type not in {"login", "name", "email"}:
            return "Tipo de filtro inválido"
        
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            query = self._SELECT_FILTERED % filter_type
            
            cursor.execute(query, (filter_value,))
            user_data = cursor.fetchone()
            connection.commit()
            cursor.close()
            self.close_connection()
            
            if user_data:
                coluns_name = [desc[0] for desc in cursor.description]
                data = dict(zip(coluns_name, user_data))
                user = User(**data)
                return user
            
            else:
                return None
        except Exception as e:
            raise e
        
    # Função responsável por atualizar o usuário no banco de dados, após isso, faz um novo select para buscar o objeto já atualizado e retornar. Caso o id 
    # esteja em branco, irá retornar None.        
    def updateUser(self, user):

        try:
            
            if user.id is not None:  
                connection = self.database.get_connection()          
                cursor = connection.cursor()
                cursor.execute(self._UPDATE, (user.name, user.login, user.password, user.email, user.phone, user.code_sales_person, user.type_sales, user.id_profile, user.tbl_price , user.id))
                connection.commit()
                cursor.close()
                
                
                # Recuperando o novo registro
                cursor = connection.cursor()
                cursor.execute(self._SELECT_BY_ID, (user.id,))
                userUpdate = cursor.fetchone()
                cursor.close()
                self.close_connection()
                
                if userUpdate:
                    coluns_name = [desc[0] for desc in cursor.description]
                    data = dict(zip(coluns_name, userUpdate))
                    user = User(**data)
                    return user
                
            else:
                return None
    
        except Exception as e:
            raise e
    
    # Funação para excluir um usuário no banco de dados, caso exista um User com o id informado, irá prosseguir com a exclusão e retornar True, caso contrário, False. 
    def deleteUser(self, id):
        
        try:            
            if self.getById(id) is not None:
                connection = self.database.get_connection()
                cursor = connection.cursor()
                cursor.execute(self._DELETE, (id,))
                connection.commit()
                cursor.close()
                self.close_connection()
                return True
        
            else:
                return False
        
        except Exception as e:
            raise e
        
    # Função que recebe três parâmetros, o filter_type que é o tipo de filtro que será realizado na query, o valor e id do registro atual para desconsiderar na query, 
    # caso exista algum registro irá retornar o objeto completo, caso contrário, retorna None.      
    def userExistsUpdate(self, filter_value, filter_type, id):
        if filter_type not in {"login", "name", "email"}:
            return "Tipo de filtro inválido"
        
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            query = self._SELECT_FILTERED_UPDATE.format(filter_type)
            
            cursor.execute(query, (filter_value, id,))
            user_data = cursor.fetchone()
            connection.commit()
            cursor.close()
            self.close_connection()
            
            if user_data:
                coluns_name = [desc[0] for desc in cursor.description]
                data = dict(zip(coluns_name, user_data))
                user = User(**data)
                return user
            else:
                return None
            
        except Exception as e:
            raise e    

    def getProfileById(self, id_profile):
        
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._SELECT_BY_ID_PROFILE, (id_profile,))
            profile = cursor.fetchone()
            connection.commit()
            cursor.close()
            self.close_connection()
            
            if profile:
                return True
            
            return False
        except Exception as e:
            raise e 