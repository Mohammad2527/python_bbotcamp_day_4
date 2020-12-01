import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)


namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")


print(names)
random_name = random.randint(0, (len(names)-1))

print(f"{names[random_name]} is going to buy the meal today!")