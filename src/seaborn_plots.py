import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("games.csv")

df["moves_made"] = df["moves"].apply(
    lambda moves: int(np.floor(len(moves.split(' '))/2)))
df["opening_name"] = df["opening_name"].apply(lambda name: name.split(":")[0])
df["avg_rating"] = (df["white_rating"]+df["black_rating"])/2


sns.pairplot(data=df, vars=["white_rating","black_rating"])
plt.show()


sns.jointplot(data=df, x="white_rating", y="black_rating")
plt.show()

sns.violinplot(data=df, x="opening_ply", y="avg_rating")
plt.show()

best_openings=df["opening_name"].value_counts().head(10).index
df1=df[df["opening_name"].isin(best_openings)][["opening_name","winner","opening_ply"]]

sns.heatmap(df1.pivot_table(index="opening_name",columns="winner",values="opening_ply", aggfunc=np.mean),annot=True)
plt.show()
