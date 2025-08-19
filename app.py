from classes import *
from functions import *

while escolha_menu != 4:
    menu()
    if escolha_menu == 1:
        cadastrar_animal()
    elif escolha_menu == 2:
        listar_animais()
    elif escolha_menu == 3:
        atualizar_cadastro()
    elif escolha_menu == 4:
        print("Saindo do sistema...")
        time.sleep(3)

        

