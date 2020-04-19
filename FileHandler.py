import csv


class File_handler:

    def load_from_csv(self, file_name):
        try:
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    print(line)

        except Exception as error:
            print("There is an error :" + str(error))


file = File_handler()
file.load_from_csv("/Users/gabrielbruck/Desktop/Python_mini_project/CSV/Vehicle.csv")
