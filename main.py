import pandas as pd

# Обратимся по индексу к элементам Series.

data = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
series_from_dict = pd.Series(data)
print(series_from_dict)

# Доступ по метке индекса
print(series_from_dict.loc['b'])  # 20

# Доступ по позиции
print(series_from_dict.iloc[2])  # 30

print(series_from_dict[['a', 'c', 'e']])



# # Создание Series

#Автоиндексы
# data = [10, 20, 30, 40, 50]
# series = pd.Series(data)
# print(series)

#С явными индексами
# data = [10, 20, 30, 40, 50]
# ind = ['a', 'b', 'c', 'd', 'e']
# series_with_index = pd.Series(data, index=ind)
#
# # Вывод Series без строки dtype
# print(series_with_index.to_string()) #dtype - обязательный аргумент при выводе. Вы можете его убрать, только в случае преобразования Series в String, например.