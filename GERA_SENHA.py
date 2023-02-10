import string
import os
import random
import getpass
import tkinter as tk
from tkinter import messagebox


def generate_password(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))


def save_password(username, application, password):
    directory = f"C:/Users/{username}/Documents/Senha"
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(f"{directory}/senha.txt", "a") as file:
        file.write(f"{application}: {password}\n")


def generate_and_save_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "O comprimento da senha deve ser um número inteiro positivo.")
            return
    except ValueError:
        messagebox.showerror("Error", "O comprimento da senha deve ser um número inteiro positivo.")
        return

    option = option_var.get()
    chars = [string.digits, string.ascii_letters, string.ascii_letters + string.digits, string.punctuation + string.ascii_letters + string.digits][option - 1]

    password = generate_password(length, chars)
    password_label["text"] = password

    if save_var.get() == 1:
        application = application_entry.get().strip()
        if not application:
            messagebox.showerror("Error", "Digite o nome do aplicativo.")
            return

        save_password(username, application, password)
        messagebox.showinfo("Sucesso", "Senha salva com sucesso.")


def clear_form():
    length_entry.delete(0, "end")
    option_var.set(1)
    password_label["text"] = ""
    save_var.set(0)
    application_entry.delete(0, "end")


# Tkinter GUI Code
root = tk.Tk()
root.title("Gerador de senhas")

username = getpass.getuser()

length_frame = tk.Frame(root)
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Comprimento da senha:")
length_label.pack(side="left")

length_entry = tk.Entry(length_frame, width=30)
length_entry.pack(side="left")

option_frame = tk.Frame(root)
option_frame.pack(pady=10)

option_label = tk.Label(option_frame, text="Opçôes de senha:")
option_label.pack(side="left")

option_var = tk.IntVar()
option_var.set(1)

option_digits = tk.Radiobutton(option_frame, text="Números", variable=option_var, value=1)
option_digits.pack(side="left")

option_letters = tk.Radiobutton(option_frame, text="Letras", variable=option_var, value=2)
option_letters.pack(side="left")

option_letters_digits = tk.Radiobutton(option_frame, text="Letras e Números", variable=option_var, value=3)
option_letters_digits.pack(side="left")

option_all = tk.Radiobutton(option_frame, text="Letras, Números e Símbolos", variable=option_var, value=4)
option_all.pack(side="left")

password_frame = tk.Frame(root)
password_frame.pack(pady=10)

password_label = tk.Label(password_frame, text="", font=("Courier", 14), width=30, height=2)
password_label.pack(side="left")

save_frame = tk.Frame(root)
save_frame.pack(pady=10)

save_var = tk.IntVar()

save_checkbox = tk.Checkbutton(save_frame, text="Salvar senha", variable=save_var)
save_checkbox.pack(side="left")

application_frame = tk.Frame(root)
application_frame.pack(pady=10)

application_label = tk.Label(application_frame, text="Nome da Aplicação:")
application_label.pack(side="left")

application_entry = tk.Entry(application_frame, width=30)
application_entry.pack(side="left")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Gerar senha", command=generate_and_save_password)
generate_button.pack(side="left", padx=10)

clear_button = tk.Button(button_frame, text="Limpar", command=clear_form)
clear_button.pack(side="left", padx=10)

root.mainloop()
