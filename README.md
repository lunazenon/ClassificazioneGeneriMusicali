# ClassificazioneGeneriMusicali
Classificazione dei Generi Musicali
Progetto di: Giuseppe Cristiano, Antonella Franza, Laura Novellino, Luana Uda

https://www.linkedin.com/in/giuseppe-cristiano-538463403/
https://www.linkedin.com/in/antonella-franza-8522a4373/
https://www.linkedin.com/in/laura-novellino-113899168/
https://www.linkedin.com/in/luana-uda-636406211/

Questo progetto sviluppa un modello di Machine Learning per classificare il genere di oltre 50.000 brani musicali.
Sfruttando feature quantitative come danceability, energy e acousticness, il sistema predice la categoria corretta.
Il flusso di lavoro si articola in quattro fasi principali condotte in modo collaborativo dal team di sviluppo:
1. Analisi Esplorativa (EDA): Studio statistico del dataset, analisi delle correlazioni e gestione degli outlier.
2. Preprocessing dei Dati: Pulizia dei record, codifica delle etichette e rimozione delle colonne non utili.
3. Modellazione Avanzata: Confronto tra algoritmi (Decision Tree, Random Forest, LightGBM) e tuning con Optuna.
4. Interfaccia Grafica: Sviluppo di una GUI interattiva in CustomTkinter per il lookup e la stima del genere.
Il repository include i seguenti componenti fondamentali per riprodurre interamente l'esperimento:
* `classificazione_generi_musicali.ipynb`: Notebook Jupyter contenente la pipeline completa di analisi e training.
* `app.py`: Codice dell'applicazione desktop scura per testare i risultati del modello tramite ricerca per artista.
* `music_genre.csv`: Il dataset strutturato contenente le tracce e i metadati audio usati per l'addestramento.
* `Documentazione...pdf`: Relazione tecnica che traccia la cronologia delle attività e la suddivisione dei ruoli.
L'obiettivo finale dimostra come una corretta preparazione del dato garantisca un'alta accuratezza predittiva.
Il progetto unisce rigore analitico, ottimizzazione algoritmica e un'applicazione pratica facilmente fruibile.