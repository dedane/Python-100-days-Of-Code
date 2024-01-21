import random

name_string = input("Give me everybody's names separated with a , ")
names = name_string.split(',')

name_items = len(names)

random_name_choice = random.randint(0, name_items - 1)


print(names[random_name_choice], ' is going to buy a meal today ')