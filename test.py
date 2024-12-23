import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Fonction de traduction
def translate_text():
    text_to_trans = text_box1.get(1.0, tk.END).strip()
    if not text_to_trans:
        return

    translator = Translator()
    detected_language = translator.detect(text_to_trans).lang
    choix = combo_select.get()

    if choix not in LANGUAGES.values():
        text_box2.delete(1.0, tk.END)
        text_box2.insert(tk.END, "Langue cible non valide.")
        return

    try:
        trans_text = translator.translate(text_to_trans, src=detected_language, dest=choix)
        text_box2.delete(1.0, tk.END)
        text_box2.insert(tk.END, trans_text.text)
    except Exception as e:
        text_box2.delete(1.0, tk.END)
        text_box2.insert(tk.END, f"Erreur de traduction: {e}")

# Création de l'interface
root = tk.Tk()
root.title("Traducteur")
root.geometry("600x400")
root.configure(bg="#f5f5f5")

# Titre
title_label = tk.Label(root, text="Traducteur", font=("Helvetica", 24, "bold"), bg="#4CAF50", fg="white")
title_label.pack(pady=10, fill=tk.X)

# Zone de texte pour l'entrée
text_box1 = tk.Text(root, height=10, wrap=tk.WORD, font=("Helvetica", 12), bg="#ffffff", bd=2, relief=tk.GROOVE)
text_box1.pack(pady=10, padx=10, fill=tk.BOTH)

# Sélecteur de langue
combo_select = ttk.Combobox(root, values=list(LANGUAGES.values()), state="readonly", font=("Helvetica", 12))
combo_select.set("fr")  # Langue par défaut
combo_select.pack(pady=10)

# Bouton de traduction
translate_button = tk.Button(root, text="Traduire", command=translate_text, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
translate_button.pack(pady=10)

# Zone de texte pour l'affichage de la traduction
text_box2 = tk.Text(root, height=10, wrap=tk.WORD, font=("Helvetica", 12), bg="#ffffff", bd=2, relief=tk.GROOVE)
text_box2.pack(pady=10, padx=10, fill=tk.BOTH)

# Lancement de l'application
root.mainloop()