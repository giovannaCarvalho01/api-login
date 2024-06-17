class Profile():
    
    REQUIRED_VALUES = ['profile_description']
    
    def __init__(self, profile_description, id=None):
        self.profile_description = profile_description
        self.id = id
        
    def __str__(self):
        return f'id: {self.id} profile_description: {self.profile_description}'
    
    def json(self):
        return {
            'id' : self.id,
            'profile_description': self.profile_description
        }

    def __eq__(self, other):
        if isinstance(other, Profile):
            # comparação
            return (
                self.id == other.id and
                self.profile_description == other.profile_description
            )
        return False
