'''
File Handling Modes:
- read: r
- write: w
- append: a
- read & write: r+
'''

vacationPlaces = ["London", "Paris", "New York", "Mumbai", "Bangkok"]

vacationFile = open("Vacations.txt", "w") #Writing to a file

for city in vacationPlaces:
    vacationFile.write(city + "\n")

vacationFile.close()

vacationFile = open("Vacations.txt", "a") #Appending to a file
vacationFile.write("Toronto")
vacationFile.close()

file = open("Vacations.txt", "r")

content = file.read() #Reads the entire file in one go
print(content)
file.readline() #Reads a single line

for city in file: #Reads file line by line
    print(city, end="")

for city in file:
    if 'o' in city:
        print(city, end="")

file.close()

#Temporarily open a file
with open("Vacations.txt", "r") as vacationFile:
    for city in vacationFile:
        print(city, end="")