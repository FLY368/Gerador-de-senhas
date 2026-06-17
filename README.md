# Gerador de Senhas (CLI e GUI)

Este é um projeto prático que gera senhas aleatórias seguras com base nas preferências do usuário.
O repositório contém duas versões da ferramenta: uma para execução direta no Terminal (CLI) e outra com uma Interface Gráfica (GUI) moderna e responsiva.

---

## Funcionalidades

- Comprimento Customizável: Defina o tamanho exato da senha que deseja gerar.
- Filtros de Caracteres: Escolha incluir ou remover letras, números e símbolos especiais.
- Tratamento de Erros: Validação integrada para impedir entradas de tamanhos inválidos ou geração sem critérios definidos.
- Modo Escuro Nativo (GUI): A interface em CustomTkinter adapta-se automaticamente ao tema do sistema do usuário (Light ou Dark mode).
- Versão Terminal: Rápida e leve, ideal para execuções diretas no console.

---

## Tecnologias Utilizadas

- Python 3
- CustomTkinter (Para a interface gráfica moderna)
- Tkinter (Para caixas de mensagem nativas)
- Bibliotecas nativas string e random (Para a lógica de aleatoriedade)

---

## Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com
cd Gerador-de-senhas
```

### 2. Instalar as dependências
A versão de interface gráfica utiliza a biblioteca customtkinter. Você pode instalá-la usando o pip:
```bash
pip install customtkinter
```

### 3. Executar as aplicações

* Para rodar a versão com Interface Gráfica:
  ```bash
  python main.py
  ```

* Para rodar a versão no Terminal:
  ```bash
  python python.py
  ```

---

## Estrutura de Arquivos

* main.py - Código principal contendo a interface em CustomTkinter.
* python.py - Script para geração rápida de senhas via linha de comando.
* senha-icon.ico - Ícone ou imagem utilizada no design da aplicação.
