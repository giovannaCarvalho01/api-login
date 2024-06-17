class Group():
    
    REQUIRED_VALUES = ['group_description', 'id_profile']
    
    def __init__(self, group_description, id_profile, id=None):
        self.group_description = group_description
        self.id_profile = id_profile
        self.id = id
        
    def __str__(self):
        return f'id: {self.id} group_description: {self.group_description} id_profile: {self.id_profile}'
    
    def json(self):
        return {
            'id' : self.id,
            'group_description': self.group_description,
            'id_profile': self.id_profile
        }

    def __eq__(self, other):
        if isinstance(other, Group):
            # comparação
            return (
                self.id == other.id and
                self.group_description == other.group_description and
                self.id_profile == other.id_profile
            )
        return False
