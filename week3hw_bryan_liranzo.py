# Question 4-6

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

# Question 4-7

mutiples = list(range(3, 30, 3))
for value in range(3,30, 3):
    print(mutiples)

# Question 4-8

squares = []
for value in range(1,11):
    cube = value ** 3
    squares.append(cube)

print(squares)

# Question 4-9

sq2 = [value**3 for value in range(1,11)]
print(sq2)

# THE LAST PART
n = 20
a = 0
print(a)
b = 1
print(b)

for i in range(n - 2):  
    next_value = a + b  
    print(next_value)   
    a = b  
    b = next_value