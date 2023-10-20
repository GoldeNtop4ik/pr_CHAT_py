import shelve

FILENAME = "G:/python/states2"

with shelve.open(FILENAME) as states:
    for city in states.keys():
        print(city, end=" ")  # London Paris Berlin Madrid
    print()
    for country in states.values():
        print(country, end=" ")  # Great Britain France Germany Spain
"""
import shelve

FILENAME = "G:/python/states2"
with shelve.open(FILENAME) as states:
    for key in states:
        print(key," - ", states[key])
"""
"""
import shelve

FILENAME = "G:/python/states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

with shelve.open(FILENAME) as states:
    print(states["London"])
    print(states["Paris"])
"""
"""
import csv

FILENAME = "G:/python/users.csv"

users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]

with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    # запись нескольких строк
    writer.writerows(users)

    user = {"name": "Sam", "age": 41}
    # запись одной строки
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])
"""
"""
FILENAME = "G:/python/messages.txt"
messages = list()

for i in range(4):
    message = input("Введите строку " + str(i + 1) + ": ")
    messages.append(message + "\n")

with open(FILENAME, "a") as file:
    for message in messages:
        file.write(message)

print("Считанные сообщения")
with open(FILENAME, "r") as file:
    for message in file:
        print(message, end="")
"""
"""
with open('G:/python/hello.txt', "r") as file:
    str1 = file.readline()
    print(str1, end="")
    str2 = file.readline()
    print(str2)
"""

"""with open('G:/python/hello.txt', "a") as file:
    file.write("\ngood bye, world")
"""
"""
somefile = open('G:/python/hello.txt')
somefile.readline()
"""
"""
try:
    somefile = open('G:/python/hello.txt', "w")
    try:
        somefile.write("hello world")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)
"""
