import pandas as pd

dados = {
    "produto": ["Notebook", "Mouse", "Teclado", "Notebook", "Mouse",
                "Monitor", "Teclado", "Notebook", "Monitor", "Mouse"],

    "vendedor": ["Ana", "João", "Carla", "Ana", "João",
                 "Carla", "Ana", "João", "Carla", "Ana"],

    "cidade": ["São Paulo", "Santos", "São Paulo", "Santos", "São Paulo",
               "São Paulo", "Santos", "São Paulo", "Santos", "São Paulo"],

    "quantidade": [2, 5, 3, 1, 4, 2, 6, 1, 3, 5],

    "valor_unitario": [3500, 80, 150, 3500, 80,
                       1200, 150, 3500, 1200, 80]
}

df = pd.DataFrame(dados)

print(df)
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df["cidade"].unique())
print(df["cidade"].value_counts())
df["faturamento"]=df["quantidade"]*df["valor_unitario"]
print(df)
print(df["faturamento"].sum())
print(df.groupby("produto")["faturamento"].sum())
print(df.groupby("vendedor")["faturamento"].sum())
print(df[["produto", "vendedor", "quantidade", "valor_unitario", "faturamento"]])
print(df.groupby("cidade")["faturamento"].sum())
print(df.groupby("cidade")["quantidade"].sum())
print(df[df["cidade"] == "São Paulo"])
print(df[(df["cidade"] == "São Paulo") & (df["produto"] == "Notebook")])
print(df.groupby("produto")["quantidade"].sum())
print(df.groupby("produto")["faturamento"].mean())
print(df.groupby("produto")["valor_unitario"].mean())
print(df.groupby(["produto", "cidade"])["faturamento"].sum())
df.to_csv("vendas_projetos.csv" ,index=False)