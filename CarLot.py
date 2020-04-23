import os
from User import User
from FileHandler import File_handler
import csv


class Carlot:

    def __init__(self, file_name):
        self.user = User(file_name)
        self.file_handler = File_handler(file_name)

    def update_salary_by_name(self, employee_name, salary):

        employee = {}
        newpath = os.path.join("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/User.csv")
        self.file_handler.load_from_csv(newpath)
        # print(self.file_handler.data)
        for x in self.file_handler.data:
            if x["first"] == employee_name:
                employee = x
        # print(employee)
        #
        if employee:
            role = self.user.user_auth(employee["first"], employee["password"])
            # print(role)
            if role == "admin":
                employee["salary"] = str(salary)
                # print(employee['salary'])
                remove_value = self.file_handler.remove_from_csv(employee["user_id"])
                # print(employee)
                if remove_value is None:
                    add_value = self.file_handler.append_to_csv(employee)
                    if add_value is None:
                        print("updated salary of an employee")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def add_to_fleet(self, external_file):
        try:
            with open(external_file, "r") as csv_external:
                csv_reader = csv.reader(csv_external)
                external_headers = next(csv_reader)

            with open("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/Vehicle.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                internal_headers = next(csv_reader)

            if external_headers != internal_headers:
                return False

            external_data = open(external_file, "r")
            internal_data = open("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/Vehicle.csv", "r")

            if external_data != internal_data:
                with open("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/Vehicle.csv", "a") as csv_append:
                    next(external_data)
                    for row in external_data:
                        csv_append.writelines(row)
                return True

        except Exception as error:
            print(error)
            raise

    def get_fleet_size(self):
        try:
            vehicle_path = os.path.join("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/Vehicle.csv")
            self.file_handler.load_from_csv(vehicle_path)
            print("There are " + str(len(self.file_handler.data)) + " cars")
            return len(self.file_handler.data)

        except Exception as error:
            print(error)
            raise


carlot = Carlot("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/User.csv")
# carlot.update_salary_by_name('Hen', '1500')
# carlot.add_to_fleet("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/external_file.csv")
carlot.get_fleet_size()
