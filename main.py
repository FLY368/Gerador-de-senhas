import string
import random
import customtkinter as ctk
from tkinter import messagebox

# Configuração global de aparência do CustomTkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# ==========================================
# FUNÇÕES DE LÓGICA
# ==========================================

def gerar_senha():
    # Obtém e valida o tamanho da senha
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            messagebox.showwarning("Erro", "O tamanho deve ser um número positivo!")
            return
    except ValueError:
        messagebox.showwarning("Erro", "Digite um número inteiro válido para o tamanho!")
        return
    
    # Monta o banco de caracteres baseado nas seleções do usuário
    caracteres = ""
    if var_letras.get():
        caracteres += string.ascii_letters
    if var_numeros.get():
        caracteres += string.digits
    if var_simbolos.get():
        caracteres += string.punctuation

    # Valida se pelo menos uma opção foi marcada
    if not caracteres:
        messagebox.showwarning("Erro", "Escolha pelo menos uma opção de caractere!")
        return

    # Gera a senha aleatória
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    
    # Exibe a senha na tela usando a propriedade configure do ctk
    entry_resultado.configure(state="normal") # Ativa temporariamente para mudar o texto
    entry_resultado.delete(0, ctk.END)        # Limpa a senha anterior
    entry_resultado.insert(0, senha)          # Insere a nova senha
    entry_resultado.configure(state="readonly") # Bloqueia para o usuário não editar

# ==========================================
# INTERFACE GRÁFICA (CUSTOMTKINTER)
# ==========================================

#Criar a janela principal
janela = ctk.CTk()
janela.title("Gerador de Senhas")
janela.geometry("450x420")
janela.resizable(False, False)
janela.iconbitmap("senha-icon.ico")

# Componente para o Tamanho da Senha
lbl_tamanho = ctk.CTkLabel(janela, text="Tamanho da Senha:", font=("Arial", 13, "bold"))
lbl_tamanho.pack(pady=(20, 5))

entry_tamanho = ctk.CTkEntry(janela, font=("Arial", 13), width=80, justify="center")
entry_tamanho.pack(pady=5)
entry_tamanho.insert(0, "12") # Define 12 como tamanho padrão

# Componentes de Seleção (CTkCheckBox)
var_letras = ctk.BooleanVar(value=True)
var_numeros = ctk.BooleanVar(value=True)
var_simbolos = ctk.BooleanVar(value=False)

# Container frame para alinhar os checkboxes no centro
frame_checks = ctk.CTkFrame(janela, fg_color="transparent")
frame_checks.pack(pady=15, padx=50, fill="x")

chk_letras = ctk.CTkCheckBox(frame_checks, text="Incluir Letras (A-Z, a-z)", variable=var_letras, font=("Arial", 12))
chk_letras.pack(anchor="w", pady=6)

chk_numeros = ctk.CTkCheckBox(frame_checks, text="Incluir Números (0-9)", variable=var_numeros, font=("Arial", 12))
chk_numeros.pack(anchor="w", pady=6)

chk_simbolos = ctk.CTkCheckBox(frame_checks, text="Incluir Símbolos (!@#...)", variable=var_simbolos, font=("Arial", 12))
chk_simbolos.pack(anchor="w", pady=6)

# Botão para Gerar a Senha
btn_gerar = ctk.CTkButton(janela, text="Gerar Senha", command=gerar_senha, font=("Arial", 14, "bold"), height=40, corner_radius=8)
btn_gerar.pack(pady=20)

# Componente para exibir o Resultado
lbl_resultado = ctk.CTkLabel(janela, text="Senha Gerada:", font=("Arial", 13, "bold"))
lbl_resultado.pack(pady=(10, 5))

entry_resultado = ctk.CTkEntry(janela, font=("Arial", 14), width=300, justify="center", state="readonly", height=35)
entry_resultado.pack(pady=5)

# Executar o aplicativo
janela.mainloop()