# Progetto Metodi del Calcolo Scientifico - Python

> Progetto PYTHON per la risoluzione con il metodo di Cholesky di sistemi lineari con matrici sparse e definite positive di grandi dimensioni

## Introduzione

Questo Repository contiene il programma Python necessario per completare il progetto di Metdi del Calcolo Scientifico. 
All'interno del progetto vengono utiliizzate le librerie esterne, per la risoluzione di un sistema lineare associato ad una matrice sparsa, simmetrica e definita positiva utilizzando la decomposizione di Cholesky

## Documentazione utilizzata
Link utile per visionare la documentazione delle librerie utilizzate durante l'implementazione del progetto:
- Documentazione Scipy: https://docs.scipy.org/doc/scipy/
- Documentazione Scikit-Sparse: https://scikit-sparse.readthedocs.io/en/latest/

## Note Generali
Il file *mainCalcolo.py* contiene il codice per eseguire la decomposizione di Cholesky e la risoluzione 
del sistema lineare *Ax=b* per gran parte delle matrici richieste dalla consegna. 

### Matrici supportate

Le Matrici simmetriche e definite positive considerate fanno parte della SuiteSparse Matrix Collection che colleziona matrici sparse derivanti da applicazioni di problemi reali 
(ingegneria strutturale, fluidodinamica, elettromagnetismo, termodinamica, computer graphics/vision, network e grafi). Disponibili al seguente link: https://sparse.tamu.edu/

| Matrici | Stato | Dimensione (in KB) |
|-----------|-----------|-----------|
| [ex15.mat](https://sparse.tamu.edu/FIDAP/ex15)  | :white_check_mark:   |  555 |
| [shallow_water1.mat](https://sparse.tamu.edu/MaxPlanck/shallow_water1)    | :white_check_mark:   | 2263 |
| [apache2.mat](https://sparse.tamu.edu/GHS_psdef/apache2)   |:white_check_mark:    | 8302 |
| [parabolic_fem.mat](https://sparse.tamu.edu/Wissgott/parabolic_fem)  | :white_check_mark:    | 13116 |
| [G3_circuit.mat](https://sparse.tamu.edu/AMD/G3_circuit)   | :white_check_mark:    | 13833 |
| [cfd1.mat](https://sparse.tamu.edu/Rothberg/cfd1)   | :white_check_mark:    | 14164 |
| [cfd2.mat](https://sparse.tamu.edu/Rothberg/cfd2)   | :white_check_mark:    | 23192 |
| [StocF-1465.mat](https://sparse.tamu.edu/Janna/StocF-1465)   | Out of memory :x:    | 178368 |
| [Flan_1565.mat](https://sparse.tamu.edu/Janna/Flan_1565)   | Out of Memory :x:    | 292858 |

### Descrizione del programma

Il programma esegue diverse operazioni su una serie di file di matrici sparse e definite positive, con lo scopo di calcolare il tempo di esecuzione e la memoria utilizzata durante la decomposizione di Cholesky e la risoluzione di un sistema lineare *Ax=b*. 
All'interno del programma è possibile trovare diverse funzioni quali: 

* **load_matrix_from_file(filename):** Carica una matrice dal file .mat specificato e la salva nella variabile 'A'. Verifica se la matrice è sparsa e stampa un messaggio di avviso se lo è.
* **create_b_vector(A):** Crea un vettore 'b' a partire dai valori contenuti nella matrice 'A', in modo che la soluzione del sistema lineare sia un vettore 'x' composto interamente da 1.
* **cholesky_decomposition(A):** Esegue la decomposizione di Cholesky della matrice 'A' e calcola la memoria utilizzata durante il processo. Restituisce il fattore di Cholesky e la memoria utilizzata.
* **solve_linear_system(factor, b)**: Risolve il sistema lineare Ax=b utilizzando il fattore di Cholesky calcolato in precedenza e il vettore 'b'. Calcola anche la memoria utilizzata durante il processo.
* **compute_relative_error(x):** Calcola l'errore relativo della soluzione 'x' del sistema lineare confrontato con un vettore 'xEsatto' composto da tutti 1.
* **compute_percent_zeros(A):** Calcola la percentuale di elementi uguali a 0 nella matrice 'A'.
* **compute_num_nonzeros(A):** Calcola il numero di elementi diversi da 0 presenti nella matrice 'A'.
* **compute_filesize(filename):** Calcola la dimensione del file .mat specificato.
* **process_file(filename):** Carica il file di matrice specificato, esegue le operazioni necessarie per calcolare la soluzione del problema e restituisce il tempo di esecuzione, l'errore relativo, la percentuale di elementi nulli, il numero di elementi non nulli, la memoria totale utilizzata e la dimensione del file.

Prima di eseguire il programma, è necessario importare alcune librerie tra cui:
* **SciPy**: libreria open-source per la computazione scientifica e tecnica in Python.  SciPy si basa su NumPy, un'altra libreria Python per il calcolo scientifico. Nel programma vengono utilizzate alcune sottolibrerie tra cui:
  * scipy.io: Fornisce funzioni per leggere e scrivere dati da file in diversi formati, come MATLAB (.mat) e file di testo.
  * scipy.sparse: Offre strutture dati e algoritmi per lavorare con matrici sparse, che sono matrici con molti elementi nulli. Questa sottolibreria fornisce metodi efficienti per la manipolazione, la fattorizzazione e la risoluzione di sistemi lineari sparsi.
  * scipy.linalg: Fornisce funzioni per operazioni lineari algebriche, come calcolo degli autovalori e autovettori, risoluzione di sistemi lineari, decomposizione di matrici e altro ancora.
* **SciKit-Sparse**: fornisce un'interfaccia per utilizzare le funzionalità di CHOLMOD, una libreria di algebra lineare sparse e decomposizione di Cholesky. La sottolibreria usata nel programma è **sksparse.cholmod** che consente di creare oggetti di matrice sparsa, eseguire operazioni algebriche su di esse e sfruttare le capacità di CHOLMOD per decomporre matrici sparse, risolvere sistemi lineari e svolgere altre operazioni di algebra lineare avanzate. 
