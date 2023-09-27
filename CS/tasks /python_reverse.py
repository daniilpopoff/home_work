import math
import numpy as np

data_tuple = ('G', 6.13, 'I','b','n', True,'o','t',3, 'Y', 1,'p')
letters =[]
numbers = []
for i in range(len(data_tuple)):
    if isinstance(data_tuple[i], str):
        letters.append(data_tuple[i])
    else:
       numbers.append(data_tuple[i])
print(numbers)
numbers.remove(6.13)

# numbers[0],numbers[-1]=numbers[-1],numbers[0]
numbers.remove(True)
numbers.insert(1,2)
numbers.sort()
squared_numders = [x**2 for x in numbers]

letters.reverse()
word= 'Python'
letters[-2] = letters[-2].lower()
letters[-1] = letters[-1].lower()
letters[-3]=letters[-3].upper()
letters[1]=letters[1].lower()
letters[0]=letters[0].upper()

letters.insert(0,True)
letters_tup = tuple(letters)
squared_numbers_tup = tuple(squared_numders)
print(f'letters{letters_tup}')
print(f'numbers {squared_numbers_tup}')