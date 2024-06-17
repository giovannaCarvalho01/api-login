from models.group.Group import Group
from connector.ConnectorPostgres import ConnectDataBase

class GroupData:
    
    _TABLE_NAME = 'group_profile'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME} ORDER BY ID'
    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME} (group_description, id_profile)' \
    f'values(%s, %s) RETURNING id'
    _SELECT_BY_ID = f'SELECT * FROM {_TABLE_NAME} WHERE id = %s'
    _UPDATE = f'UPDATE {_TABLE_NAME} SET group_description = %s, id_profile = %s WHERE id = %s'
    _DELETE = f'DELETE FROM {_TABLE_NAME} WHERE id = %s'
    _SELECT_FILTERED = f'SELECT * FROM {_TABLE_NAME} WHERE %s = %%s'
    
    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    def close_connection(self):
        ConnectDataBase().close_connection()

    def get_all_groups(self):
        groups = []
        
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._SELECT_ALL)
            all_groups = cursor.fetchall()
            coluns_name = [desc[0] for desc in cursor.description]
            
            for profile in all_groups:
                data = dict(zip(coluns_name, profile))
                group = Group(**data)
                groups.append(group.json())
        
            connection.commit()
            cursor.close()
            self.close_connection()
            return groups
        
        except Exception as e:
            raise e

    
    def getById(self, id):
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._SELECT_BY_ID, (id,))
            profile = cursor.fetchone()
            
            if profile:
                coluns_name = [desc[0] for desc in cursor.description]
                data = dict(zip(coluns_name, profile))
                group = Group(**data)
                connection.commit()
                cursor.close()
                self.close_connection()
                return group
            return None
        except Exception as e:
            raise e 

    def post(self, group):
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._INSERT_INTO, (group.group_description, group.id_profile,))
            id = cursor.fetchone()[0]
            connection.commit()
            cursor.close()
            self.close_connection()
            group.id = id
            return group
        except Exception as e:
            raise e

    def update(self, group):
        try:
            
            if group.id is not None:   
                #Atualizando o registro antigo  
                connection = self.database.get_connection()
                cursor = connection.cursor()
                cursor.execute(self._UPDATE, (group.group_description, group.id_profile, group.id,))
                connection.commit()
                cursor.close()
                
                # Recuperando o novo registro
                cursor = connection.cursor()
                cursor.execute(self._SELECT_BY_ID, (group.id,))
                groupUpdate = cursor.fetchone()
                cursor.close()
                self.close_connection()
                
                if groupUpdate:
                    coluns_name = [desc[0] for desc in cursor.description]
                    data = dict(zip(coluns_name, groupUpdate))
                    group = Group(**data)
                    return group
                
            else:
                return None
    
        except:
            raise Exception('Não é possível atualizar o grupo')

    def delete(self, id):
        
        try:            
            if id is not None:
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
        