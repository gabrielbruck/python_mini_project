import csv


class User:

    def inputAuth(self):
        self.name = str(input("Please enter your username:"))
        self.password = str(input("Please enter your password:"))

    def user_auth(name,password):
        try:
            with open("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/User.csv", 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                access = False
                user_role = ' '

                for row in csv_reader:
                    if name.lower() == row[1] and password == row[3]:
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


User.inputAuth(User)
User.user_auth(User.name, User.password)



