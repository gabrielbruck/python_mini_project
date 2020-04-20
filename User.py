import csv
from FileHandler import File_handler


class User:

    def __init__(self):
        self.handler = File_handler
        # self.name = str(input("Please enter your username:"))
        # self.password = str(input("Please enter your password:"))

    def user_auth(self, name, password):
        try:
            self.handler.load_from_csv(self.handler, '/Users/gabrielbruck/Desktop/Python_mini_project/CSV/User.csv')
            print(self.handler.list)

            access = False
            user_role = ' '

            for row in self.handler.list:
                if name == row[1] and password == row[3]:
                    access = True
                    user_role = str(row[6])

                if access:
                    print('Access Granted')
                    print(f'Your role is {user_role}')
                    return access

                else:
                    print('Access Denied')
                    return access

        except Exception as error:
            print("There is an error :" + str(error))


User.__init__(User)
User.user_auth(User, 'Amir', '12345678')
