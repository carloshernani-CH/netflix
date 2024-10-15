import pandas as pd
import numpy as np
from numpy.linalg import svd
import random
import matplotlib.pyplot as plt

# Carregar o dataset
ratings = input("Qual dos arquivos deseja utilizar?")
print("1 - ratings_small.csv")
print("2 - ratings.csv")
if ratings == "1":
    df = pd.read_csv('ratings_small.csv', sep=',',)
elif ratings == "2":
    df = pd.read_csv('ratings.csv', sep=',', )

# Criar a matriz de usuários e filmes (A)
A = df.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Exibir o início da matriz para visualização
print("Matriz A:")
print(A.head())

# Selecionar uma posição aleatória na matriz A
i = random.randint(0, A.shape[0] - 1)
j = random.randint(0, A.shape[1] - 1)

# Gerar a matriz B com o valor "estragado"
B = A.copy()
B.iloc[i, j] = random.uniform(0, 5)  # Substituir por um valor aleatório entre 0 e 5
print(f"Valor original da posição ({i}, {j}): {A.iloc[i, j]}")
print(f"Valor 'estragado' inserido na posição ({i}, {j}): {B.iloc[i, j]}")

# Decomposição SVD da matriz B (estragada)
U, S, Vt = svd(B, full_matrices=False)

# Reduzir a dimensão dos dados para k componentes principais
k = 50  # Número de componentes principais
U_reduced = U[:, :k]
S_reduced = np.diag(S[:k])
Vt_reduced = Vt[:k, :]

# Reconstrução aproximada da matriz B (estragada)
B_approx = np.dot(np.dot(U_reduced, S_reduced), Vt_reduced)

# Previsão do valor original
predicted_value = B_approx[i, j]

# Exibir o valor real, o valor estragado e o valor previsto
print(f"Valor real: {A.iloc[i, j]}")
print(f"Valor previsto: {predicted_value}")

# Lista para armazenar os erros
errors = []

# Número de estimativas
n_estimates = 1000

for _ in range(n_estimates):
    # Selecionar uma posição aleatória
    i = random.randint(0, A.shape[0] - 1)
    j = random.randint(0, A.shape[1] - 1)
    
    # Gerar a matriz B (estragada) novamente para cada iteração
    B = A.copy()
    B.iloc[i, j] = random.uniform(0, 5)
    
    # Decompor a matriz estragada
    U, S, Vt = svd(B, full_matrices=False)
    U_reduced = U[:, :k]
    S_reduced = np.diag(S[:k])
    Vt_reduced = Vt[:k, :]
    
    # Prever o valor original
    B_approx = np.dot(np.dot(U_reduced, S_reduced), Vt_reduced)
    predicted_value = B_approx[i, j]
    
    # Calcular o erro
    real_value = A.iloc[i, j]
    error = real_value - predicted_value
    errors.append(error)

# Gerar o histograma dos erros
plt.hist(errors, bins=30, edgecolor='black')
plt.xlabel('Erros')
plt.ylabel('Frequência')
plt.title('Histograma dos erros nas previsões')
plt.show()