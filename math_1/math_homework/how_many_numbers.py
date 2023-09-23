numbers = [2, 3, 5, 11]
count= 0 
for i in range(10,100):
    if all(i % num == 0 for num in numbers):
        count= count + 1
print("Количество двузначных чисел, делящихся на 2, 3, 5 и 11:", count)