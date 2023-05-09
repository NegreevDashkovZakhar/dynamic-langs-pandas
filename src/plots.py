import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv("games.csv")

df["moves_made"] = df["moves"].apply(
    lambda moves: int(np.floor(len(moves.split(' '))/2)))
df["opening_name"] = df["opening_name"].apply(lambda name: name.split(":")[0])
df["avg_rating"] = (df["white_rating"]+df["black_rating"])/2

# 1.1
openings = df["opening_name"].value_counts().head(5)
top_opening_names = openings.index
plt.bar(top_opening_names, openings)
plt.show()


# 1.2
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ax1.title.set_text('Результат при победе белых')
ax2.title.set_text('Результат при победе черных')
ax3.title.set_text('Количество ходов при победе белых')
ax3.xaxis.set_label_text('Количество ходов')
ax3.yaxis.set_label_text('Количество партий')
ax4.title.set_text('Количество ходов при победе черных')
ax4.xaxis.set_label_text('Количество ходов')
ax4.yaxis.set_label_text('Количество партий')

plt.subplot(221)
victories = df[df["winner"] == "white"]["victory_status"].value_counts()
plt.bar(victories.index, victories)

plt.subplot(222)
victories = df[df["winner"] == "black"]["victory_status"].value_counts()
plt.bar(victories.index, victories)

plt.subplot(223)
moves_to_win = df[df["winner"] == "white"]["moves_made"].value_counts()
plt.scatter(moves_to_win.index, moves_to_win)

plt.subplot(224)
moves_to_win = df[df["winner"] == "black"]["moves_made"].value_counts()
plt.scatter(moves_to_win.index, moves_to_win)

plt.show()

# 2

df[df["rated"] == True].plot(
    x="white_rating", y="black_rating", kind='scatter')
plt.show()

df["moves_made"].plot(kind='kde')
plt.show()

df.boxplot(column=["avg_rating"], by=["opening_ply"])
plt.show()

# 5

best_openings=df["opening_name"].value_counts().head(25).reset_index()
fig = px.pie(best_openings,names="index",values="opening_name")
fig.show()
