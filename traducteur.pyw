import tkinter as tk
import customtkinter as ctk
import googletrans
from googletrans import Translator, LANGUAGES
from deep_translator import GoogleTranslator
from tkinter import ttk

ctk.set_appearance_mode("ligth")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("F-FRANCK - Translator")
root.geometry("900x500+350+160")
root.config(bg="white")

# change label
def change_label():
    changer = combo_select.get()
    show_lang.configure(text=changer)
    root.after(1000, change_label)



# traduire le texte
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


# our color var
first_green = "#2cc985"
secong_green = "#0c955a"




title_lbl =ctk.CTkLabel(master=root, text="F-FRANCK - Translator App",
                        bg_color="green", font=("bold",25))
title_lbl.pack(pady=35)

# Sélecteur de langue
combo_select = ttk.Combobox(root, values=list(LANGUAGES.values()), state="readonly", font=("Helvetica", 25))
combo_select.set("fr")  # Langue par défaut
combo_select.pack(pady=20)


# combo box select language
# combo_select = ctk.CTkComboBox(master=root, button_color=first_green, border_color=secong_green,
#                                 button_hover_color=secong_green,
#                                 values=langage_value, bg_color="blue",state="read" )


combo_select.pack(pady=5)
combo_select.set("Select Language")

show_lang = ctk.CTkLabel(master=root, bg_color="white", font=("Helvitica",25,"bold"))
show_lang.pack(pady=10)

# our text frame

text_frame = tk.Frame(root, bg="white")
text_frame.pack(padx=10)

text_box1 = ctk.CTkTextbox(text_frame, border_width=2,font=("Helvitica",20,"bold"),
                            text_color= "black",border_color="#121212",width=370,height=200,fg_color="#ffffff")
text_box1.grid(row=0, column = 0, padx = 15)

text_box2 = ctk.CTkTextbox(text_frame, border_width=2,font=("Helvitica",20,"bold"),
                            text_color= "black",border_color="#121212",width=370,height=200,fg_color="#ffffff")
text_box2.grid(row=0, column = 1, padx = 15)

# translate btn
translate_btn = ctk.CTkButton(root, text="Translate", command=translate_text)
translate_btn.pack(padx=15,pady=20)

change_label()
root.mainloop()








   