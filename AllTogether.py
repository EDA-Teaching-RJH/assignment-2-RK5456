### Part Four -- your code goes here. 

import random

numbers = [random.randint(1,100) for _ in range(10)]
print("This is the initial list", numbers)

# even numbers now will be removed, the pop will remove even numbers.
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        numbers.pop(i) 
    else:
        i += 1
    
print("odd numbers are ", numbers)

