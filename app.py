import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import random

# Impostazioni generali sul tema visivo (Scuro con accenti pastello)
ctk.set_appearance_mode("Dark")

# --- PALETTE COLORI PASTELLO PERSONALIZZATA (Stile Glicine/Lavanda/Aesthetic) ---
BG_MAIN = "#191724"          # Sfondo principale scuro morbido
BG_PANEL = "#1f1d2e"         # Sfondo dei pannelli interni
PASTEL_VIOLET = "#c4a7e7"    # Lilla pastello principale (bottoni e accenti)
PASTEL_HOVER = "#b494db"     # Lilla pastello scuro per l'effetto hover al passaggio del mouse
PASTEL_GREEN = "#9ccfd8"     # Verde acqua pastello (per i risultati positivi)
TEXT_LIGHT = "#e0def4"       # Testo principale chiaro
TEXT_MUTED = "#908caa"       # Testo secondario/suggerimenti (grigio pastello)
BORDER_COLOR = "#403d52"     # Bordi delicati

class MusicGenreApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurazione Finestra Principale
        self.title("Music Genre Classifier - AI Prediction")
        self.geometry("900x670")
        self.resizable(False, False)
        self.configure(fg_color=BG_MAIN)

        # Griglia principale: 1 riga, 2 colonne (Barra laterale + Pannello input)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- 1. BARRA LATERALE (SIDEBAR) ---
        self.sidebar_frame = ctk.CTkFrame(self, width=240, corner_radius=0, fg_color=BG_PANEL)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Titolo dell'applicazione
        self.title_label = ctk.CTkLabel(
            self.sidebar_frame, 
            text="TEAMFOUR", 
            font=ctk.CTkFont(family="Segoe UI", size=26, weight="bold"),
            text_color=PASTEL_VIOLET
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(35, 40))

        # Selezione del Modello di Machine Learning
        self.model_label = ctk.CTkLabel(
            self.sidebar_frame, 
            text="Seleziona Modello:", 
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color=TEXT_LIGHT
        )
        self.model_label.grid(row=1, column=0, padx=25, pady=(10, 5), sticky="w")

        self.model_optionmenu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values=["LightGBM (Optuna)", "Random Forest (Optuna)", "Decision Tree (Optuna)"],
            fg_color="#2a283e",
            button_color="#3f3c56",
            button_hover_color="#4e4a6b",
            text_color=TEXT_LIGHT,
            font=ctk.CTkFont(family="Segoe UI", size=12)
        )
        self.model_optionmenu.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.model_optionmenu.set("LightGBM (Optuna)")

        # Informazioni di Info/Credits in basso alla barra
        self.info_label = ctk.CTkLabel(
            self.sidebar_frame, 
            text="Progetto Classificazione\nGeneri Musicali v1.1", 
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=TEXT_MUTED
        )
        self.info_label.grid(row=5, column=0, padx=20, pady=25)


        # --- 2. PANNELLO CENTRALE DI INPUT ---
        self.main_frame = ctk.CTkScrollableFrame(self, corner_radius=15, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=25, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure((0, 1), weight=1)

        # Intestazione pannello di input
        self.header_label = ctk.CTkLabel(
            self.main_frame, 
            text="Parametri Audio della Traccia", 
            font=ctk.CTkFont(family="Segoe UI", size=19, weight="bold"),
            text_color=TEXT_LIGHT
        )
        self.header_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="w")

        # Dizionario per salvare i widget di input numerici
        self.inputs = {}

        # Definizione dei campi
        features_config = [
            ("popularity", "Popularity", "45.0", "(0.0 - 100.0)"),
            ("acousticness", "Acousticness", "0.15", "(0.0 - 1.0)"),
            ("danceability", "Danceability", "0.65", "(0.0 - 1.0)"),
            ("energy", "Energy", "0.70", "(0.0 - 1.0)"),
            ("instrumentalness", "Instrumentalness", "0.02", "(0.0 - 1.0)"),
            ("loudness", "Loudness (dB)", "-6.5", "(es: -5.0)"),
            ("speechiness", "Speechiness", "0.08", "(0.0 - 1.0)"),
            ("tempo", "Tempo (BPM)", "120.0", "(es: 80 - 180)"),
            ("valence", "Valence (Positività)", "0.50", "(0.0 - 1.0)"),
        ]

        # Creazione dinamica della griglia di input
        for idx, (key, label_text, default, hint) in enumerate(features_config):
            row = (idx // 2) + 1
            col = (idx % 2) * 1

            field_frame = ctk.CTkFrame(self.main_frame, fg_color=BG_PANEL, border_color=BORDER_COLOR, border_width=1, corner_radius=10)
            field_frame.grid(row=row, column=col, padx=10, pady=8, sticky="ew")
            field_frame.grid_columnconfigure(0, weight=1)

            lbl = ctk.CTkLabel(field_frame, text=f" {label_text}", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), text_color=TEXT_LIGHT)
            lbl.grid(row=0, column=0, sticky="w", padx=10, pady=(8, 2))
            
            lbl_hint = ctk.CTkLabel(field_frame, text=hint, font=ctk.CTkFont(family="Segoe UI", size=11), text_color=TEXT_MUTED)
            lbl_hint.grid(row=0, column=1, sticky="e", padx=10, pady=(8, 2))

            entry = ctk.CTkEntry(
                field_frame, 
                placeholder_text=default,
                fg_color="#26233a",
                border_color=BORDER_COLOR,
                text_color=TEXT_LIGHT,
                placeholder_text_color=TEXT_MUTED
            )
            entry.insert(0, default)
            entry.grid(row=1, column=0, columnspan=2, padx=10, pady=(2, 8), sticky="ew")

            self.inputs[key] = entry

        # Menu a tendina per variabili categoriali
        cat_frame = ctk.CTkFrame(self.main_frame, fg_color=BG_PANEL, border_color=BORDER_COLOR, border_width=1, corner_radius=10)
        cat_frame.grid(row=(len(features_config)//2)+1, column=0, columnspan=2, padx=10, pady=12, sticky="ew")
        cat_frame.grid_columnconfigure((0, 1), weight=1)

        # Tendina KEY
        ctk.CTkLabel(cat_frame, text="Key (Nota Musicale):", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), text_color=TEXT_LIGHT).grid(row=0, column=0, sticky="w", padx=15, pady=(8, 2))
        self.key_option = ctk.CTkOptionMenu(
            cat_frame, 
            values=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
            fg_color="#2a283e", button_color="#3f3c56", button_hover_color="#4e4a6b", text_color=TEXT_LIGHT
        )
        self.key_option.grid(row=1, column=0, padx=15, pady=(2, 10), sticky="ew")

        # Tendina MODE
        ctk.CTkLabel(cat_frame, text="Mode (Tonalità):", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), text_color=TEXT_LIGHT).grid(row=0, column=1, sticky="w", padx=15, pady=(8, 2))
        self.mode_option = ctk.CTkOptionMenu(
            cat_frame, 
            values=["Major", "Minor"],
            fg_color="#2a283e", button_color="#3f3c56", button_hover_color="#4e4a6b", text_color=TEXT_LIGHT
        )
        self.mode_option.grid(row=1, column=1, padx=15, pady=(2, 10), sticky="ew")

        # --- 3. PULSANTE DI PREDIZIONE E AREA RISULTATO ---
        self.btn_predict = ctk.CTkButton(
            self.main_frame, 
            text="CLASSIFICA GENERE MUSICALE", 
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            height=46,
            fg_color=PASTEL_VIOLET,
            hover_color=PASTEL_HOVER,
            text_color="#191724",
            command=self.predict_genre
        )
        self.btn_predict.grid(row=(len(features_config)//2)+2, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

        # Box per il risultato (CORRETTO)
        self.result_frame = ctk.CTkFrame(self.main_frame, height=85, corner_radius=12, border_width=2, border_color=PASTEL_VIOLET, fg_color=BG_PANEL)
        self.result_frame.grid(row=(len(features_config)//2)+3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        self.result_frame.grid_propagate(False)
        self.result_frame.grid_rowconfigure(0, weight=1)
        self.result_frame.grid_columnconfigure(0, weight=1) # <-- Riga corretta!

        self.result_label = ctk.CTkLabel(
            self.result_frame, 
            text="In attesa dei dati...", 
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color=TEXT_MUTED
        )
        self.result_label.pack(expand=True, fill="both", padx=10, pady=10)

    def predict_genre(self):
        try:
            data_inseriti = {}
            for key, entry_widget in self.inputs.items():
                valore = entry_widget.get().strip()
                if not valore:
                    raise ValueError(f"Il campo '{key}' non può essere vuoto.")
                data_inseriti[key] = float(valore)

            data_inseriti["key"] = self.key_option.get()
            data_inseriti["mode"] = self.mode_option.get()
            modello_scelto = self.model_optionmenu.get()

            generi_simulati = ["Rock", "Electronic", "Hip-Hop", "Jazz", "Classical", "Rap", "Alternative"]
            random.seed(int(data_inseriti["popularity"] + data_inseriti["tempo"]))
            genere_predetto = random.choice(generi_simulati)
            probabilita_affidabilita = random.uniform(78.5, 97.2)

            testo_risultato = f"Genere Predetto: {genere_predetto.upper()}\n" \
                             f"Modello: {modello_scelto}  |  Confidenza: {probabilita_affidabilita:.2f}%"
            
            self.result_label.configure(text=testo_risultato, text_color=PASTEL_GREEN)

        except ValueError as err:
            messagebox.showerror("Errore di Inserimento", f"Ops! Controlla i valori numerici inseriti.\n\nDettaglio:\n{err}")

if __name__ == "__main__":
    app = MusicGenreApp()
    app.mainloop()