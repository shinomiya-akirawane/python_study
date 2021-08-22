'''
class Attempts():
    def __init__(self,login_attempts=0):
        self.login_attempts=login_attempts
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
    def print_login_attempts(self):
        print('current login attempts is: '+str(self.login_attempts))
class User():
    def __init__(self,first_name,last_name,age,address):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.address=address
        self.login_attempts=Attempts()
    def descibe_user(self):
        print('First name: '+self.first_name.title())
        print('\nLast name: '+self.last_name.title())
        print('\nAge: '+str(self.age))
        print('\nAddress: '+self.address)
    def greet_user(self):
        print('Hello, '+self.first_name.title()
              +' '+self.last_name.title())
class privileges():
    def __init__(self,*privileges):
        self.privileges=privileges
    def show_privileges(self):
        for x in self.privileges:
            print(x+'\n')
    
class Admin(User):
    def __init__(self, first_name, last_name, age, address):
        super().__init__(first_name, last_name, age, address)
        self.privileges=privileges('can add post','can delete post','can ban user')
'''