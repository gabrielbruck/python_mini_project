import csv
from FileHandler import File_handler


class User:

    def __init__(self,file_name):
        self.handler = File_handler(file_name)

    def user_auth(self, name, password):
        try:

            res ={}
            self.handler.load_from_csv('/Users/gabrielbruck/Desktop/Python_mini_project/CSV/User.csv')
            access = False
            user_role = ' '

            for row in self.handler.data:
                res.update(row)
                if name == row['first'] and password == row['password']:
                    access = True
                    user_role = str(row['role'])

                    if access:
                        print('Access Granted')
                        print(f'Your role is {user_role}')
                        return user_role

                    else:
                        print('Access Denied')
                        return access

        except Exception as error:
            print("There is an error :" + str(error))


User.__init__(User,'/Users/gabrielbruck/Desktop/Python_mini_project/CSV/User.csv')
# User.user_auth(User, 'Hen', 'password')
