import os
from User import User
from FileHandler import File_handler


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
                if remove_value == None:
                    add_value = self.file_handler.append_to_csv(employee)
                    if add_value == None:
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


carlot = Carlot("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/User.csv")
carlot.update_salary_by_name('Hen', '1500')

