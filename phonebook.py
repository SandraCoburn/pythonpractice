import csv

file = open("phonebook.csv", "a") #a for append things to the file, it create file if it doesn't exist

name = input("Name: ")
number = input("Number: ")

writer = csv. writer(file) #pass open file to read it
writer.writerow((name, number)) #it will take care of formating

file.close()

#if you use "with" and "as" on line 3 you don't need to close the file(line 11):
#with open("phonebook.cs", "a") as file: