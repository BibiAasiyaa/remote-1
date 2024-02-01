import random

def modelYear():
    '''returns a model year'''
    year = [2021, 2022, 2023, 2024]
    return random.choice(year)

print("This is file cars.py")
cars = ["Mercedes-Benz","Audi","Lexus","BMW"]
print("Car:",random.choice(cars))
print("Model year:",modelYear())
