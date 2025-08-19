from classes import Roedores, Cachorro, Gato
import os
import time
import random

escolha_menu = 0

def menu():
    os.system("cls")
    print(50 * "-")
    print("Bem-vindo ao sistema de gerenciamento de animais!".center(50))
    print(50 * "-")
    print("1. Cadastrar Animais")
    print("2. Listar Animais")
    print("3. Atualizar Cadastro")
    print("4. Sair")

    escolha_menu = int(input("\nEscolha uma opção:\n-->"))

    if escolha_menu == 1:
        cadastrar_animal()
    elif escolha_menu == 2:
        listar_animais()
    elif escolha_menu == 3:
        atualizar_cadastro()
    elif escolha_menu == 4:
        print("Saindo do sistema")
        time.sleep(3)


def cadastrar_animal():
    os.system("cls")
    print(50 * "-")
    print("Cadastro de Animais".center(50))
    print(50 * "-")
    nome = input("Digite o nome do animal: ")
    os.system("cls")
    peso = float(input("Digite o peso do animal: "))
    os.system("cls")
    cor = input("Digite a cor do animal: ")
    os.system("cls")

    print(50 * "-")
    print("Escolha o tipo de animal:".center(50))
    print(50 * "-")
    print("1. Roedor")
    print("2. Cachorro")
    print("3. Gato")
    
    tipo_animal = int(input("\nDigite o número correspondente ao tipo de animal:\n-->"))

    if tipo_animal == 1:
        animal = Roedores(nome, peso, cor)
        Roedores.Roedores.append(animal)
        print("Animal cadastrado com sucesso!")
        time.sleep(3)
    elif tipo_animal == 2:
        animal = Cachorro(nome, peso, cor)
        Cachorro.Cachorros.append(animal)
        print("Animal cadastrado com sucesso!")
        time.sleep(3)
    elif tipo_animal == 3:
        animal = Gato(nome, peso, cor)
        Gato.Gatos.append(animal)
        print("Animal cadastrado com sucesso!")
        time.sleep(3)
    else:
        print("Tipo de animal inválido!")
        time.sleep(5)

def listar_animais():
    os.system("cls")
    print(50 * "-")
    print("Listagem de Animais".center(50))
    print(50 * "-")

    print("Escolha o tipo de animal para listar:")
    print("1. Roedores")
    print("2. Cachorros")
    print("3. Gatos")

    numero_listar = int(input("\nDigite o número correspondente ao tipo de animal:\n-->"))

    if numero_listar == 1:
        for roedor in Roedores.Roedores:
            print(f"Nome: {roedor._Roedores__nome}, Peso: {roedor._Roedores__peso}, Cor: {roedor._Roedores__cor}")
            os.system("pause")
    elif numero_listar == 2:
        for cachorro in Cachorro.Cachorros:
            print(f"Nome: {cachorro._Cachorro__nome}, Peso: {cachorro._Cachorro__peso}, Cor: {cachorro._Cachorro__cor}")
            os.system("pause")
    elif numero_listar == 3:
        for gato in Gato.Gatos:
            print(f"Nome: {gato._Gato__nome}, Peso: {gato._Gato__peso}, Cor: {gato._Gato__cor}")
            os.system("pause")


def atualizar_cadastro():
    os.system("cls")
    print(50 * "-")
    print("Atualização de Cadastro".center(50))
    print(50 * "-")
    print("Escolha o tipo de animal para refazer o cadastro:")
    print("1. Roedores")
    print("2. Cachorros")
    print("3. Gatos")

    numero_atualizar = int(input("\nDigite o número correspondente ao tipo de animal:\n-->"))
    if numero_atualizar == 1:
        if Roedores.Roedores:
            for i, roedor in enumerate(Roedores.Roedores):
                print(f"{i + 1}. Nome: {roedor._Roedores__nome}, Peso: {roedor._Roedores__peso}, Cor: {roedor._Roedores__cor}")
            indice = int(input("Digite o número do roedor que deseja atualizar: ")) - 1
            if 0 <= indice < len(Roedores.Roedores):
                nome = input("Digite o novo nome do roedor: ")
                peso = float(input("Digite o novo peso do roedor: "))
                cor = input("Digite a nova cor do roedor: ")
                Roedores.Roedores[indice] = Roedores(nome, peso, cor)
            else:
                print("Índice inválido!")
        else:
            print("Nenhum roedor cadastrado.")



    elif numero_atualizar == 2:
        if Cachorro.Cachorros:
            for i, cachorro in enumerate(Cachorro.Cachorros):
                print(f"{i + 1}. Nome: {cachorro._Cachorro__nome}, Peso: {cachorro._Cachorro__peso}, Cor: {cachorro._Cachorro__cor}")
            indice = int(input("Digite o número do cachorro que deseja atualizar: ")) - 1
            if 0 <= indice < len(Cachorro.Cachorros):
                nome = input("Digite o novo nome do cachorro: ")
                peso = float(input("Digite o novo peso do cachorro: "))
                cor = input("Digite a nova cor do cachorro: ")
                Cachorro.Cachorros[indice] = Cachorro(nome, peso, cor)
            else:
                print("Índice inválido!")
        else:
            print("Nenhum cachorro cadastrado.")

    elif numero_atualizar == 3:
        if Gato.Gatos:
            for i, gato in enumerate(Gato.Gatos):
                print(f"{i + 1}. Nome: {gato._Gato__nome}, Peso: {gato._Gato__peso}, Cor: {gato._Gato__cor}")
            indice = int(input("Digite o número do gato que deseja atualizar: ")) - 1
            if 0 <= indice < len(Gato.Gatos):
                nome = input("Digite o novo nome do gato: ")
                peso = float(input("Digite o novo peso do gato: "))
                cor = input("Digite a nova cor do gato: ")
                Gato.Gatos[indice] = Gato(nome, peso, cor)
            else:
                print("Índice inválido!")
        else:
            print("Nenhum gato cadastrado.")




    

