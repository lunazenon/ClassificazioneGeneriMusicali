# Music Genre Classification

Machine Learning project developed by **Giuseppe Cristiano, Antonella Franza, Laura Novellino, and Luana Uda**.

- Giuseppe Cristiano: https://www.linkedin.com/in/giuseppe-cristiano-538463403/
- Antonella Franza: https://www.linkedin.com/in/antonella-franza-8522a4373/
- Laura Novellino: https://www.linkedin.com/in/laura-novellino-113899168/
- Luana Uda: https://www.linkedin.com/in/luana-uda-636406211/

---

**A Machine Learning project designed to classify more than 50,000 music tracks into their corresponding genres using audio features.**

By leveraging quantitative features such as **danceability**, **energy**, and **acousticness**, the system predicts the correct musical genre. The project combines exploratory data analysis, advanced modeling techniques, and a graphical user interface for practical usage.

## Features

- **Exploratory Data Analysis (EDA).**
  Statistical analysis, correlation study, and outlier management.

- **Data Preprocessing.**
  Record cleaning, label encoding, and removal of irrelevant features.

- **Advanced Modeling.**
  Comparison of Decision Tree, Random Forest, and LightGBM models with hyperparameter optimization using Optuna.

- **Interactive GUI.**
  Desktop application developed with CustomTkinter for artist lookup and genre prediction.

## Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Repository Structure

The repository contains the following components:

- `classificazione_generi_musicali.ipynb`

  Jupyter Notebook containing the complete analysis, preprocessing, and training pipeline.

- `app.py`

  Desktop application with a dark interface used to test the trained model and perform artist-based genre prediction.

- `music_genre.csv`

  Dataset containing tracks and audio metadata used for model training.

- `requirements.txt`

  List of Python dependencies required to reproduce the project environment.

- `Documentazione.pdf`

  Technical report describing the project timeline, methodology, and task distribution among team members.

## Workflow

The project follows four main stages.

### 1. Exploratory Data Analysis

Statistical analysis of the dataset, feature distributions, correlation analysis, and outlier handling.

### 2. Data Preprocessing

Cleaning records, encoding labels, and removing unnecessary columns to improve model performance.

### 3. Advanced Modeling

Comparison among:

- Decision Tree
- Random Forest
- LightGBM

Hyperparameter optimization was performed using **Optuna** to maximize predictive accuracy.

### 4. Graphical User Interface

Development of an interactive desktop application using **CustomTkinter**, enabling users to search for artists and estimate the corresponding music genre.

## Goal

The project demonstrates how proper data preparation and model optimization can achieve high predictive accuracy in music genre classification.

By combining analytical rigor, algorithm optimization, and a practical interface, the project provides a complete end-to-end Machine Learning application.

---

# Classificazione dei Generi Musicali

Progetto di Machine Learning sviluppato da **Giuseppe Cristiano, Antonella Franza, Laura Novellino e Luana Uda**.

- Giuseppe Cristiano: https://www.linkedin.com/in/giuseppe-cristiano-538463403/
- Antonella Franza: https://www.linkedin.com/in/antonella-franza-8522a4373/
- Laura Novellino: https://www.linkedin.com/in/laura-novellino-113899168/
- Luana Uda: https://www.linkedin.com/in/luana-uda-636406211/

---

**Un progetto di Machine Learning progettato per classificare oltre 50.000 brani musicali nel rispettivo genere utilizzando caratteristiche audio quantitative.**

Sfruttando feature come **danceability**, **energy** e **acousticness**, il sistema è in grado di predire correttamente il genere musicale. Il progetto integra analisi esplorativa dei dati, modellazione avanzata e un'interfaccia grafica per l'utilizzo pratico.

## Caratteristiche

- **Analisi Esplorativa dei Dati (EDA).**

  Studio statistico, analisi delle correlazioni e gestione degli outlier.

- **Preprocessing dei Dati.**

  Pulizia dei record, codifica delle etichette e rimozione delle variabili non rilevanti.

- **Modellazione Avanzata.**

  Confronto tra Decision Tree, Random Forest e LightGBM con ottimizzazione tramite Optuna.

- **Interfaccia Grafica.**

  Applicazione desktop sviluppata con CustomTkinter per la ricerca degli artisti e la stima del genere.

## Installazione

Installare le dipendenze del progetto tramite:

```bash
pip install -r requirements.txt
```

## Struttura del Repository

Il repository contiene i seguenti componenti:

- `classificazione_generi_musicali.ipynb`

  Notebook Jupyter contenente l'intera pipeline di analisi, preprocessing e addestramento.

- `app.py`

  Applicazione desktop con interfaccia scura per testare il modello e stimare il genere musicale tramite ricerca dell'artista.

- `music_genre.csv`

  Dataset contenente tracce e metadati audio utilizzati durante l'addestramento.

- `requirements.txt`

  Elenco delle librerie Python necessarie per riprodurre l'ambiente di sviluppo.

- `Documentazione.pdf`

  Relazione tecnica che descrive le attività svolte e la suddivisione dei compiti tra i membri del team.

## Workflow

Il progetto si sviluppa attraverso quattro fasi principali.

### 1. Analisi Esplorativa dei Dati

Studio statistico del dataset, distribuzione delle feature, analisi delle correlazioni e gestione degli outlier.

### 2. Preprocessing dei Dati

Pulizia dei record, codifica delle etichette e rimozione delle colonne non necessarie.

### 3. Modellazione Avanzata

Confronto tra:

- Decision Tree
- Random Forest
- LightGBM

Ottimizzazione degli iperparametri tramite **Optuna** per massimizzare l'accuratezza predittiva.

### 4. Interfaccia Grafica

Sviluppo di una GUI interattiva tramite **CustomTkinter**, che permette la ricerca degli artisti e la stima del genere musicale.

## Obiettivo

Il progetto dimostra come una corretta preparazione dei dati e l'ottimizzazione dei modelli consentano di ottenere un'elevata accuratezza nella classificazione dei generi musicali.

L'unione tra rigore analitico, ottimizzazione algoritmica e una semplice interfaccia grafica rende il progetto una soluzione completa end-to-end di Machine Learning.

