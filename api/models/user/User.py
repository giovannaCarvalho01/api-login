from models.login.Login import Login

class User(Login):
    
    REQUIRED_VALUES = ['name', 'login', 'password', 'email', 'phone', 'id_profile']
    REQUIRED_VALUES_RECOVER = ['password']
    
    def __init__(self, name, login, password, email, phone, id_profile, type_sales=None, tbl_price=[], code_sales_person=None, id=None):
        # Chama o construtor da classe pai (Login) para inicializar os atributos login e password
        super().__init__(login, password)
        self.name = name
        self.email = email
        self.phone = phone
        self.code_sales_person = code_sales_person
        self.type_sales = type_sales
        self.id_profile = id_profile
        self.tbl_price = tbl_price
        self.id = id
        
    def __str__(self):
        return f'id: {self.id} name: {self.name} login: {self.login} password: {self.password} email: {self.email} phone: {self.phone} code_sales_person: {self.code_sales_person} type_sales: {self.type_sales} id_profile: {self.id_profile} tbl_price: {self.tbl_price}'
    
    def json(self):
        return {
            'id' : self.id,
            'name': self.name,
            'login': self.login,
            'password': self.password,
            'email': self.email,
            'phone': self.phone,
            'code_sales_person' : self.code_sales_person,
            'type_sales': self.type_sales,
            'id_profile': self.id_profile,
            'tbl_price' : self.tbl_price
        }

    def __eq__(self, other):
        if isinstance(other, User):
            # comparação
            return (
                self.id == other.id and
                self.name == other.name and
                self.login == other.login and
                self.password == other.password and
                self.email == other.email and
                self.phone ==  other.phone and
                self.code_sales_person == other.code_sales_person and
                self.type_sales == other.type_sales and
                self.id_profile == other.id_profile and
                self.tbl_price == other.tbl_price
            )
        return False
    