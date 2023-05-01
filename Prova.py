
'''
import scipy.io
import scipy.sparse
import scipy.sparse.linalg

import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve


# Carica il file .mat
mat = scipy.io.loadmat('C:/Users/dadec/Downloads/Metodi del calcolo Scientifico/ex15.mat')

# Accedi alla matrice A all'interno della struttura Problem
A = mat['Problem'][0,0]['A']
A = np.array(A)

'''
'''
# Crea il vettore b
n = A.shape[0]
x = np.ones((n,))
b = A.dot(x)
'''
'''
# Applica il metodo di Cholesky
L = scipy.linalg.cholesky(A, lower=True)

# Risolvi il sistema lineare ax=b
b = mat['b']
x = scipy.linalg.solve_triangular(L, scipy.linalg.solve_triangular(L.T, b, lower=False))

print(x)


#Stampa ogni valore di x
'''
'''
for val in x:
    print(val)
'''
'''
# controlla il numero di elementi non nulli nella matrice A
n_nonzero = A_sparse.count_nonzero()
# calcola il numero totale di elementi nella matrice A
n_total = A.shape[0] * A.shape[1]

# calcola la percentuale di elementi nulli
percent_zero = 100 * (1 - (n_nonzero / n_total))

print(f"La percentuale di elementi nulli nella matrice A è {percent_zero}%")

# Stampa gli elementi diversi da zero
'''
'''
rows, cols = A.nonzero()
for i in range(len(rows)):
    print(f"A[{rows[i]}, {cols[i]}] = {A[rows[i], cols[i]]}")

'''
'''
# E vengono anche contati
num_nonzeros = len(rows)
print("Numero di elementi diversi da zero in A: {}".format(num_nonzeros))
'''
import scipy.io
import sksparse.cholmod as cholmod

# Carica il file .mat
mat = scipy.io.loadmat('C:/Users/dadec/Downloads/Metodi del calcolo Scientifico/ex15.mat')

# Accedi alla matrice A all'interno della struttura Problem
A = mat['Problem'][0,0]['A']
# Calcola la decomposizione di Cholesky
factor = cholmod.cholesky(A)

# Risolvi il sistema lineare
x = factor(b)

print(x)
