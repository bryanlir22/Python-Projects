#Problem 4-1
pizza = ['Cheese Pizza', 'Chicken Pizza', 'Bacon Pizza']

for pizza in pizza:
    print(f"I really love, {pizza.title()}.\n")

print("I honestly really love pizza!")

#Problem 4-2

animals = ['dog', 'cat', 'fish']

for animals in animals:
    print(f"{animals.title()}")

print("I dog would make a great pet!")

print("All of these animals would make great pets!")

#Problem 4-3

numbers = list(range(1, 21))

print(numbers)

#Problem 8-1

def topic(learning):
    """Display what we are learning."""
    print(f"Hello we are learning {learning.title()}!")
          
topic('functions')
          
#Problem 8-2

def favorite_book(title):
    """Display your favorite book"""
    print(f"One of my favorite books is {title.title()}!")

favorite_book('Rich Dad, Poor Dad')

#Problem 8-3

def makeshirt(shirtsize, text):
    """Display shirt size and requested text)"""
    print(f"The shirt size will be {shirtsize.title()} and the text on the shirt will say {text.title()}.")

makeshirt('Large', 'Hello there')

makeshirt(shirtsize='Small', text='Goodbye Loser')

#Problem 8-4

def make_shirt(shirtsize2='Large', text2='I love Python'):
    """Display shirt size and requested text)"""
    print(f"The shirt size will be {shirtsize2.title()} and the text on the shirt will say {text2.title()}.")

make_shirt()

#Promble 8-5

def decribe_city(city,country='United States',):
    print(f"{city.title()} is located in the {country.title()}!")

decribe_city('Bronx')
decribe_city('Queens')
decribe_city('Albany')

#Problem 8-6

def city_country(city, country):
    location_format = f"{city} {country}"
    return location_format.title()

location = city_country('Bronx', 'United States')
print(location)

