from models.routine.Routine import Routine
from connector.ConnectorPostgres import ConnectDataBase

class RoutineData:
    
    _TABLE_NAME = 'routine'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME} ORDER BY ID'
    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME} (routine_description, id_group)' \
    f'values(%s, %s) RETURNING id'
    _SELECT_BY_ID = f'SELECT * FROM {_TABLE_NAME} WHERE id = %s'
    _UPDATE = f'UPDATE {_TABLE_NAME} SET routine_description = %s, id_group = %s WHERE id = %s'
    _DELETE = f'DELETE FROM {_TABLE_NAME} WHERE id = %s'
    _SELECT_FILTERED_POST = f'SELECT * FROM {_TABLE_NAME} WHERE routine_description = %s and id_group = %s'
    
    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    def close_connection(self):
        ConnectDataBase().close_connection()
    
    # busca todos os routines do banco e retorna uma lista com todos os jsons 
    def get_all(self):
        routines = []
        
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._SELECT_ALL)
            all_routines = cursor.fetchall()
            coluns_name = [desc[0] for desc in cursor.description]
            
            for routine in all_routines:
                data = dict(zip(coluns_name, routine))
                routine = Routine(**data)
                routines.append(routine.json())
        
            connection.commit()
            cursor.close()
            self.close_connection()
            return routines
        
        except Exception as e:
            raise e
    
    # Busca o routine pelo id e retorna o objeto
    def getById(self, id):
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._SELECT_BY_ID, (id,))
            routine = cursor.fetchone()
            
            if routine:
                coluns_name = [desc[0] for desc in cursor.description]
                data = dict(zip(coluns_name, routine))
                routine = Routine(**data)
                connection.commit()
                cursor.close()
                self.close_connection()
                return routine
            
            return None
        except Exception as e:
            raise e 

    # Salva um novo routine no banco e retorna o objeto gravado já com o ID
    def post(self, routine):
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._INSERT_INTO, (routine.routine_description, routine.id_group,))
            id = cursor.fetchone()[0]
            connection.commit()
            cursor.close()
            self.close_connection()
            routine.id = id
            return routine
        
        except Exception as e:
            raise e

    # Atualiza o routine e recupera o novo registro do banco, para devolver já com os dados atualizados.
    def update(self, routine):
        
        try:
            
            if routine.id is not None:   
                #Atualizando o registro antigo
                connection = self.database.get_connection()  
                cursor = connection.cursor()
                cursor.execute(self._UPDATE, (routine.routine_description, routine.id_group, routine.id,))
                connection.commit()
                cursor.close()
                
                # Recuperando o novo registro
                cursor = connection.cursor()
                cursor.execute(self._SELECT_BY_ID, (routine.id,))
                routineUpdate = cursor.fetchone()
                cursor.close()
                self.close_connection()
                
                if routineUpdate:
                    coluns_name = [desc[0] for desc in cursor.description]
                    data = dict(zip(coluns_name, routineUpdate))
                    routine = Routine(**data)
                    return routine
                
            else:
                return None
    
        except Exception as e:
            raise e

    # Deleta o routine pelo id
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

    def validaGroupDescription(self, routine):
        
        try:
            
            connection = self.database.get_connection()
            cursor = connection.cursor()
            cursor.execute(self._SELECT_FILTERED_POST, (routine.routine_description, routine.id_group,))
            routine = cursor.fetchone()
            
            if routine:
                coluns_name = [desc[0] for desc in cursor.description]
                data = dict(zip(coluns_name, routine))
                routine = Routine(**data)
                # connection.commit()
                cursor.close()
                self.close_connection()
                return True
            
            return False

        except Exception as e:
            raise e