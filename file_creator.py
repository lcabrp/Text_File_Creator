# file_creator.py

name = input("What's your name? ")

with open('example.txt', 'w') as file:
    file.write(f"{name} created this file\n")  

color = input("What's your favorite color? ")

with open('example.txt', 'a') as file:
    file.write(f"{name}'s favorite color is {color}\n")  


