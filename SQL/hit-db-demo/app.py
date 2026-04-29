import sys
from dbhelper import DBhelper
class Flipkart:

    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input("""
        1. Enter 1 to Register.
        2. Enter 2 to Login.
        3. Enter anything to exit.
        """)

        if user_input == '1':
            print("You selected Register")
            self.register()
        elif user_input == '2':
            print("You selected Login")
            self.login()
        else:
            print("Exiting the application...")
            sys.exit()
    def login_menu(self):
        input_user = input("""
        1. Enter 1 to see profile.
        2. Enter 2 to edit profile.
        3. Enter 3 to delete profile.
        4. Enter 4 to Logout.
        """)
    def register(self):
        name = input("Enter your Name: ")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")
        response = self.db.register(name, email, password)

        if response:
            print("Registration is successful")
        else:
            print("Registration Failed!")
    def login(self):
        email = input("Enter your Email: ")
        password = input("Enter your password: ")
        data = self.db.search(email,password)

        if len(data) == 0:
            print("Incorrect Username or Password")
            self.login()
        else:
            print("Hello ",data[0][1])
            self.login_menu()

    
obj = Flipkart()

