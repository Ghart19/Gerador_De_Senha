# Importação das bibliotecas necessárias
import string
import os
import random
import getpass
import tkinter as tk
from tkinter import messagebox

# Função para gerar uma senha aleatória
def generate_password(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

# Função para salvar a senha em um arquivo
def save_password(username, application, password):
    # Define o diretório onde o arquivo será salvo
    directory = f"C:/Users/{username}/Documents/Senha"
    # Verifica se o diretório existe e, se não existir, cria um novo
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Abre o arquivo para escrita e adiciona a aplicação e a senha
    with open(f"{directory}/senha.txt", "a") as file:
        file.write(f"{application}: {password}\n")

# Função para gerar e salvar a senha
def generate_and_save_password():
    try:
        # Tenta obter o comprimento da senha a partir da entrada "length_entry"
        length = int(length_entry.get())
        # Verifica se o comprimento é um número inteiro positivo
        if length <= 0:
            # Se o comprimento for menor ou igual a zero, mostra uma mensagem de erro
            # e retorna sem fazer mais nada
            messagebox.showerror("Error", "O comprimento da senha deve ser um número inteiro positivo.")
            return
    except ValueError:
        # Se houver um erro ao tentar converter o comprimento para inteiro, mostra
        # uma mensagem de erro e retorna sem fazer mais nada
        messagebox.showerror("Error", "O comprimento da senha deve ser um número inteiro positivo.")
        return

    # Obtém a opção escolhida pelo usuário a partir da variável "option_var"
    option = option_var.get()
    # Define uma lista de caracteres possíveis para a senha, com base na opção escolhida
    chars = [string.digits, string.ascii_letters, string.ascii_letters + string.digits, string.punctuation + string.ascii_letters + string.digits][option - 1]

    # Gera uma senha aleatória com o comprimento e caracteres escolhidos
    password = generate_password(length, chars)
    # Exibe a senha gerada na label "password_label"
    password_label["text"] = password

    # Verifica se o usuário escolheu salvar a senha
    if save_var.get() == 1:
        # Obtém o nome do aplicativo para o qual a senha será usada a partir da entrada "application_entry"
        application = application_entry.get().strip()
        # Verifica se o nome do aplicativo foi fornecido pelo usuário
        if not application:
            # Se o nome do aplicativo não foi fornecido, mostra uma mensagem de erro e retorna sem fazer mais nada
            messagebox.showerror("Error", "Digite o nome do aplicativo.")
            return

        # Salva a senha no armazenamento, associando-a ao usuário e ao nome do aplicativo fornecidos
        save_password(username, application, password)
        # Exibe uma mensagem de sucesso informando que a senha foi salva com sucesso
        messagebox.showinfo("Sucesso", "Senha salva com sucesso.")

# Função para limpar o formulário
def clear_form():
    # Apaga o texto da caixa de entrada de comprimento da senha
    length_entry.delete(0, "end")
    # Define a variável de opções de senha para o valor 1 (primeira opção)
    option_var.set(1)
    # Apaga o texto do rótulo de senha gerada
    password_label["text"] = ""
    # Define a variável de salvamento como 0 (não salva senha gerada)
    save_var.set(0)
    # Apaga o texto da caixa de entrada de aplicação/website
    application_entry.delete(0, "end")


# Código da interface gráfica do usuário usando Tkinter
root = tk.Tk()
root.title("Gerador de senhas")

# Obtém o nome do usuário atual do sistema
username = getpass.getuser()

# Cria um quadro para o comprimento da senha
length_frame = tk.Frame(root)
length_frame.pack(pady=10)

# Cria um rótulo para o comprimento da senha
length_label = tk.Label(length_frame, text="Comprimento da senha:")
length_label.pack(side="left")

# Cria uma caixa de entrada para o comprimento da senha
length_entry = tk.Entry(length_frame, width=30)
length_entry.pack(side="left")

# Cria um quadro para as opções de senha
option_frame = tk.Frame(root)
option_frame.pack(pady=10)

# Cria um rótulo para as opções de senha
option_label = tk.Label(option_frame, text="Opções de senha:")
option_label.pack(side="left")

# Cria uma variável inteira para as opções de senha e define o valor padrão como 1
option_var = tk.IntVar()
option_var.set(1)

# Define o título da janela
root.title("Gerador de senha")

# Cria um frame para as opções de senha
option_frame = tk.Frame(root)
option_frame.pack(pady=10)

# Cria quatro botões de opção para as diferentes combinações de caracteres para a senha
# Cada botão tem um texto, variável e valor diferentes
option_var = tk.IntVar()

option_digits = tk.Radiobutton(option_frame, text="Números", variable=option_var, value=1)
option_digits.pack(side="left")

option_letters = tk.Radiobutton(option_frame, text="Letras", variable=option_var, value=2)
option_letters.pack(side="left")

option_letters_digits = tk.Radiobutton(option_frame, text="Letras e Números", variable=option_var, value=3)
option_letters_digits.pack(side="left")

option_all = tk.Radiobutton(option_frame, text="Letras, Números e Símbolos", variable=option_var, value=4)
option_all.pack(side="left")

# Cria um frame para exibir a senha gerada
password_frame = tk.Frame(root)
password_frame.pack(pady=10)

# Cria um rótulo para exibir a senha gerada
password_label = tk.Label(password_frame, text="", font=("Courier", 14), width=30, height=2)
password_label.pack(side="left")

# Cria um frame para um botão "Salvar"
save_frame = tk.Frame(root)
save_frame.pack(pady=10)

# Cria uma variável para o botão "Salvar"
save_var = tk.IntVar()

# Criando a checkbox para salvar a senha
save_var = tk.BooleanVar()  # Cria uma variável booleana para armazenar o estado da checkbox
save_frame = tk.Frame(root)  # Cria um frame para a checkbox
save_frame.pack()  # Adiciona o frame à janela principal
save_checkbox = tk.Checkbutton(save_frame, text="Salvar senha", variable=save_var)  # Cria a checkbox com o texto "Salvar senha"
save_checkbox.pack(side="left")  # Posiciona a checkbox no lado esquerdo do frame

# Criando um frame para a aplicação
application_frame = tk.Frame(root)  # Cria um frame para a aplicação
application_frame.pack(pady=10)  # Adiciona o frame à janela principal com um espaçamento de 10 pixels

# Adicionando um label e uma entry para o nome da aplicação
application_label = tk.Label(application_frame, text="Nome da Aplicação:")  # Cria um label com o texto "Nome da Aplicação:"
application_label.pack(side="left")  # Posiciona o label no lado esquerdo do frame
application_entry = tk.Entry(application_frame, width=30)  # Cria uma entry com uma largura de 30 caracteres
application_entry.pack(side="left")  # Posiciona a entry ao lado do label

# Criando um frame para os botões
button_frame = tk.Frame(root)  # Cria um frame para os botões
button_frame.pack(pady=10)  # Adiciona o frame à janela principal com um espaçamento de 10 pixels

# Adicionando botões para gerar senha e limpar o formulário
generate_button = tk.Button(button_frame, text="Gerar senha", command=generate_and_save_password)  # Cria um botão com o texto "Gerar senha"
generate_button.pack(side="left", padx=10)  # Posiciona o botão no lado esquerdo do frame com um espaçamento de 10 pixels
clear_button = tk.Button(button_frame, text="Limpar", command=clear_form)  # Cria um botão com o texto "Limpar"
clear_button.pack(side="left", padx=10)  # Posiciona o botão ao lado do botão "Gerar senha" com um espaçamento de 10 pixels

# Iniciando o loop principal da janela
root.mainloop()
