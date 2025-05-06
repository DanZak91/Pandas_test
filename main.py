import pandas as pd
# Создание Series

#Автоиндексы
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)

#С явными индексами
data = [10, 20, 30, 40, 50]
ind = ['a', 'b', 'c', 'd', 'e']
series_with_index = pd.Series(data, index=ind)

# Вывод Series без строки dtype
print(series_with_index.to_string()) #dtype - обязательный аргумент при выводе. Вы можете его убрать, только в случае преобразования Series в String, например.


# Обратимся по индексу к элементам Series.
data = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
series_from_dict = pd.Series(data)
print(series_from_dict)

# Доступ по метке индекса
print(series_from_dict.loc['b'])  # 20

# Доступ по позиции
print(series_from_dict.iloc[2])  # 30

#Доступ по индексам сразу же к нескольким элементам.
print(series_from_dict[['a', 'c', 'e']])

#Складываем Series c числом
series_added = series_from_dict + 10
print(series_added)

#Умножаем на 2
multiplied_series = series_from_dict * 2
print(multiplied_series)

#Можем складывать series.
another_series = pd.Series([5, 15, 25, 35, 45], index=['a', 'b', 'c', 'd', 'e'])
sum_series = series_from_dict + another_series
print(sum_series)


##Также посмотрим на то, как работает None в Series.
# Создание списка индексов
index = ['a', 'b', 'c', 'd', 'e']

# Создание Series с отсутствующими значениями
data_with_nan = [10, 20, None, 40, 50]
series_with_nan = pd.Series(data_with_nan, index=index)
print("Series с отсутствующими значениями:")
print(series_with_nan)

# Заполнение отсутствующих значений
filled_series = series_with_nan.fillna('0')
print("\nSeries с заполненными отсутствующими значениями:")
print(filled_series)

# Удаление отсутствующих значений
dropped_series = series_with_nan.dropna()
print("\nSeries без отсутствующих значений:")
print(dropped_series)



# Cоздадим первый Dataframe из словаря списков.
data = {
    'Name':['Alice', 'Bob', 'David'],
    'Age':[25, 30, 29],
    'City':['NY', 'LA', 'Moscow']
}

df = pd.DataFrame(data)
print(df,'\n')

# Dataframe из списка списков с метками столбцов.
data1 = [
    ['Alice', 25, 'NY'],
    ['Bob', 30, 'LA', ],
    ['David', 29, 'Moscow']
]
df2 = pd.DataFrame(data1, columns=['Имя', 'Возраст', 'Город'])
print(df2)