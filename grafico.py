import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datos = pd.read_csv("datos/Titanic-Dataset.csv")

fig, ax = plt.subplots()
g = sns.countplot(x = "Sex", hue = "Survived", data = datos)
g.figure.savefig("plot.png")

fig, ax = plt.subplots()
g = sns.countplot(x = "Sex", hue = "Pclass", data = datos)
g.figure.savefig("plot2.png")
