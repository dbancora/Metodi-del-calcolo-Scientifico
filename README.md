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

| Matrici | Stato | Dimensione (in MB) |
|-----------|-----------|-----------|
| [ex15.mat](https://sparse.tamu.edu/FIDAP/ex15)  | :white_check_mark:   |  0,555 |
| [shallow_water1.mat](https://sparse.tamu.edu/MaxPlanck/shallow_water1)    | :white_check_mark:   | 2,263 |
| [apache2.mat](https://sparse.tamu.edu/GHS_psdef/apache2)   |:white_check_mark:    | 8,302 |
| [parabolic_fem.mat](https://sparse.tamu.edu/Wissgott/parabolic_fem)  | :white_check_mark:    | 13,116 |
| [G3_circuit.mat](https://sparse.tamu.edu/AMD/G3_circuit)   | :white_check_mark:    | 13,833 |
| [cfd1.mat](https://sparse.tamu.edu/Rothberg/cfd1)   | :white_check_mark:    | 14,164 |
| [cfd2.mat](https://sparse.tamu.edu/Rothberg/cfd2)   | :white_check_mark:    | 23,192 |
| [StocF-1465.mat](https://sparse.tamu.edu/Janna/StocF-1465)   | Out of memory :x:    | 178,368 |
| [Flan_1565.mat](https://sparse.tamu.edu/Janna/Flan_1565)   | Out of Memory :x:    | 292,858 |

## Descrizione del programma

Il programma esegue diverse operazioni su una serie di file che contengono matrici sparse e definite positive, con lo scopo di calcolare il tempo di esecuzione, la memoria utilizzata e l'errore relativo, tra la soluzione calcolata e quella esatta, durante la decomposizione di Cholesky e la risoluzione di un sistema lineare *Ax=b*. 
All'interno del programma è possibile trovare diverse funzioni quali: 

* **load_matrix_from_file(filename):** Carica una matrice dal file .mat specificato e la salva nella variabile 'A'. Verifica se la matrice è sparsa e stampa un messaggio di avviso se lo è.
* **is_symmetric(A):** Verifica se una matrice A è simmetrica controllando se i valori non nulli della matrice sono gli stessi dei valori non nulli della sua trasposta. La funzione inizia calcolando la trasposta della matrice A utilizzando il metodo *transpose* fornito da NumPy. Successivamente, viene confrontato l'array *data* di *A* (che contiene i valori non nulli della matrice) con l'array *data* della sua trasposta. La funzione *np.all* restituisce _True_ solo se tutti gli elementi degli array sono uguali, verificando così che la matrice è simmetrica. 
* **create_b_vector(A):** Crea un vettore 'b' a partire dai valori contenuti nella matrice 'A', in modo che la soluzione del sistema lineare sia un vettore 'x' composto interamente da 1.
* **cholesky_decomposition(A):** Esegue la decomposizione di Cholesky della matrice 'A' e calcola la memoria utilizzata durante il processo. Restituisce il fattore di Cholesky e la memoria utilizzata.
* **solve_linear_system(factor, b)**: Risolve il sistema lineare Ax=b utilizzando il fattore di Cholesky calcolato in precedenza e il vettore 'b'. Calcola anche la memoria utilizzata durante il processo.
* **compute_relative_error(x):** Calcola l'errore relativo della soluzione 'x' del sistema lineare confrontato con un vettore 'xEsatto' composto da tutti 1.
* **compute_percent_zeros(A):** Calcola la percentuale di elementi uguali a 0 nella matrice 'A'.
* **compute_num_nonzeros(A):** Calcola il numero di elementi diversi da 0 presenti nella matrice 'A'.
* **compute_filesize(filename):** Calcola la dimensione del file .mat specificato.
* **process_file(filename):** Carica il file di matrice specificato, esegue le operazioni necessarie per calcolare la soluzione del problema e restituisce il tempo di esecuzione, l'errore relativo, la percentuale di elementi nulli, il numero di elementi non nulli, la memoria totale utilizzata e la dimensione del file.

## Librerie utilizzate
Per completare il progetto ed affrontare il problema di risolvere il sistema lineare *Ax=b*, è stato necessario utilizzare diverse librerie open-source in Python. L'obiettivo era manipolare le matrici sparse definite, evitando la conversione in matrici dense che avrebbe comportato un eccessivo utilizzo delle risorse del sistema.

Le librerie open-source riportate di swguito, sono state scelte per la loro affidabilità, flessibilità e popolarità nella comunità Python. 
Consentono di gestire in modo efficiente le matrici sparse e risolvere sistemi lineari in modo rapido ed efficiente, evitando l'esaurimento delle risorse della macchina.

L'utilizzo di librerie open-source come queste, offre un'alternativa accessibile e potente rispetto ai software a pagamento, consentendo alle aziende con risorse finanziarie limitate di affrontare problemi complessi senza dover sostenere costi elevati.

### SciPy
E' una libreria open-source per la computazione scientifica e tecnica in Python.  SciPy si basa su NumPy, un'altra libreria Python per il calcolo scientifico. Nel programma vengono utilizzate alcune sottolibrerie tra cui:
  * scipy.io: Fornisce funzioni per leggere e scrivere dati da file in diversi formati, come MATLAB (.mat) e file di testo.
  * scipy.sparse: Offre strutture dati e algoritmi per lavorare con matrici sparse, che sono matrici con molti elementi nulli. Questa sottolibreria fornisce metodi efficienti per la manipolazione, la fattorizzazione e la risoluzione di sistemi lineari sparsi.
  * scipy.linalg: Fornisce funzioni per operazioni lineari algebriche, come calcolo degli autovalori e autovettori, risoluzione di sistemi lineari, decomposizione di matrici e altro ancora.

La documentazione della libreria è presente al sito https://docs.scipy.org/doc/scipy/ e contiene tutte le informazioni necessarie per l'installazione e per l'utilizzo dei metodi utili per il progetto. In particolare, il link è diviso in 4 sezioni:
* *Getting Started* che contiene le informazioni per l'installazione della libreria e i tutorial utili per scrivere il codice. 
* *User guide*  è una sezione che fornisce una panoramica completa e dettagliata sulle funzionalità offerte dalla libreria SciPy. Fornisce esempi pratici, spiegazioni concettuali e istruzioni passo-passo su come utilizzare le varie funzioni e moduli. Utile per gli utenti che desiderano imparare ad utilizzare SciPy o che vogliono approfondire la loro conoscenza della libreria
* *Api Reference*  è una sezione che fornisce una documentazione tecnica dettagliata sull'interfaccia di programmazione (API) di SciPy. In questa sezione sono elencati tutti i moduli, le classi, le funzioni e gli attributi disponibili insieme alle loro firme, descrizioni e parametri. L'API Reference è pensata per gli sviluppatori che desiderano utilizzare SciPy come libreria e hanno bisogno di informazioni precise sulle funzioni e sulle loro modalità di utilizzo.
* *Developer Guide* contiene le informazioni utili per contribuire al progetto open source. Vengono indicati quali sono i bug noti, e la roadmap per implementare le nuove funzionalità pianificate. 
L'ultimo aggiornamento della libreria risale a Febbraio 2023 ma, osservando il progetto contenuto su GitHub, è facile notare che gli autori continuano ad aggiornare la libreria. 

### SciKit-Sparse
E' una libreria opensource e fornisce un'interfaccia per utilizzare le funzionalità di CholMod una libreria di algebra lineare sparse e decomposizione di Cholesky. La sottolibreria usata nel programma è **sksparse.cholmod** che consente di creare oggetti di matrice sparsa, eseguire operazioni algebriche su di esse e sfruttare le capacità di CHOLMOD per decomporre matrici sparse, risolvere sistemi lineari e svolgere altre operazioni di algebra lineare avanzate. 

La documentazione è disponibile al sito https://scikit-sparse.readthedocs.io/en/latest/ ed è divisa in varie sezioni tra cui:
* *Overview* che contiene link utili per l'installazione della libreria, le informazioni generali e i contatti degli sviluppatori. E' inoltre presente una sezione specifica per i requisiti necessari per il corretto funzionamento della libreria e questi comprendono NumPy, SciPy (vedi sopra), Cython e CHOLMOD (incluso in SuiteSparse). 
* *Sparse.cholmod* contiene le informazioni relative per l'utilizzo dei metodi per la decomposizione di Cholesky psu matrici sparse. E' disponibile una sezione relativa agli errori che possono verificarsi durante l'utilizzo della funzione. 
* *Changes* contiene tutte le versioni della libreria che sono state distribuite: per ognuna di queste è possibile verificare il changelog delle funzionalità. 

Osservando la pagina ufficiale della libreria, si trova un link di riferimento alla pagina GitHub del progetto. L'ultima release risale a novembre 2022 e, attualmente, non sono disponibili nuovi aggiornamenti; anche osservando i singoli file della libreria, non si notano nuovi push. 

### NumPy
NumPy è una libreria open-source per il linguaggio di programmazione Python, che fornisce supporto per l'elaborazione efficiente di array multidimensionali. È ampiamente utilizzata nel campo della computazione scientifica, data manipulation e machine learning. E' stata utilizzata nel progetto per manipolare array  multidimensionali pur non essendo strattamente legata alla manipolazione delle matrici sparse. In particolare, nel nostro programma, viene utilizzata:
* per calcolare la trasposta della matrice e verificare se ques'ultima è simmetrica con la matrice A data in input. 
* per creare un vettore *x_esatto*, utile per calcolare l'errore relativo. 
* per creare il vettore *b*, utile per la riosoluzione del sistema lineare *Ax=b* 

Inoltre, la libreria è necessaria per il funzionamento di *SciPy* e *SciKit-Sparse*. Di fatto è ampiamente utilizzato come base per molte altre librerie scientifiche in Python per eseguire oprazioni su array multidimensionali. 
La documentazione della libreria è disponibile al sito https://numpy.org/doc/stable/ e la struttura del sito è analoga a quella descritta in SciPy. Quest'ultima dipende strettamente da NumPy per le ragioni sopradescritte. 


