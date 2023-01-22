import os

from enum import Enum

from data_base_manager.data_base_manager import DataBaseManager
from data_base_orcamentos.data_base_orcamentos import DataBaseOrcamentos

class MenuCodes(Enum):
    EXIT = 0
    MAIN_MENU = 1
    
    DATA_BASE_MENU = 2
    
    ORCAMENTO_MENU = 6

    ADD_ORCAMENTO = 7
    EDIT_ORCAMENTO = 8


class CoreApp:

    def __init__(self, store_db):
        self.active_menu = MenuCodes.MAIN_MENU
        self.store_db = store_db
        self.orcamento_ativo = None

    def run(self):
        while self.active_menu != MenuCodes.EXIT:
            self.next_menu()
    
    def delete_from_base_dados(self):                                   #Eliminar elementos da base de dados
        del_db_code = input('Introduza o código do elemento a eliminar ou introduza 0 para sair: ')
        if del_db_code == '0':
            print('Cancelou a sua operação!')
            return
        for path, _, file_names in os.walk('orcamentos'):
            for file in file_names:
                o = DataBaseOrcamentos(path+'/'+file)
                o.import_dados()
                if o.check_code(del_db_code):
                    print(f'Este artigo encontra-se ativo no orçamento {file}! Impossível eliminar.')
                    return
        self.store_db.remove(del_db_code)
            

    def add_to_base_dados(self):                                        #Inserir elementos da base de dados
        insert_db_code = input('\nIntroduza o código do artigo desejado:  ')
        if not insert_db_code =='0':
            insert_db_name = input('Introduza o nome do artigo: ')
            try:
                insert_db_price = float(input('Introduza o preço do artigo: '))
            except ValueError:
                print('O preço inserido não é válido!!')
                return
            result = self.store_db.insert(insert_db_code, insert_db_name, insert_db_price)

            if result:
                print('\nO seu artigo foi adicionada com sucesso.')
                print(insert_db_code)
                print(insert_db_name)
                print(insert_db_price)
        else:
            print('Cancelou a sua operação!')
            return
        
    def add_to_orcamento(self):
        insert_orcamento_code = input('\nIntroduza o código do artigo desejado ou insira 0 para sair:  ')
        if not insert_orcamento_code =='0':
            insert_orcamento_quantity =int(input('Introduza a quantidade desejada: '))
            self.orcamento_ativo.insert(insert_orcamento_code, insert_orcamento_quantity, self.store_db)
            print('Artigo inserido com sucesso.')
        else:
            print('Cancelou a sua operação!')
            return
        
    def delete_from_orcamento(self):
        del_orcamento_code = input('Introduza o código do elemento a eliminar ou introduza 0 para sair: ')
        if not del_orcamento_code == '0':
            self.orcamento_ativo.remove(del_orcamento_code)
        else:
            print('Cancelou a sua operação!')
            return        
    
    def delete_orcamento(self):
        name_file_to_remove = 'orcamentos\\' + input('Insira o nome do orçamento ou insira 0 para voltar: ')
        if name_file_to_remove == 0:
            return
        if not os.path.isfile(name_file_to_remove):
            print('Não foi possivel encontrar o orçamento, por favor vericar os orçamentos existentes.')
            return

        orcamento_delete = DataBaseOrcamentos(name_file_to_remove)
        orcamento_delete.import_dados()
        self.active_menu = MenuCodes.ORCAMENTO_MENU
        orcamento_delete.calcutate_totals()
        print(orcamento_delete)
        print('\nDeseja mesmo eliminar? ')
        print('                1 - Sim.')
        print('Qualquer caracter - Não.')
        confirm_del = input('')
        if confirm_del == '1':
            print('Orçamento eliminado com sucesso.')
            os.remove(name_file_to_remove)

    def next_menu(self):                                                #Menu
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
        
        if self.active_menu == MenuCodes.DATA_BASE_MENU:                    #Gestão de artigos
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
                self.orcamento_ativo = DataBaseOrcamentos()
                return
            if user_input == '2':
                name_file = 'orcamentos\\' + input('Insira o nome do orçamento ou insira 0 para voltar: ')
                if name_file == 0:
                    return
                if not os.path.isfile(name_file):
                    print('Não foi possivel encontrar o orçamento, por favor vericar os orçamentos existentes.')
                    return
                self.orcamento_ativo = DataBaseOrcamentos(name_file)
                self.orcamento_ativo.import_dados()
                self.active_menu = MenuCodes.EDIT_ORCAMENTO
                return
            if user_input == '3':
                for path, _, file_names in os.walk('orcamentos'):
                    for file in file_names:
                        o = DataBaseOrcamentos(path+'/'+file)
                        o.import_dados()
                        o.calcutate_totals()
                        print(file)
                return




            if user_input == '4':
                pass
                return


            if user_input == '5':
                self.delete_orcamento()
                return
            print('Opção desconhecida!')
            return

        if self.active_menu == MenuCodes.ADD_ORCAMENTO:                                 #Criar novo orçamento - finish
            self.print_menu_add_orcamento()
            user_input = input()
            if user_input == '0':
                if self.save():
                    self.orcamento_ativo.save()
                self.active_menu = MenuCodes.ORCAMENTO_MENU
                self.orcamento_ativo = None
                return

            if user_input == '1':
                self.add_to_orcamento()
                return
            if user_input == '2':
                self.delete_from_orcamento()
                return
            if user_input == '3':
                self.orcamento_ativo.calcutate_totals()
                print(self.orcamento_ativo)
                return
            if user_input == '4':
                print(self.store_db)
                return
            if user_input == '5':
                if self.save():
                    self.orcamento_ativo.save()
                return
            print('Opção desconhecida!')
            return
        
        if self.active_menu == MenuCodes.EDIT_ORCAMENTO:                        #Editar orçamento do ficheiro
            self.print_menu_edit_orcamento()
            user_input = input()
            if user_input == '0':
                if self.save():
                    self.orcamento_ativo.save()
                self.active_menu = MenuCodes.ORCAMENTO_MENU
                self.orcamento_ativo = None
                return

            if user_input == '1':
                self.add_to_orcamento()
                return
            if user_input == '2':
                self.delete_from_orcamento()
                return
            if user_input == '3':
                self.orcamento_ativo.calcutate_totals()
                print(self.orcamento_ativo)
                return

            if user_input == '4':
                pass
                return
            if user_input == '5':
                if self.save():
                    self.orcamento_ativo.save()
                return

            print('Opção desconhecida!')
                
    def print_main_menu(self):                                          #Menu principal
        print('\n--MENU PRINCIPAL--')
        print('1 - Gestão de artigos.')
        print('2 - Gestão de orçamentos.')
        print('0 - Sair.\n')

    def print_menu_base_dados(self):                                    #Menu data base
        print('\n--GESTÃO DE ARTIGOS--')
        print("1 - Inserir novo artigo.")
        print('2 - Eliminar artigo.')
        print('3 - Ver Base de dados.')
        print("4 - Guardar.")
        print('0 - Sair.\n')

    def print_main_menu_orcamento(self):                                #Menu orcamento
        print('\n--GESTÃO DE ORÇAMENTOS--')
        print('1 - Criar novo orçamento')
        print('2 - Editar orçamento')
        print('3 - Ver orçamentos existentes')
        print('4 - Ver orçamento especifico')
        print('5 - Eliminar orçamento')
        print('0 - Sair\n')
    
    def print_menu_add_orcamento(self):                                 #Menu Adicionar orcamento
        print('\n--ADICIONAR NOVO ORÇAMENTO--')
        print('1 - Inserir novo artigo no orçamento')
        print('2 - Eliminar artigo do orçamento')
        print('3 - Ver orçamento')
        print('4 - Ver artigos disponíveis')
        print('5 - Guardar orçamento')
        print('0 - Sair\n')

    def print_menu_edit_orcamento(self):                                #Menu Adicionar artigos
        print('\n--EDITAR ORÇAMENTO--')
        print('1 - Inserir novo artigo no orçamento')
        print('2 - Eliminar artigo do orçamento')
        print('3 - Ver orçamento')
        print('4 - Ver artigos disponíveis')
        print('5 - Guardar orçamento')
        print('0 - Sair\n')

    def save(self):                                                   #Menu salvar
        print('Deseja salvar? ')
        print('\n1 - Sim.')
        print('Qualquer caracter - Não.')
        save_input = input()
        if save_input == '1':
            return True
        return False
