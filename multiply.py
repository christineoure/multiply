def hello(name, age):
    year = 2022 - age
    print(f"hello {name} you were born in {year}")

def my_country(country="Kenya"):
    return f"my country is {country}"

def greet (*names):
    print(names)

def multiply (*nums):
    multiply=1
    for m in nums:
        multiply*=m
    return multiply



