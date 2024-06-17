class Routine():
    
    REQUIRED_VALUES = ['routine_description', 'id_group']
    
    def __init__(self, routine_description, id_group, id=None):
        self.routine_description = routine_description
        self.id_group = id_group
        self.id = id
        
    def __str__(self):
        return f'id: {self.id} routine_description: {self.routine_description} id_group: {self.id_group}'
    
    def json(self):
        return {
            'id' : self.id,
            'routine_description': self.routine_description,
            'id_group': self.id_group
        }

    def __eq__(self, other):
        if isinstance(other, Routine):
            # comparação
            return (
                self.id == other.id and
                self.routine_description == other.routine_description and
                self.id_group == other.id_group
            )
        return False
