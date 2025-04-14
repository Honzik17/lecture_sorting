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
        n = len(seznam)
        for i in range(n):
            # Najdeme index nejmenšího prvku od i do konce
            min_index = i
            for j in range(i + 1, n):
                if seznam[j] < seznam[min_index]:
                    min_index = j
            # Prohodíme nejmenší prvek s prvkem na pozici i
            seznam[i], seznam[min_index] = seznam[min_index], seznam[i]
        return seznam
    elif direction == "descending":
        n = len(seznam)
        for i in range(n):
            # Najdeme index největšího prvku od i do konce
            max_index = i
            for j in range(i + 1, n):
                if seznam[j] > seznam[max_index]:
                    max_index = j
            # Prohodíme největší prvek s prvkem na pozici i
            seznam[i], seznam[max_index] = seznam[max_index], seznam[i]
        return seznam
    else:
        return print("Invalid direction")

def bubble_sort(number_array):
    n = len(number_array)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if number_array[j] > number_array[j + 1]:
                number_array[j], number_array[j + 1] = number_array[j + 1], number_array[j]
    return number_array

def insertion_sort(number_array):
    for i in range(1, len(number_array)):
        suma = number_array[i]
        j = i - 1
        while j >= 0 and number_array[j] > suma:
            number_array[j + 1] = number_array[j]
            j -= 1
        number_array[j + 1] = suma
    return number_array


def main():
    data = read_data("numbers.csv")
    print(data)
    print(selection_sort([88, 36, 21, 54, 99, 1, 81, 18, 21, 36, 61], "ascending"))
    print(bubble_sort([88, 36, 21, 54, 99, 1, 81, 18, 21, 36, 61]))
    print(insertion_sort([88, 36, 21, 54, 99, 1, 81, 18, 21, 36, 61]))
    pass


if __name__ == '__main__':
    main()
