# from googletrans import Translator

# translator = Translator()
# try:
#     translated = translator.translate('Bonjour', src='fr', dest='en')
#     print(translated.text)
# except Exception as e:
#     print(f"Une erreur est survenue: {e}")

import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def translate_text():
    text_to_trans = text_box1.get(1.0, tk.END).strip()
    if not text_to_trans:
        return

    translator = Translator()
    detected_language = translator.detect(text_to_trans).lang
    target_language = language_combo.get()

    if target_language not in LANGUAGES.values():
        text_box2.delete(1.0, tk.END)
        text_box2.insert(tk.END, "Langue cible non valide.")
        return

    try:
        trans_text = translator.translate(text_to_trans, src=detected_language, dest=target_language)
        text_box2.delete(1.0, tk.END)
        text_box2.insert(tk.END, trans_text.text)
    except Exception as e:
        text_box2.delete(1.0, tk.END)
        text_box2.insert(tk.END, f"Erreur de traduction: {e}")

# Création de l'interface
root = tk.Tk()
root.title("MyKELASI - Translator APP")
root.geometry("600x400")
root.configure(bg="#ffffff")

# En-tête
header = tk.Label(root, text="MyKELASI - Translator APP", font=("Helvetica", 18, "bold"), bg="#4CAF50", fg="white")
header.pack(pady=10, fill=tk.X)

# Sélecteur de langue
language_combo = ttk.Combobox(root, values=list(LANGUAGES.values()), state="readonly", font=("Helvetica", 12))
language_combo.set("Select Language")  # Sélection par défaut
language_combo.pack(pady=10)

# Zone de texte pour l'entrée
text_box1 = tk.Text(root, height=10, wrap=tk.WORD, font=("Helvetica", 12), bg="#f0f0f0", bd=2, relief=tk.GROOVE)
text_box1.pack(pady=10, padx=10, fill=tk.BOTH)

# Bouton de traduction
translate_button = tk.Button(root, text="Translate", command=translate_text, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
translate_button.pack(pady=10)

# Zone de texte pour l'affichage de la traduction
text_box2 = tk.Text(root, height=10, wrap=tk.WORD, font=("Helvetica", 12), bg="#f0f0f0", bd=2, relief=tk.GROOVE)
text_box2.pack(pady=10, padx=10, fill=tk.BOTH)

# Lancement de l'application
root.mainloop()