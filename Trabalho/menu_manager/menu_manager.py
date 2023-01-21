import os

from enum import Enum

<<<<<<< HEAD

=======
from data_base_manager.data_base_manager import DataBaseManager
from data_base_orcamentos.data_base_orcamentos import DataBaseOrcamentos
>>>>>>> Add Core

class MenuCodes(Enum):
    EXIT = 0
    MAIN_MENU = 1
    
    DATA_BASE_MENU = 2
    ADD_TO_DATA_BASE = 3
    DELETE_FROM_DATA_BASE = 4
    
    ORCAMENTO_MENU = 6

    ADD_ORCAMENTO = 7
    EDIT_ORCAMENTO = 8
    CONSULT_ORCAMENTOS = 9
    DELETE_ORCAMENTO = 10
    
    ADD_TO_NEW_ORCAMENTO = 11
    DELETE_FROM_NEW_ORCAMENTO = 12

    ADD_TO_EDITED_ORCAMENTO = 13
    DELETE_FROM_EDITED_ORCAMENTO = 14

class CoreApp:

    def __init__(self, store_db):
<<<<<<< HEAD
        self.active_menu = MenuCodes.MAIN
        self.store_db = store_db
        self.orcamento_ativo = None

=======
        self.active_menu = MenuCodes.MAIN_MENU
        self.store_db = store_db
        self.orcamento_ativo = None

    def run(self):
        while self.active_menu != MenuCodes.EXIT:
            self.next_menu()
    

>>>>>>> Add Core
    def delete_from_base_dados(self):
        pass

    def add_to_base_dados(self):
        pass

    def delete_orcamento(self):
        pass

    def next_menu(self):
        if self.active_menu == MenuCodes.MAIN_MENU:
            self.print_main_menu()
            user_input = input()
            if user_input == '0':
                self.active_menu = MenuCodes.EXIT
                return
            if user_input == '1': # password?
                self.active_menu = MenuCodes.DATA_BASE_MENU
                return
            if user_input == '2':
                self.active_menu = MenuCodes.ORCAMENTO_MENU
                return
            print('Opção desconhecida!')
            return
        
        if self.active_menu == MenuCodes.DATA_BASE_MENU:
            self.print_menu_base_dados()
            user_input = input()
            if user_input == '0':
                self.active_menu = MenuCodes.MAIN_MENU
                return
            if user_input == '1':
                self.add_to_base_dados()
                return
            if user_input == '2':
                self.delete_from_base_dados()
                return
            if user_input == '3':
                print(self.store_db)
                return
            if user_input == '4':
                self.store_db.save()
                return
            print('Opção desconhecida!')
            return
        
        if self.active_menu == MenuCodes.ORCAMENTO_MENU:
            self.print_main_menu_orcamento()
            user_input = input()
            if user_input == '0':
                self.active_menu = MenuCodes.MAIN_MENU
                return
            if user_input == '1':
                self.active_menu = MenuCodes.ADD_ORCAMENTO
                return
            if user_input == '2':
                self.active_menu = MenuCodes.EDIT_ORCAMENTO
                return
            if user_input == '3':
<<<<<<< HEAD
                for _, _, file_names in os.walk('orcamentos'):
                    print(file_names) # TODO improve
=======
                for path, _, file_names in os.walk('orcamentos'):
                    for file in file_names:
                        o = DataBaseOrcamentos(path+'/'+file)
                        o.import_dados()
                        o.calcutate_totals()
                        print(o)
>>>>>>> Add Core
                return
            if user_input == '4':
                self.delete_orcamento()
                return
            print('Opção desconhecida!')
            return

        if self.active_menu == MenuCodes.ADD_ORCAMENTO:
<<<<<<< HEAD
            self.orcamento_ativo = BaseDadosOrcamento()
=======
            self.orcamento_ativo = DataBaseOrcamentos()
>>>>>>> Add Core
            self.print_menu_add_orcamento()
            user_input = input()
            if user_input == '0':
                self.active_menu = MenuCodes.MAIN_MENU
                return
            if user_input == '1':
                self.add_to_orcamento()
                return
            if user_input == '2':
                self.delete_from_orcamento()
                return
            if user_input == '3':
                print(self.orcamento_ativo)
                return
<<<<<<< HEAD
=======
            print('Opção desconhecida!')
            return
>>>>>>> Add Core
        
        if self.active_menu == MenuCodes.EDIT_ORCAMENTO:
            self.print_menu_edit_orcamento()
            user_input = input()
            if user_input == '0':
                self.active_menu = MenuCodes.MAIN_MENU
                return
            if user_input == '1':
                self.add_to_base_dados()
                return
            if user_input == '2':
                self.delete_from_base_dados()
                return
            if user_input == '3':
                print(self.store_db)
                return
<<<<<<< HEAD
=======
            print('Opção desconhecida!')
            return
>>>>>>> Add Core


    def print_main_menu(self):
        print('1 - Gestão Base de Dados.')
        print('2 - Orçamentos.')
        print('0 - Sair.\n')

    def print_menu_base_dados(self):
        print("1 - Inserir novo artigo.")
        print('2 - Eliminar artigo.')
        print('3 - Ver Base de dados.')
        print("4 - Guardar.")
        print('0 - Sair.\n')

    def print_main_menu_orcamento(self):
<<<<<<< HEAD
        print('1 - Criar nove orçamento')
=======
        print('1 - Criar novo orçamento')
>>>>>>> Add Core
        print('2 - Editar editar orçamento')
        print('3 - Ver orçamentos existentes')
        print('4 - Ver orçamento especifico')
        print('5 - Eliminar orçamento')
        print('0 - Sair\n')
    
    def print_menu_add_orcamento(self):
        print('1 - Inserir novo artigo no orçamento')
        print('2 - Eliminar artigo do orçamento')
        print('3 - Ver orçamento')
        print('4 - Ver artigos disponíveis')
        print('5 - Guardar orçamento')
        print('0 - Sair\n')

    def print_menu_edit_orcamento(self):
        print('1 - Inserir novo artigo no orçamento')
        print('2 - Eliminar artigo do orçamento')
        print('3 - Ver orçamento')
        print('4 - Ver artigos disponíveis')
        print('5 - Guardar orçamento')
        print('0 - Sair\n')

