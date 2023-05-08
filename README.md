# Progetto Metodi del Calcolo Scientifico - Python

> Progetto PYTHON per la risoluzione con il metodo di Choleski di sistemi lineari con matrici sparse e definite positive di grandi dimensioni

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

| Nomi Matrici | Stato | Dimensione (in KB) |
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
