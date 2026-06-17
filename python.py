# ==========================================
# IMPORTS
# ==========================================
import string
import random
import tkinter as tk

# ==========================================
# FUNÇÔES
# ==========================================

def obter_tamanho():
  while True:
    try:
     tamanho=int(input("Digite o tamanho desejado para a senha: "))
     if tamanho <=0:
        print("O número deve ser positivo")
     else:
        return tamanho
    except ValueError:
     print("apenas números inteiros são válidos")

def obter_letras():
    letras = input("Deseja incluir letras em sua senha? (s/n)").lower()
    if letras == "s":
      return string.ascii_letters
    elif letras == "n":
      return ""
    else:
      print("digite apenas (s ou n)")

def obter_numeros():
    numeros = input("Deseja incluir números em sua senha? (s/n)").lower()
    if numeros == "s":
      return string.digits
    elif numeros == "n":
        return ""
    else:
      print("digite apenas (s ou n)")

def obter_simbolos():
  while True:
    simbolos = input("Deseja incluir símbolos em sua senha? (s/n)").lower()
    if simbolos == "s":
      return string.punctuation
    elif simbolos == "n":
      return ""
    else:
      print("digite apenas (s ou n)")
   

while True:
# armazena o retorno da função na variavel
  tamanho_senha=obter_tamanho()

  while True:

    caracteres="" 

    caracteres += obter_letras()

    caracteres += obter_numeros()

    caracteres += obter_simbolos()
    if caracteres != "":
      break
    else:
        print("escolha (s) em pelo menos uma opção")

  senha = ""

  for i in range(tamanho_senha):
    senha += random.choice(caracteres)
  print("Senha criada:",senha)
  
  continuar = input("Deseja criar uma nova senha? (s/n): ").lower()
  if continuar == "n":
   break