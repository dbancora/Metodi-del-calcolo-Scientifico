import scipy.io
import sksparse.cholmod as cholmod
import numpy as np
import time
# import resource --> funziona solo per linux
import psutil #funziona su windows
import os
import matplotlib.pyplot as plt

# Estrae la matrice dal file .mat e la salva nella variabile 'A'
def load_matrix_from_file(filename):
    mat = scipy.io.loadmat(filename)
    A = mat['Problem'][0, 0]['A']
    A = scipy.sparse.csc_matrix(A)
    return A

# Crea il vettore 'b' a partire dai valori contenuti nella matrice 'A' passata come parametro affinchè la sol. del sistema lineare sia un vettore 'x' composto da tutti 1
def create_b_vector(A):
    n = A.shape[0]
    b = A.dot(np.ones(n))
    #DEBUG: print(b)
    return b

# Esegue la decomposizione di cholesky della matrice 'A' passata come parametro e calcola la memoria utilizzata durante il processo 
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


# Risolve il sistema lineare Ax=b prendendo in ingresso la matrica 'A' fattorizzata con il metodo di Cholesky e il vettore 'b'. Calcola anche la memoria utilizzata durante il processo 
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

# Calcola l'errore relativo della soluzione 'x' del sistema lineare cofrontato con un vettore xEsatto (un vettore contente tutti 1)
def compute_relative_error(x):
    n = len(x)
    x_esatto = np.ones(n)
    errore_relativo = np.linalg.norm(x - x_esatto) / np.linalg.norm(x_esatto)
    return errore_relativo

# Calcola la percentuale di elementi uguali a 0 nella matrice 'A'
def compute_percent_zeros(A):
    n_nonzero = A.count_nonzero()
    n_total = A.shape[0] * A.shape[1]
    percent_zero = 100 * (1 - (n_nonzero / n_total))
    return percent_zero

# Calcola il numero di elementi diversi da 0 presenti nella matrice A
def compute_num_nonzeros(A):
    rows, cols = A.nonzero()
    num_nonzeros = len(rows)
    return num_nonzeros

# MainFile
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

# definiamo tre array per la creazione dei plot
tempi_totali = []
memoria_cholesky = []
nomi_matrici = []

# cartella contenente i file .mat
cartella = "./"

# Esegue il loop dei file contenuti nella cartella e richiama le funzioni necessarie per calolcare la soluzione del problema
for filename in os.listdir(cartella):   

    if filename.endswith(".mat"):

        tempo_cholesky, errore_relativo, percent_zero, num_nonzero, memoria_totale = process_file(filename)
        tempi_totali.append(tempo_cholesky)
        nomi_matrici.append(filename)
        memoria_cholesky.append(memoria_totale)


# Ordina i tempi di esecuzione in base alla dimensione dei file
tempi_totali, memoria_cholesky, nomi_matrici = zip(*sorted(zip(tempi_totali, memoria_cholesky, nomi_matrici), key=lambda x: os.path.getsize(os.path.join(cartella, x[2]))))

# Crea il grafico dei tempi di esecuzione 
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


# Crea il gragfico della memoria utilizzata
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