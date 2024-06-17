from models.profile.Profile import Profile
from connector.ConnectorPostgres import ConnectDataBase

class ProfileData:
    
    _TABLE_NAME = 'profile'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME} ORDER BY ID'
    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME} (profile_description)' \
    f'values(%s) RETURNING id'
    _SELECT_BY_ID = f'SELECT * FROM {_TABLE_NAME} WHERE id = %s'
    _UPDATE = f'UPDATE {_TABLE_NAME} SET profile_description = %s WHERE id = %s'
    _DELETE = f'DELETE FROM {_TABLE_NAME} WHERE id = %s'
    _SELECT_FILTERED = f'SELECT * FROM {_TABLE_NAME} WHERE %s = %%s'
    
    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    def close_connection(self):
        ConnectDataBase().close_connection()
    
    # busca todos os profiles do banco e retorna uma lista com todos os jsons 
    def get_all(self):
        profiles = []
        
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._SELECT_ALL)
            all_profiles = cursor.fetchall()
            coluns_name = [desc[0] for desc in cursor.description]
            
            for profile in all_profiles:
                data = dict(zip(coluns_name, profile))
                profile = Profile(**data)
                profiles.append(profile.json())
        
            connection.commit()
            cursor.close()
            self.close_connection()
            return profiles
        
        except Exception as e:
            raise e
    
    # Busca o profile pelo id e retorna o objeto
    def getById(self, id):
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._SELECT_BY_ID, (id,))
            profile = cursor.fetchone()
            
            if profile:
                coluns_name = [desc[0] for desc in cursor.description]
                data = dict(zip(coluns_name, profile))
                profile = Profile(**data)
                connection.commit()
                cursor.close()
                self.close_connection()
                return profile
            
            return None
        except Exception as e:
            raise e 

    # Salva um novo profile no banco e retorna o objeto gravado já com o ID
    def post(self, profile):
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._INSERT_INTO, (profile.profile_description,))
            id = cursor.fetchone()[0]
            connection.commit()
            cursor.close()
            self.close_connection()
            profile.id = id
            return profile
        except Exception as e:
            raise e

    # Atualiza o profile e recupera o novo registro do banco, para devolver já com os dados atualizados.
    def update(self, profile):
        
        try:
            
            if profile.id is not None:   
                #Atualizando o registro antigo
                connection = self.database.get_connection()  
                cursor = connection.cursor()
                cursor.execute(self._UPDATE, (profile.profile_description, profile.id,))
                connection.commit()
                cursor.close()
                
                # Recuperando o novo registro
                cursor = connection.cursor()
                cursor.execute(self._SELECT_BY_ID, (profile.id,))
                profileUpdate = cursor.fetchone()
                cursor.close()
                self.close_connection()
                
                if profileUpdate:
                    coluns_name = [desc[0] for desc in cursor.description]
                    data = dict(zip(coluns_name, profileUpdate))
                    profile = Profile(**data)
                    return profile
                
            else:
                return None
    
        except Exception as e:
            raise e

    # Deleta o profile pelo id
    def delete(self, id):
        
        try:            
            if id is not None:
                connection = self.database.get_connection()
                cursor = connection.cursor()
                cursor.execute(self._DELETE, (id,))
                connection.commit()
                cursor.close()
                return True
        
            else:
                return False
        
        except Exception as e:
            raise e

    # Verifica se um profile existe, de acordo com o tipo do filtro informado e o valor a ser filtrado, caso ache, retorna o objeto
    def profileExists(self, filter_value, filter_type):
        
        if filter_type not in {"profile_description"}:
            return "Tipo de filtro inválido"
        
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            query = self._SELECT_FILTERED % filter_type
            
            cursor.execute(query, (filter_value,))
            profile_data = cursor.fetchone()
            connection.commit()
            cursor.close()
            self.close_connection()
            
            if profile_data:
                coluns_name = [desc[0] for desc in cursor.description]
                data = dict(zip(coluns_name, profile_data))
                profile = Profile(**data)
                return profile
            
            else:
                return None
        except Exception as e:
            raise e