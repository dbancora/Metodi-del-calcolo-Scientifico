import scipy.io
import sksparse.cholmod as cholmod
import numpy as np
import time
# import resource --> funziona solo per linux
import psutil #funziona su windows
import os
import matplotlib.pyplot as plt

# cartella contenente i file .mat
cartella = "./"

# definiamo due array per la creazione dei plot
tempi_cholesky = []
memoria_cholesky = []
nomi_matrici = []

# loop sui file nella cartella
for filename in os.listdir(cartella):   

    if filename.endswith(".mat"):
        # Ottieni il consumo di memoria corrente (Linux)
        '''
        def memoria_usata():
            return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
        '''
        # todo: sistemare consumo di memoria che non funziona bene
        # Ottieni il consumo di memoria corrente (Windows)
        def memoria_usata():
            process = psutil.Process()
            return process.memory_info().rss / (1024 * 1024)
        
        print(f"Elaborazione file {filename}")    
        # Carica il file .mat
        mat = scipy.io.loadmat(os.path.join(cartella, filename))

        # Accedi alla matrice A all'interno della struttura Problem
        A = mat['Problem'][0,0]['A']

        # stampa matrice: print(A)

        # Converti la matrice in formato CSC
        A = scipy.sparse.csc_matrix(A)

        # misura il tempo di inizio 
        start_time = time.time()  

        # calcola la dimensione della matrice A
        n = A.shape[0]

        # Crea il vettore b di modo che x = [1,1,....,1]
        b = A.dot(np.ones(n))

        # Ottieni la memoria usata prima della fattorizzazione di Cholesky
        memoria_iniziale = memoria_usata()

        # Calcola la decomposizione di Cholesky
        factor = cholmod.cholesky(A)

        # Ottieni la memoria usata dopo la fattorizzazione di Cholesky
        memoria_cholesky.append(memoria_usata() - memoria_iniziale)

        # Risolvi il sistema lineare
        x = factor(b)

        end_time = time.time()

        # Ottieni la memoria usata dopo la risoluzione del sistema
        memoria_risoluzione = memoria_usata() - memoria_cholesky[-1] - memoria_iniziale

        # Calcola la memoria totale utilizzata
        memoria_totale = memoria_cholesky[-1] + memoria_risoluzione + memoria_iniziale

        print("Memoria utilizzata per la fattorizzazione di Cholesky: {:.2f} MB".format(memoria_cholesky[-1]))
        print("Memoria utilizzata per la risoluzione del sistema: {:.2f} MB".format(memoria_risoluzione))

        # terminiamo il timer e stampiamo il risultato        
        tempi_cholesky.append(end_time - start_time)
        nomi_matrici.append(filename)
        print("Tempo impiegato per la decomposizione di Cholesky: {:.4f} secondi".format(end_time - start_time))

        # Stampa il vettore soluzione
        # print(x)

        # Definisci il vettore x_esatto contenente tutti 1
        x_esatto = np.ones(n)

        # Calcola l'errore relativo
        errore_relativo = np.linalg.norm(x - x_esatto) / np.linalg.norm(x_esatto)

        # Stampa il vettore soluzione e l'errore relativo in notazione scientifica
        # print("Soluzione del sistema lineare: ", x)
        print("Errore relativo: {:.4e}".format(errore_relativo))

        # controlla il numero di elementi non nulli nella matrice A
        n_nonzero = A.count_nonzero()
        # calcola il numero totale di elementi nella matrice A
        n_total = A.shape[0] * A.shape[1]

        # calcola la percentuale di elementi nulli
        percent_zero = 100 * (1 - (n_nonzero / n_total))

        print(f"La percentuale di elementi nulli nella matrice A è {percent_zero}%")

        # Conta numeri diversi da 0
        rows, cols = A.nonzero()
        num_nonzeros = len(rows)
        print("Numero di elementi diversi da zero in A: {}".format(num_nonzeros))



# Ordina i tempi di esecuzione in base alla dimensione dei file
tempi_cholesky, memoria_cholesky, nomi_matrici = zip(*sorted(zip(tempi_cholesky, memoria_cholesky, nomi_matrici), key=lambda x: os.path.getsize(os.path.join(cartella, x[2]))))

# Crea il grafico
fig, ax1 = plt.subplots(figsize=(10, 5))

color = 'tab:red'
ax1.set_xlabel('Nome della matrice')
ax1.set_ylabel('Tempo di esecuzione della decomposizione di Cholesky (secondi)', color=color)
ax1.bar(nomi_matrici, tempi_cholesky, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.tick_params(axis='x', rotation=90)

ax2 = ax1.twinx()  # Secondo asse y

color = 'tab:blue'
ax2.set_ylabel('Memoria utilizzata (MB)', color=color)
ax2.plot(nomi_matrici, memoria_cholesky, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()