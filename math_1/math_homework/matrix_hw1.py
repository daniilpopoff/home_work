import numpy as np
# 1.1.3
A = np.array([[2, -1, 0], [3, 4, -2], [-3, 1, 5]])
B = np.array([[3, 1, 2], [-2, 1, 3], [0, 2, -4]])
antwort113 = 4*A - 5 * B  
print (antwort113)
# 1.1.7
a = np.array([[4, 0, -2, 3, 1]])
b = np.array([[3], [1], [-1], [5], [2]])
answer117 = np.dot(a,b)
print(f'ответ примера номер 1.1.7{answer117}') 

a = np.array([[1, 2],[3, 6]])
b = np.array([[2,6], [-1,-3]])
answer119 = np.dot(b,a)
print(f'ответ примера номер 1.1.9{answer119}')

print(f'ответ {2**1}')

import numpy as np
import matplotlib.pyplot as plt

# Создайте сетку точек на координатной плоскости
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

# Определите условие x**2 - y**2 > 0
condition = X**2 - Y**2 > 0

# Создайте контурный график, где True будет отображаться как 1 (белый), а False как 0 (синий)
plt.contourf(X, Y, condition, levels=[0, 1], colors=['blue', 'white'])

# Настройте оси и отобразите график
plt.xlabel('x')
plt.ylabel('y')
plt.title('Регион, где x**2 - y**2 > 0')
plt.grid()
plt.show()
