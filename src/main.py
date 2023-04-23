import numpy as np
import pandas as pd

df = pd.read_csv("games.csv")

print("2.1 вывод таблицы")
print(df)

print("\n2.2 вывод первых 5 элементов таблицы")
print(df.head(5))

print("\n2.3 вывод последних 5 элементов таблицы")
print(df.tail(5))

print("\n2.4 использовать функцию describe()")
print(df.describe(include=[np.number])["opening_ply"])

print("\n2.5 считывание значения конкретной ячейки")
print(df["opening_name"].values[3])
print(df.at[3, 'opening_name'])
print(df.loc[3]['opening_name'])

print("\n2.6 фильтрация строк по диапазону индекса")
print(df.filter(items=range(5,10), axis=0))

print("\n2.7 фильтрация набора данных по какому-либо условию")
print(df[df["opening_name"] == "Queen's Pawn Game: Zukertort Variation"])

print("\n2.8 работа с пропущенными значениями")
df.iloc[1:3,9] = np.nan
print("has empty columns:{}".format(df.isnull().values.any()))
print("remsolving empty values")
for i in df.columns[df.isnull().any(axis=0)]:     #---Applying Only on variables with NaN values
    df[i].fillna(df[i].mean(),inplace=True)
print("has empty columns:{}".format(df.isnull().values.any()))

print("\n2.9 создание нового поля вычисленного на основе значений других полей")

print("\n2.9.1 через выражение на базе имеющихся колонок")
df["avg_rating"] = (df["white_rating"]+df["black_rating"])/2
print(df["avg_rating"])

print("\n2.9.2 через DataFrame.apply")
df["avg_rating_apply"] = df.apply(lambda row: (row.white_rating+row.black_rating)/2 , axis = 1)
print(df["avg_rating_apply"])

print("\n2.9.3 через Series.apply")
df["opening_name"] = df["opening_name"].apply(lambda name: name.split(":")[0])
print(df["opening_name"])

print("\n2.10 сортировка по какому-либо из полей")
df.sort_values(by=["avg_rating"], ignore_index=True, inplace=True)
print(df["avg_rating"])

print("\n2.11 вычислить несколько статистик по колонкам")
print("First move frequency (in %)")
first_move_series = df["moves"].apply(lambda moves: moves.split(" ")[0])
print(first_move_series.value_counts(normalize=True) * 100)

print("Average rating difference when black wins")
print(df[df["winner"] == "black"].apply(lambda row: row.black_rating-row.white_rating , axis = 1).mean())

print("\n2.12 .value_counts()")
print("openings count:{}".format(df["opening_name"].value_counts()))

print("\n2.13 Вывод уникальных значений колонки")
print("all players with white:")
print(df["white_id"].unique())

print("\n2.14 Удалите текущий индекс и создайте новый индекс на базе новой колонки")
df.reset_index(drop=True, inplace=True)
df.set_index('id', inplace=True)
print(df)