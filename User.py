class User:
    def __init__(self, name, email_address, drivers_license_number):
        self.name = name
        self.email = email_address
        self.license = drivers_license_number
        
    def __str__(self):
        return f"""\
            name: {self.name}
            email: {self.email}
            license: {self.license}\
            """
            
#justin = User('Justin', 'email@address.com', '1112223333')
#print(justin)