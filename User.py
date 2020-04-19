import csv


class File_handler:

    def __init__(self):
        self.users = []

    def load_from_csv(self, *args):
        try:
            with open(args[0]) as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    users = {
                        "id": row[0],
                        "first": row[1],
                        "last": row[2],
                        "password": row[3],
                        "position": row[4],
                        "salary": row[5],
                        "role": row[6]
                    }
                    self.users.append(users)

        except Exception as error:
            print("There is an error :" + str(error))


UserFile = File_handler()
UserFile.load_from_csv("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/User.csv")
print(UserFile.users)
