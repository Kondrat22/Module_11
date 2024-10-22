import requests  # может достать какую-либо информацию из интернета по ссылке.
import matplotlib.pyplot as plt  # создаёт графики
# позволяет быстрее и эффективнее работать с массивами данных.
import numpy as np
# помогает выполнить анализ данных и вывести результаты на консоль в виде таблицы.
import pandas as pd


print("Пример библиотеки PANDAS:")
dict_cities = {'City': ['Moscow', 'Saint-Petersburg', 'Novosibirsk'],
               'Population': ['12,6 mln', '5,4 mln', '1,6 mln']}
df = pd.DataFrame(dict_cities)
print(df.head())


print("Пример библиотеки NumPy:")
arr = np.array([-1, -4, 2, 8, 1, 3, -2])
arr[0] = 0
print(arr[0])
print(arr[0:2])
print(arr[::-1])
print(arr[arr < 2])
print(arr[(arr < 2) & (arr > 0)])
print(arr[(arr > 6) | (arr < -3)])
arr[1:6] = 0
print(arr)


print("Пример библиотеки Matplotlib:")
# plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots()
x = [-3, -2, -1, 0, 1, 2, 3]
y = [9, 4, 1, 0, 1, 4, 9]
print(ax.plot(x, y))


print("Пример библиотеки Requests:")
url = 'https://www.kinopoisk.ru/lists/movies/top250/'
r = requests.get(url)
print(r.text)
