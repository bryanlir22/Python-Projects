# Section 6-1

personinfo = {
    'first_name': 'Steven',
    'last_name': 'Rush',
    'city': 'Albany',

}

print(personinfo)

print()

# Section 6-2

fav_numbers = {
    'Jess': 1,
    'Brandon': 23,
    'Engrie': 19,
    'Dennis': 66,
    'Justin': 72,
}
print(fav_numbers)

print()

# Section 6-3

glossary = {
    'Python': 'A programming language',
    'Debugging': 'Fixing mistakes in the programs code',
    'Terminal': 'Where the code is processed',
    'Chatgpt': 'It sucks',
    'Output': 'Is the data or information a program produces',
    'Loop': 'Repeats until condition is met',
    'Function': 'A set of instucitons to do something',
    'Variable': 'A place to store information',
    'C++': 'Another Programming language',
    'Input': 'Is the data that put in from the user of the program',
}
print("Python:", glossary['Python'])
print("Debugging:", glossary['Debugging'])
print("Terminal:", glossary['Terminal'])
print("Chatgpt:", glossary['Chatgpt'])
print("Output:", glossary['Output'])

print()

# Section 6-4

for word, meaning in glossary.items():
    print(f"{word}:")
    print(f"    {meaning}")
    print()

# Section 6-5

major_rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Mississippi': 'United States'
}

for river, country in major_rivers.items():
    print(f"The {river} runs through {country}.")

print()

for river in major_rivers:
    print(river)

print()

for country in major_rivers.values():
    print(country)

print()

# Section 6-7

personinfo2 = {
    'first_name': 'Brandon',
    'last_name': 'James',
    'city': 'Queens',

}

personinfo3 = {
    'first_name': 'Bryan',
    'last_name': 'Liranzo',
    'city': 'Bronx',

}

people = [personinfo, personinfo2, personinfo3]

for person in people:
    print(f"First Name:", {person['first_name']},", Last Name:", {person['last_name']}, ", City:", {person['city']})
    print()

# Secontion 6-8

pet_1 = {
    'owner': 'Jelly',
    'pet': 'dog',
}

pet_2 = {
    'owner': 'Jess',
    'pet': 'dog',
}

pet_3 = {
    'owner': 'Brandon',
    'pet': 'mouse',
}

pet_4 = {
    'owner': 'Steven',
    'pet': 'cat',
}

pet_5 = {
    'owner': 'Jelly',
    'pet': 'bird',
}

pet_6 = {
    'owner': 'Naldo',
    'pet': 'elepant',
}

pets = [pet_1, pet_2, pet_3, pet_4, pet_5, pet_6]
 
for eachpet in pets:
    print(f"Owner of pet:", {eachpet['owner']}, " Animal:", {eachpet['pet']})
    print()

# Section 6-9

favorite_places = {
    'Brandon': 'Mcdonalds',
    'Bryan': 'Libary',
    'Steven': 'E-TEC Building'
}

for human, fav in favorite_places.items():
    print(f"{human}'s place is a {fav}")
    print()

print()

# Section 6-10

fav_numbers2 = {
    'Jess': [1, 55],
    'Brandon': [23, 22],
    'Engrie': [19, 99],
    'Dennis': [66, 36],
    'Justin': [72, 22],
}

for name3, fav_num in fav_numbers2.items():
    print(f"{name3}'s favorite numbers are: {fav_num}")
    print()

# Section 6-11

cities = {
    'Bronx': ['1.47M', 'United States' ,'The Bronx is home to the Yankee Stadium'],
    'Manhattan': ['1.63M', 'United States', 'Central Park is one of the most famous urban parks in the world.'],
    'Queens': ['2.39M', 'United States', 'Queens is the most linguistically diverse place on Earth'],
}

print(cities)

