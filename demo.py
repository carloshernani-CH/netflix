import pandas as pd
import numpy as np
from numpy.linalg import svd
import random
import matplotlib.pyplot as plt

# Carregar o dataset

df = pd.read_csv('ratings_small.csv', sep=',',)

# Criar a matriz de usuários e filmes (A)
A = df.pivot(index='userId', columns='movieId', values='rating').fillna(0)


# Selecionar uma posição aleatória na matriz A
i = random.randint(0, A.shape[0] - 1)
j = random.randint(0, A.shape[1] - 1)

# Gerar a matriz B com o valor "estragado"
B = A.copy()
B.iloc[i, j] = random.uniform(0, 5)  # Substituir por um valor aleatório entre 0 e 5

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

# Lista para armazenar os erros
errors = []

# Número de estimativas
n_estimates = 100

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