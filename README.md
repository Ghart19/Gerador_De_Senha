# Gerador_De_Senha
Este é um script Python que gera e salva senhas usando uma interface gráfica do usuário (GUI) criada com a biblioteca Tkinter.

A GUI tem os seguintes componentes:

- Um campo para inserir o tamanho da senha desejada.
- Botões de opção para selecionar opções de senha (dígitos, letras, letras e dígitos ou letras, dígitos e símbolos).
- Um rótulo que exibe a senha gerada.
- Uma caixa de seleção para indicar se a senha deve ser salva.
- Um campo para inserir o nome do aplicativo para o qual a senha está sendo gerada.
- Botões para gerar uma senha, limpar o formulário e sair do aplicativo.

A função generate_password() gera uma senha aleatória selecionando caracteres da string de caracteres fornecida, com um comprimento especificado pelo parâmetro de comprimento.

A função save_password() salva a senha fornecida para o aplicativo fornecido em um arquivo chamado "senha.txt" em um diretório chamado "Senha" localizado na pasta Documentos da conta de usuário do Windows do usuário atual.

A função generate_and_save_password() é chamada quando o botão "Gerar senha" é clicado. Ele recupera o comprimento da senha e as opções da GUI, gera uma senha usando generate_password() e exibe a senha na GUI. Se a caixa de seleção "Salvar senha" estiver marcada, ele recupera o nome do aplicativo e chama save_password() para salvar a senha.

A função clear_form() é chamada quando o botão "Limpar" é clicado. Ele limpa todos os campos de entrada e desmarca a caixa de seleção "Salvar senha".

A função root.mainloop() inicia o loop de eventos da GUI, que espera pela entrada do usuário e responde a ela.
