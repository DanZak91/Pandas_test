import pandas as pd
import numpy as np

# # Создание Series
#
# #Автоиндексы
# data = [10, 20, 30, 40, 50]
# series = pd.Series(data)
# print(series)
#
# #С явными индексами
# data = [10, 20, 30, 40, 50]
# ind = ['a', 'b', 'c', 'd', 'e']
# series_with_index = pd.Series(data, index=ind)
#
# # Вывод Series без строки dtype
# print(series_with_index.to_string()) #dtype - обязательный аргумент при выводе. Вы можете его убрать, только в случае преобразования Series в String, например.
#
#
# # Обратимся по индексу к элементам Series.
# data = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# series_from_dict = pd.Series(data)
# print(series_from_dict)
#
# # Доступ по метке индекса
# print(series_from_dict.loc['b'])  # 20
#
# # Доступ по позиции
# print(series_from_dict.iloc[2])  # 30
#
# #Доступ по индексам сразу же к нескольким элементам.
# print(series_from_dict[['a', 'c', 'e']])
#
# #Складываем Series c числом
# series_added = series_from_dict + 10
# print(series_added)
#
# #Умножаем на 2
# multiplied_series = series_from_dict * 2
# print(multiplied_series)
#
# #Можем складывать series.
# another_series = pd.Series([5, 15, 25, 35, 45], index=['a', 'b', 'c', 'd', 'e'])
# sum_series = series_from_dict + another_series
# print(sum_series)
#
#
# ##Также посмотрим на то, как работает None в Series.
# # Создание списка индексов
# index = ['a', 'b', 'c', 'd', 'e']
#
# # Создание Series с отсутствующими значениями
# data_with_nan = [10, 20, None, 40, 50]
# series_with_nan = pd.Series(data_with_nan, index=index)
# print("Series с отсутствующими значениями:")
# print(series_with_nan)
#
# # Заполнение отсутствующих значений
# filled_series = series_with_nan.fillna('0')
# print("\nSeries с заполненными отсутствующими значениями:")
# print(filled_series)
#
# # Удаление отсутствующих значений
# dropped_series = series_with_nan.dropna()
# print("\nSeries без отсутствующих значений:")
# print(dropped_series)
#
#
#
#
#
# # # Cоздадим первый Dataframe из словаря списков.
# # data = {
# #     'Name':['Alice', 'Bob', 'David'],
# #     'Age':[25, 30, 29],
# #     'City':['NY', 'LA', 'Moscow']
# # }
# #
# # df = pd.DataFrame(data)
# # print(df,'\n')
# #
# # # Dataframe из списка списков с метками столбцов.
# # data1 = [
# #     ['Alice', 25, 'NY'],
# #     ['Bob', 30, 'LA', ],
# #     ['David', 29, 'Moscow']
# # ]
# # df2 = pd.DataFrame(data1, columns=['Имя', 'Возраст', 'Город'])
# # print(df2)






# df = pd.read_csv('data.csv')
# print(df.head(2)) #первые 2 строки
# print(df.tail(2)) #последние 2 строки
# print(df.info()) #  получить информацию о датафрейме, например о типах данных или о размере
#
# df['Salary'] = [5000, 6000, 7000, 8000]  # как добавлять столбец(цы) к уже существующему dataframe.
# print(df)
#
# df = df.drop('Salary', axis=1) #УДАЛЕНИЕ СТОЛБЦА
# df = df.drop(1, axis=0) #УДАЛЕНИЕ СТРОКИ по ИНДЕКСУ









'''КОНКАТЕНАЦИЯ (concat): Эта операция используется для объединения двух или более DataFrame по строкам или столбцам.
 Конкатенация не учитывает значения ключей (индексов) и просто объединяет DataFrame друг за другом.'''

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
}, index=[0, 1, 2, 3])

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7']
}, index=[4, 5, 6, 7])

# Конкатенация двух DataFrame по строкам (axis=0)
result_concat = pd.concat([df1, df2], axis=0)
print("Конкатенация по строкам:\n", result_concat)

# Конкатенация двух DataFrame по столбцам (axis=1)
result_concat_cols = pd.concat([df1, df2], axis=1)
print("\nКонкатенация по столбцам:\n", result_concat_cols)



'''СЛИЯНИЕ (merge): Эта операция используется для объединения двух DataFrame на основе значений одного или нескольких общих столбцов (подобно SQL JOIN). 
Слияние учитывает ключевые значения для определения соответствующих строк.'''
df1 = pd.DataFrame({
    'Key': ['A', 'B', 'C'],
    'Value1': [10, 20, 30]
})

df2 = pd.DataFrame({
    'Key': ['A', 'B', 'D'],
    'Value2': [100, 200, 400]
})

print(df1,'\n')
print(df2)

# Слияние двух DataFrame по общему столбцу 'Key' (INNER) Только совпадающие ключи из обоих DataFrame (Только общие ключи (пересечение))
result_merge = pd.merge(df1, df2, on='Key', how='inner')
print("\nСлияние по общему столбцу 'Key' (inner join):\n", result_merge)

# Слияние двух DataFrame по общему столбцу 'Key' (LEFT). Все ключи из левого (df1) + совпадения из правого
result_merge_left = pd.merge(df1, df2, on='Key', how='left')
print("\nСлияние с левым объединением (left join):\n", result_merge_left)

# Слияние двух DataFrame по общему столбцу 'Key' (Right). Все ключи из правого (df2) + совпадения из левого
result_merge_right = pd.merge(df1, df2, on='Key', how='right')
print("\nСлияние с правым объединением (right join):\n", result_merge_right)

# Слияние двух DataFrame с внешним объединением (outer join). Все ключи из обоих DataFrame + NaN для пропущенных значений. (Все ключи из обоих DF (объединение))
result_merge_outer = pd.merge(df1, df2, on='Key', how='outer')
print("\nСлияние с внешним объединением (outer join):\n", result_merge_outer)

#  Декартово произведение (все комбинации строк)/ Все возможные комбинации строк
result_merge_cross = pd.merge(df1, df2,  how='cross')
print("\n Декартово произведение (все комбинации строк):\n", result_merge_cross)

#Объединение по разным именам столбцов:
#pd.merge(df1, df2, left_on='Key1', right_on='Key2', how='left')

#Индикатор источника данных:
'''Добавляет столбец _merge с значениями:
"both" - есть в обоих
"left_only" - только в левом
"right_only" - только в правом '''
source_where = pd.merge(df1, df2, how='outer', indicator=True)
print("\n Индикатор источника данных: \n", source_where)





#ОЧИСТКА ДАННЫХ SERIES:
# Создание Series с пропущенными значениями
s = pd.Series([1, 2, np.nan, 4, np.nan, 6])

# 1. Удаление пропущенных значений
s_dropped = s.dropna()
print("\nУдаление пропущенных значений:")
print(s_dropped)

# 2. Заполнение пропущенных значений определенным значением
s_filled = s.fillna(0)
print("\nЗаполнение пропущенных значений нулями:")
print(s_filled)

# 3. Заполнение пропущенных значений средним значением серии
s_filled_mean = s.fillna(s.mean())
print("\nЗаполнение пропущенных значений средним значением:")
print(s_filled_mean)


#ОЧИСТКА ДУБЛИКАТОВ SERIES:
# Создание Series с дубликатами
s = pd.Series([1, 2, 2, 3, 4, 4, 4, 5])

# 1. Определение дубликатов
duplicates = s.duplicated()
print("\nОпределение дубликатов в Series:")
print(duplicates)

# 2. Удаление дубликатов
s_no_duplicates = s.drop_duplicates()
print("\nУдаление дубликатов из Series:")
print(s_no_duplicates)



#ПРЕОБРАЗОВАНИЕ ТИПОВ SERIES:
# Создание Series с числовыми значениями в виде строк
s = pd.Series(['1', '2', '3', '4.5', '5'])
# Преобразование типа данных из строк в числовой формат
s_converted = pd.to_numeric(s)
print("\nПреобразование типов данных в числовой формат:")
print(s_converted)


#УДАЛЕНИЕ ВЫБРОСОВ
'''IQR (Interquartile Range), или межквартильный размах, — это статистический показатель, который используется для описания разброса данных в наборе. 
IQR измеряет разницу между первым квартилем (25-й процентиль, Q1) и третьим квартилем (75-й процентиль, Q3). 
Проще говоря, IQR показывает, насколько широко распространены значения в середине распределения данных. 
'''
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
s = pd.Series(data)
# Вычисление первого и третьего квартилей
Q1 = s.quantile(0.25)  # Первый квартиль (25-й процентиль)
Q3 = s.quantile(0.75)  # Третий квартиль (75-й процентиль)
# Вычисление IQR
IQR = Q3 - Q1
# Определение границ выбросов
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(f"IQR: {IQR}")
print(f"Нижняя граница выбросов: {lower_bound}")
print(f"Верхняя граница выбросов: {upper_bound}")
# Выявление выбросов
outliers = s[(s < lower_bound) | (s > upper_bound)]
print(f"Выбросы в данных: {outliers.tolist()}")





#ОЧИСТКА ДАННЫХ DATAFRAME:
# Создание DataFrame с пропущенными значениями
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, 5]
})
# Удаление строк с любыми пропущенными значениями
df_dropped = df.dropna()
print("Удаление строк с пропущенными значениями:")
print(df_dropped)
# Удаление столбцов, содержащих пропущенные значения
df_dropped_columns = df.dropna(axis=1)
print("\nУдаление столбцов с пропущенными значениями:")
print(df_dropped_columns)





#ОБРАБОТКА пропущенныХ значения и вставит туда средние значения, а также вставит нули.
# Заполнение пропущенных значений средним значением по столбцу
df_filled_mean = df.fillna(df.mean())
print("\nЗаполнение пропущенных значений средним:")
print(df_filled_mean)
# Заполнение пропущенных значений постоянным значением
df_filled_constant = df.fillna(0)
print("\nЗаполнение пропущенных значений нулями:")
print(df_filled_constant)


#ОЧИСТКА ДУБЛИКАТОВ DATAFRAME:
# Создание DataFrame с дубликатами
df_duplicates = pd.DataFrame({
    'A': [1, 2, 2, 4, 5],
    'B': [1, 2, 2, 4, 5]
})
# Удаление дубликатов
df_no_duplicates = df_duplicates.drop_duplicates()
print("\nУдаление дубликатов:")
print(df_no_duplicates)


#ПРЕОБРАЗОВАНИЕ ТИПОВ DATAFRAME:
# Создание DataFrame с типами данных для преобразования
df_types = pd.DataFrame({
    'A': ['1', '2', '3', '4'],
    'B': ['10.1', '20.2', '30.3', '40.4']
})
# Изменение типа данных столбца
df_types['A'] = df_types['A'].astype(int)
df_types['B'] = df_types['B'].astype(float)
print("\nИзменение типов данных:")
print(df_types)




#УДАЛЕНИЕ Выбросов.
'''Выбросы (или аномальные значения) — это значения данных, которые значительно отличаются от большинства других наблюдений в наборе данных. 
Они могут быть аномально большими или малыми по сравнению с остальными значениями. 
Выбросы могут возникать по различным причинам, таким как ошибки измерений, ошибки ввода данных или естественные вариации.
'''
# Создание DataFrame с выбросами
df_outliers = pd.DataFrame({
    'A': [1, 2, 3, 1000, 5]
})

# Удаление выбросов
df_no_outliers = df_outliers[df_outliers['A'] < 100]
print("\nУдаление выбросов:")
print(df_no_outliers)