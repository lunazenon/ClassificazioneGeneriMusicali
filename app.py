import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import pandas as pd
import numpy as np
import joblib
import os
from collections import Counter

ctk.set_appearance_mode("Dark")

BG_MAIN = "#191724"
BG_PANEL = "#1f1d2e"
PASTEL_VIOLET = "#c4a7e7"
PASTEL_HOVER = "#b494db"
PASTEL_GREEN = "#9ccfd8"
TEXT_LIGHT = "#e0def4"
TEXT_MUTED = "#908caa"
BORDER_COLOR = "#403d52"
WARN_COLOR = "#f6c177"


class MusicGenreApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.genre_history = None
        self.genre_map = None
        self.label_encoder = None

        self.load_trained_artifacts()

        self.title("Music Genre Classifier - Artist Lookup")
        self.geometry("900x560")
        self.resizable(False, False)
        self.configure(fg_color=BG_MAIN)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.sidebar_frame = ctk.CTkFrame(self, width=240, corner_radius=0, fg_color=BG_PANEL)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.title_label = ctk.CTkLabel(
            self.sidebar_frame,
            text="TEAMFOUR",
            font=ctk.CTkFont(family="Segoe UI", size=26, weight="bold"),
            text_color=PASTEL_VIOLET
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(35, 40))

        self.mode_label = ctk.CTkLabel(
            self.sidebar_frame,
            text="Modalità:",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color=TEXT_LIGHT
        )
        self.mode_label.grid(row=1, column=0, padx=25, pady=(10, 5), sticky="w")

        self.mode_optionmenu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values=["Lookup artista", "Classificazione assistita"],
            fg_color="#2a283e",
            button_color="#3f3c56",
            button_hover_color="#4e4a6b",
            text_color=TEXT_LIGHT,
            font=ctk.CTkFont(family="Segoe UI", size=12),
            command=self.on_mode_change
        )
        self.mode_optionmenu.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.mode_optionmenu.set("Lookup artista")

        self.status_label = ctk.CTkLabel(
            self.sidebar_frame,
            text="Stato: Verifico dati...",
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            text_color=TEXT_MUTED
        )
        self.status_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.update_status_ui()

        self.info_label = ctk.CTkLabel(
            self.sidebar_frame,
            text="Predizione basata\nsullo storico artista-genere",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=TEXT_MUTED
        )
        self.info_label.grid(row=5, column=0, padx=20, pady=25)

        self.main_frame = ctk.CTkScrollableFrame(self, corner_radius=15, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=25, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.header_label = ctk.CTkLabel(
            self.main_frame,
            text="Predizione genere musicale da artista",
            font=ctk.CTkFont(family="Segoe UI", size=19, weight="bold"),
            text_color=TEXT_LIGHT
        )
        self.header_label.grid(row=0, column=0, padx=10, pady=(10, 12), sticky="w")

        artist_frame = ctk.CTkFrame(self.main_frame, fg_color=BG_PANEL, border_color=PASTEL_VIOLET, border_width=1, corner_radius=10)
        artist_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        artist_frame.grid_columnconfigure(0, weight=1)

        artist_lbl = ctk.CTkLabel(
            artist_frame,
            text="Nome Artista",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            text_color=PASTEL_VIOLET
        )
        artist_lbl.grid(row=0, column=0, sticky="w", padx=15, pady=(8, 2))

        self.artist_entry = ctk.CTkEntry(
            artist_frame,
            placeholder_text="Es: Metallica, Eminem, Röyksopp...",
            fg_color="#26233a",
            border_color=BORDER_COLOR,
            text_color=TEXT_LIGHT,
            placeholder_text_color=TEXT_MUTED
        )
        self.artist_entry.insert(0, "Metallica")
        self.artist_entry.grid(row=1, column=0, padx=15, pady=(2, 12), sticky="ew")

        self.btn_predict = ctk.CTkButton(
            self.main_frame,
            text="🔮 ANALIZZA ARTISTA",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            height=46,
            fg_color=PASTEL_VIOLET,
            hover_color=PASTEL_HOVER,
            text_color="#191724",
            command=self.predict_genre
        )
        self.btn_predict.grid(row=2, column=0, padx=10, pady=16, sticky="ew")

        self.result_frame = ctk.CTkFrame(self.main_frame, height=130, corner_radius=12, border_width=2, border_color=PASTEL_VIOLET, fg_color=BG_PANEL)
        self.result_frame.grid(row=3, column=0, padx=10, pady=8, sticky="ew")
        self.result_frame.grid_propagate(False)
        self.result_frame.grid_rowconfigure(0, weight=1)
        self.result_frame.grid_columnconfigure(0, weight=1)

        self.result_label = ctk.CTkLabel(
            self.result_frame,
            text="In attesa dei dati...",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color=TEXT_MUTED
        )
        self.result_label.pack(expand=True, fill="both", padx=10, pady=10)

        self.detail_label = ctk.CTkLabel(
            self.main_frame,
            text="Lookup artista usa lo storico per restituire il genere più frequente. Classificazione assistita usa il lookup + stima di affidabilità.",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=TEXT_MUTED,
            wraplength=560,
            justify="left"
        )
        self.detail_label.grid(row=4, column=0, padx=12, pady=(4, 12), sticky="w")

    def on_mode_change(self, value):
        if value == "Lookup artista":
            self.btn_predict.configure(text=" ANALIZZA ARTISTA")
        else:
            self.btn_predict.configure(text=" CLASSIFICAZIONE ASSISTITA")

    def load_trained_artifacts(self):
        try:
            if os.path.exists("artist_genre_history.joblib"):
                self.genre_history = joblib.load("artist_genre_history.joblib")
            if os.path.exists("artist_genre_map.joblib"):
                self.genre_map = joblib.load("artist_genre_map.joblib")
            if os.path.exists("label_encoder.joblib"):
                self.label_encoder = joblib.load("label_encoder.joblib")
        except Exception as e:
            print(f"Nota: caricamento artefatti non completato ({e}).")

    def update_status_ui(self):
        if self.genre_map is not None or self.genre_history is not None:
            self.status_label.configure(text="Stato: Storico artista caricato", text_color="#9ccfd8")
        else:
            self.status_label.configure(text="Stato: Nessuno storico trovato", text_color="#eb6f92")

    def _normalize_artist(self, name):
        return str(name).strip().lower()

    def _lookup_genre_from_map(self, artist_name):
        if self.genre_map is None:
            return None, 0, None
        key = self._normalize_artist(artist_name)
        if key not in self.genre_map:
            return None, 0, None
        value = self.genre_map[key]
        if isinstance(value, dict):
            genre = value.get("genre") or value.get("top_genre")
            count = int(value.get("count", 0))
            total = int(value.get("total", max(count, 1)))
            return genre, count, total
        if isinstance(value, (list, tuple)) and len(value) >= 2:
            genre = value[0]
            count = int(value[1])
            total = int(value[2]) if len(value) > 2 else max(count, 1)
            return genre, count, total
        if isinstance(value, str):
            return value, 1, 1
        return None, 0, None

    def _infer_from_history(self, artist_name):
        if self.genre_history is None:
            return None, 0, 0
        if not isinstance(self.genre_history, pd.DataFrame):
            return None, 0, 0
        lower_cols = {c.lower(): c for c in self.genre_history.columns}
        artist_col = None
        genre_col = None
        for cand in ["artist", "artists", "name", "track_artist"]:
            if cand in lower_cols:
                artist_col = lower_cols[cand]
                break
        for cand in ["genre", "track_genre", "label", "class"]:
            if cand in lower_cols:
                genre_col = lower_cols[cand]
                break
        if artist_col is None or genre_col is None:
            return None, 0, 0
        mask = self.genre_history[artist_col].astype(str).str.strip().str.lower() == self._normalize_artist(artist_name)
        subset = self.genre_history.loc[mask, genre_col].dropna().astype(str)
        if subset.empty:
            return None, 0, 0
        counts = Counter(subset)
        genre, count = counts.most_common(1)[0]
        total = len(subset)
        return genre, count, total

    def predict_genre(self):
        try:
            artist_name = self.artist_entry.get().strip()
            if not artist_name:
                raise ValueError("Il campo 'Nome Artista' è obbligatorio.")

            mode = self.mode_optionmenu.get()

            genre = None
            count = 0
            total = 0

            if self.genre_map is not None:
                genre, count, total = self._lookup_genre_from_map(artist_name)

            if genre is None:
                genre, count, total = self._infer_from_history(artist_name)

            if genre is None:
                if mode == "Lookup artista":
                    self.result_label.configure(
                        text=f"Nessun dato trovato per: {artist_name.upper()}\nProva un artista presente nello storico.",
                        text_color=WARN_COLOR
                    )
                else:
                    self.result_label.configure(
                        text=f"Classificazione assistita non disponibile per: {artist_name.upper()}\nArtista non presente nello storico.",
                        text_color=WARN_COLOR
                    )
                return

            confidence = (count / total * 100.0) if total else 0.0
            share_text = f"Occorrenze: {count}/{total}" if total else "Occorrenze: n/d"

            if mode == "Lookup artista":
                text = f"Artista: {artist_name.upper()}\nGenere dominante: {str(genre).upper()}\n{share_text}"
                self.result_label.configure(text=text, text_color=PASTEL_GREEN)
            else:
                text = (
                    f"Artista: {artist_name.upper()}\n"
                    f"Genere stimato: {str(genre).upper()}\n"
                    f"Affidabilità storico: {confidence:.2f}%\n"
                    f"{share_text}"
                )
                self.result_label.configure(text=text, text_color=PASTEL_GREEN if confidence >= 50 else WARN_COLOR)

        except Exception as err:
            messagebox.showerror("Errore nei Dati", f"Controlla i campi inseriti.\n\nDettaglio:\n{err}")


if __name__ == "__main__":
    app = MusicGenreApp()
    app.mainloop()