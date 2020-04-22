import csv
from csv import writer


class File_handler:
    data = None

    def __init__(self, file_name):
        if self.data is None:
            self.data = []
        self.load_from_csv(file_name)
        self.file_name = file_name

    def load_from_csv(self, file_name):
        try:
            self.data = []
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=',')
                for line in csv_reader:
                    self.data.append(line)

        except Exception as error:
            print("There is an error :" + str(error))

    def append_to_csv(self, data):
        try:
            for row in self.data:
                if row.get("user_id") == data[0]:
                    raise Exception("This ID already exists")

            with open(self.file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(data)

        except Exception as error:
            print("There is an error :" + str(error))

    def remove_from_csv(self, id):
        try:

            found = False
            for item in self.data:
                if item["user_id"] == id:
                    print("Found & Deleted")
                    self.data.remove(item)
                    found = True

            if found:
                keys = self.data[0].keys()
                with open(self.file_name, 'w') as f:
                    dict_writer = csv.DictWriter(f, keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(self.data)
            else:
                raise Exception("That id does not exist")

        except Exception as error:
            print("There is an error :" + str(error))

    def update_csv(self, id, row):
        try:
            found = False
            for item in self.data:
                if item["user_id"] == id:
                    print("Found & Changed")
                    self.data.remove(item)
                    found = True
            if found:
                keys = self.data[0].keys()  # grabbing the keys from teh data
                with open(self.file_name, 'w') as f:
                    dict_writer = csv.DictWriter(f, keys)  # setting the first row
                    dict_writer.writeheader()  # writing the first row
                    dict_writer.writerows(self.data)  # writing the rows
                self.append_to_csv(row)
            else:
                raise Exception("That id does not exist")

        except Exception as e:
            print(e)


# data_input = ['8', 'Ben', 'Berg', 'password', 'student', 100, 'teacher']
#
file = File_handler("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/User.csv")
# file.append_to_csv(data_input)
# file.load_from_csv("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/User.csv")
# file.remove_from_csv('15')
# file.update_csv('9', data_input)
