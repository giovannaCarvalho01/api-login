from connector.ConnectorPostgres import ConnectDataBase

class GetAllTables:
    
    # Variáveis privadas que armazenam as querys que serão utilizadas nas funções abaixo

    _SELECT_FILTERED = 'SELECT * FROM {} WHERE {} = %s'.format('{}', '{}')
            
    def __init__(self):
        self.database = ConnectDataBase().get_instance()     

    def close_connection(self):
        ConnectDataBase().close_connection()

    # Recebe o nome da tabela, o tipo do filtro e o valor filtrado, caso exista registro, retornará True.
    def existsFK(self, table_name, filter_type, filter_value):
        
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor()
            query = self._SELECT_FILTERED.format(table_name, filter_type)
            
            cursor.execute(query, (filter_value,))
            result = cursor.fetchone()
            connection.commit()
            cursor.close()
            self.close_connection()
            
            if result:
                return True
            else:
                return False
            
        except Exception as e:
            raise e 
                
        