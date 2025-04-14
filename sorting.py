import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = {}
        for row in csv_reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))

    return data

def selection_sort(seznam, direction = "ascending"):
    if direction == "ascending":
        seznam.sort()
        return seznam
    elif direction == "descending":
        seznam.sort()
        seznam.reverse()
        return seznam
    else:
        return print("Invalid direction")

def main():
    data = read_data("numbers.csv")
    print(data)
    print(selection_sort([88, 36, 21, 54, 99, 1, 81, 18, 21, 36, 61], "descending"))
    pass


if __name__ == '__main__':
    main()
