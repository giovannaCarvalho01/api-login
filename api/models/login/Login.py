class Login:
    
    # Array usado no route para validar se todos os campos obrigatórios no json foram enviados
    REQUIRED_VALUES = ['login', 'password']
    
    # Construtor da classe
    def __init__(self, login, password):
        self.login = login
        self.password = password
    
    # Função para retornar os dados em string    
    def __str__(self):
        return f'login: {self.login} password: {self.password}'
    
    # Função para converter os dados me json   
    def json(self):
        return {
            'login': self.login,
            'password': self.password
        }

    # Função para validar se é uma instância de Login
    def __eq__(self, other):
        if isinstance(other, Login):
            # comparação
            return (
                self.login == other.login and
                self.password == other.password
            )
        return False