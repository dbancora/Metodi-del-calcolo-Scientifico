import scipy.io
import sksparse.cholmod as cholmod
import numpy as np
import time
# import resource --> funziona solo per linux
import psutil #funziona su windows
import os
import matplotlib.pyplot as plt

def load_matrix_from_file(filename):
    mat = scipy.io.loadmat(filename)
    A = mat['Problem'][0, 0]['A']
    A = scipy.sparse.csc_matrix(A)
    return A

def create_b_vector(A):
    n = A.shape[0]
    b = A.dot(np.ones(n))
    #DEBUG: print(b)
    return b

def cholesky_decomposition(A):
    # Ottieni la memoria usata prima della fattorizzazione di Cholesky
    memoria_iniziale = None
    if os.name == 'posix':  # Linux
        memoria_iniziale = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    elif os.name == 'nt':  # Windows
        process = psutil.Process()
        memoria_iniziale = process.memory_info().rss / (1024 * 1024)

    factor = cholmod.cholesky(A)

    # Ottieni la memoria usata dopo la fattorizzazione di Cholesky
    memoria_finale = None
    if os.name == 'posix':  # Linux
        memoria_finale = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    elif os.name == 'nt':  # Windows
        process = psutil.Process()
        memoria_finale = process.memory_info().rss / (1024 * 1024)

    # Calcola la memoria utilizzata dalla funzione
    memoria_utilizzata_chol = memoria_finale - memoria_iniziale

    return factor, memoria_utilizzata_chol

def solve_linear_system(factor, b):
    # Ottieni la memoria usata prima della fattorizzazione di Cholesky
    memoria_iniziale = None
    if os.name == 'posix':  # Linux
        memoria_iniziale = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    elif os.name == 'nt':  # Windows
        process = psutil.Process()
        memoria_iniziale = process.memory_info().rss / (1024 * 1024)

    x = factor(b)   

    #DEBUG: print(x) 

     # Ottieni la memoria usata dopo la fattorizzazione di Cholesky
    memoria_finale = None
    if os.name == 'posix':  # Linux
        memoria_finale = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    elif os.name == 'nt':  # Windows
        process = psutil.Process()
        memoria_finale = process.memory_info().rss / (1024 * 1024)
    
    # Calcola la memoria utilizzata dalla funzione
    memoria_utilizzata_sistemaLin = memoria_finale - memoria_iniziale

    
    return x, memoria_utilizzata_sistemaLin

def compute_relative_error(x):
    n = len(x)
    x_esatto = np.ones(n)
    errore_relativo = np.linalg.norm(x - x_esatto) / np.linalg.norm(x_esatto)
    return errore_relativo

def compute_percent_zeros(A):
    n_nonzero = A.count_nonzero()
    n_total = A.shape[0] * A.shape[1]
    percent_zero = 100 * (1 - (n_nonzero / n_total))
    return percent_zero

def compute_num_nonzeros(A):
    rows, cols = A.nonzero()
    num_nonzeros = len(rows)
    return num_nonzeros

# Funzione che esegue in loop le varie azioni 
def process_file(filename):
    print(f"Elaborazione file {filename}")
    A = load_matrix_from_file(os.path.join(cartella, filename))
    b = create_b_vector(A)
    start_time = time.time()

    factor, memoria_utilizzata_chol = cholesky_decomposition(A)

    #DEBUG: print(memoria_utilizzata_chol)

    x, memoria_utilizzata_sistemaLin = solve_linear_system(factor, b)

    #DEBUG: print(memoria_utilizzata_sistemaLin)

    memoria_totale = memoria_utilizzata_chol + memoria_utilizzata_sistemaLin

    print("La memoria utilizzata totale è {:.2f} MB".format(memoria_totale))

    end_time = time.time()
    tempo_cholesky = end_time - start_time
    
    #Stampa il tempo impiegato per la decomposizione di Cholesky
    print("Tempo impiegato per la decomposizione di Cholesky: {:.4f} secondi ".format(tempo_cholesky))
    
    errore_relativo = compute_relative_error(x)

    print("Errore relativo: {:.4e}".format(errore_relativo))

    percent_zero = compute_percent_zeros(A)
    num_nonzeros = compute_num_nonzeros(A)
    return tempo_cholesky, errore_relativo, percent_zero, num_nonzeros, memoria_totale

# definiamo due array per la creazione dei plot
tempi_totali = []
memoria_cholesky = []
nomi_matrici = []

# cartella contenente i file .mat
cartella = "./"

# loop sui file nella cartella
for filename in os.listdir(cartella):   

    if filename.endswith(".mat"):

        tempo_cholesky, errore_relativo, percent_zero, num_nonzero, memoria_totale = process_file(filename)
        tempi_totali.append(tempo_cholesky)
        nomi_matrici.append(filename)
        memoria_cholesky.append(memoria_totale)


# Ordina i tempi di esecuzione in base alla dimensione dei file
tempi_totali, memoria_cholesky, nomi_matrici = zip(*sorted(zip(tempi_totali, memoria_cholesky, nomi_matrici), key=lambda x: os.path.getsize(os.path.join(cartella, x[2]))))

# Crea il grafico
fig, ax1 = plt.subplots(figsize=(10, 5))

color = 'tab:red'
ax1.set_xlabel('Nome della matrice (ordinate in base alla dimensione del file in ordine crescente)')
ax1.set_ylabel('Tempo di esecuzione della decomposizione di Cholesky e della risoluzione del sistema lineare (secondi)', color=color)
ax1.bar(nomi_matrici, tempi_totali, width=-0.2, align='edge', color=color)

# aggiungi etichette di testo per i tempi di esecuzione
for i, v in enumerate(tempi_totali):
    ax1.annotate(f'{v:.2f} s', xy=(i-0.2, v), ha='center', va='bottom', color=color)


ax1.tick_params(axis='y', labelcolor=color)
ax1.tick_params(axis='x', rotation=90)

ax2 = ax1.twinx()  # Secondo asse y

color = 'tab:blue'
ax2.set_ylabel('Memoria utilizzata (MB) per Cholensky e risoluzione sistema lineare', color=color)
ax2.bar(nomi_matrici, memoria_cholesky, width=0.2, align='edge', color=color, alpha=0.5)

# aggiungi etichette di testo per la memoria utilizzata
for i, v in enumerate(memoria_cholesky):
    ax2.annotate(f'{v:.2f} MB', xy=(i+0.2, v), ha='center', va='bottom', color=color)

ax2.tick_params(axis='y', labelcolor=color)

# Regola la distanza tra i subplot per separare le barre
plt.subplots_adjust(bottom=0.3)

fig.tight_layout()
plt.show()