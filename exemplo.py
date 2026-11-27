import pandas as pd

idades_lista = [25,38,22,28]

idades_series=pd.Series([25,30,22,28])

# print(f"Lista: \n{idades_lista}\n")
# print(f"Séries: \n{idades_series}")

# Manipulando Series e Consultas
notas = pd.Series([9.5, 8.0, 7.5, 9.0], index=['João', 'Maria', 'Pedro', 'Ana'])

print(notas['Maria'])   # Acessando a nota de Maria pelo rótulo​
print(notas.iloc[2])    # Acessando a nota de Pedro pela posição​
print(notas.mean())     # Calculando a média das notas​
print(notas[notas > 8]) # Filtrando notas maiores que 8​
print(notas.describe()) # Estatísticas descritivas das notas​