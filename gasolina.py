import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

sns.lineplot(data=df, x="dia", y="venda").set(title="Preço da gasolina por dia")
plt.savefig('gasolina.png')