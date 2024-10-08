# 10-1

with open('learning_Python.txt') as file_object:
    
    content = file_object.read()

print(content)
print()
print(content)
print()
print(content)

print()

# 10-2

file = open('learning_Python.txt', 'r')

linesofcode = file.readlines()

file.close()

for line in linesofcode:
    changed_line = line.replace('Python', 'C')
    print(changed_line)

print()
# 10-3

filename = 'guest.txt'

print("Please enter in your full name so you can be added to the guest list!")

with open(filename, 'w') as file_object:
    file_object.write(input())

# 10-4

guest_book_file = 'guest_book.txt'
with open('guest_book.txt', 'a') as guestbook:
    while True:

        name = input("Please enter your name (or type 'exit' to quit): ")

        if name.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            print("Hello,", name, "! Welcome!")
            guestbook.write(f"{name}\n")

print()

# 10-5

answers = 'answers.txt'
with open('answers.txt', 'a') as progsurvey:
    while True:

        answer = input("Please enter one reason you like programming (or type 'exit' to quit): ")

        if answer.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            print("Thanks for your respond!")
            progsurvey.write(f"{answer}\n")

print()

# 10-6

num1 = input("Enter the first number: ")

num2 = input("Enter the second number: ")

try:
    result = int(num1) + int(num2)
    print(f"The result of adding {num1} and {num2} is: {result}")

except ValueError:
     print("Please enter valid numbers. Make sure to use numbers only.")

# 10-7

while True:

    num1 = input("Enter the first number (or type 'exit' to quit): ")
    if num1.lower() == 'exit':
        print("Peace!")
        break

    num2 = input("Enter the second number: ")

    try:
        
        result = int(num1) + int(num2)
        print(f"The result of adding {num1} and {num2} is: {result}")
    except ValueError:
        
        print("Please enter valid numbers. Make sure to use digits only.")
