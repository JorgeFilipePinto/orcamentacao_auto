#gestão de produtos
#evitar inseriri códigos repetidos
#criar novos orçamentos editar eliminar e guardar em json
#guardar com datetime
#https://zetcode.com/python/fstring/

import json                                                             #Importação da biblioteca JSOM
import datetime

from data_base_manager.data_base_manager import DataBaseManager

db = DataBaseManager('dados.json')
db.import_dados()

def inicio():
    if supervisor == 0:
        print('1 - Gestão Base de Dados.')
        print('2 - Orçamentos.')
        print('0 - Sair.\n')
    else:
        print('2 - Orçamentos.')
        print('0 - Sair.\n')

def menu_basedados():
    print("1 - Inserir novo artigo.")
    print("2 - Editar artigo.")
    print('3 - Eliminar artigo.')
    print('4 - Ver Base de dados.')
    print("5 - Guardar.")
    print('0 - Sair.')

def menu_save():
    print('1 - Sim')
    print('2 - Não')
    print('0 - Sair.')

def menu():         #Menu principal
    print('1 - Inserir novo artigo no orçamento')
    print('2 - Editar artigos do orçamento')
    print('3 - Guardar / Editar orçamentos')
    print('0 - Sair')

def sub_menu():
    print('1 - Consultar Orçamentos.')
    print('2 - Editar Orçamentos.')
    print('3 - Sair.')

def menu1_1():      #Menu inserir artigos
    print('1 - Inserir artigo único')
    print('2 - Inserir artigos múltiplos')
    print('3 - Voltar ao menu principal')

def menu1_2():      #Menu editar artigos
    print('1 - Editar')
    print('2 - Voltar ao menu principal')

def menu_continuar():   #Menu confirmar inserir artigos multiplos
    print('1 - Sim')
    print('2 - Não') 

def sair():          #Sair do menu de edição
    print('1 - Sim')
    print('2 - Não')

index = 0
dados_clone = []
orcamento = []
num_artigo = 1
contagem = 0
soma = 0
preco = 0
user_input_1 = 0
iniciar = 0
codigo_secreto = 0000
erro_codigo = 3
supervisor = 0
code_supervisor = 11110000
data_save = 1

while iniciar != 3:
    print('Bem-vindo\n')
    inicio()
    iniciar = int(input('Escolha a opção!'))
    if iniciar == 1:
        if iniciar == code_supervisor:
            print('A sua base de dados foi desbloqueada com sucesso.\n')
            erro_codigo = 3
            supervisor = 0
        if iniciar == 1:
            print('Gestão de Base de Dados!\n')
            password = int(input('Por favor introduza o código de acesso!'))
            if password == codigo_secreto:
                erro_codigo = 3
                iniciar = 2
            else:
                erro_codigo = erro_codigo - 1
                print('O código que introduziu está errado!!\nRestam', erro_codigo, 'Tentativas\n')
            if erro_codigo == 0:
                supervisor = 1
                print('Não tem mais tentativas por favor dirija-se ao seu supervisor.\n')
        while iniciar != 6:
            menu_basedados()
            iniciar = int(input('Escolha a opção!'))
            if iniciar == 1:
                bd_code = input('Introduza o código do produto.\n')
                dado_bd = {}
                bd_name = input('Introduza o nome do produto.')
                bd_price = float(input('Introduza o preço do produto.'))

                db.insert(bd_code, bd_name, bd_price)
                data_save = 0
            
            if iniciar == 2:
                data_save = 0
                print(db)
                
                edit_code_bd = input('Insira o código do produto que pretende alterar.')
                while not db.check_code(edit_code_bd):
                    edit_code_bd = input('Insira o código do produto que pretende alterar.')

                new_code_bd = input('Insira o novo produto a substituir.')
                new_name_bd = input('Introduza o nome.\n')
                new_price_bd = float(input('Introduza o preço\n'))
                db.insert(new_code_bd, new_name_bd, new_price_bd)
        ########################################################################################################################################################################
            if iniciar == 3:
                print(db)
                edit_code_bd = input('Insira o código do produto que pretende eliminar.')
                db.remove(edit_code_bd)
                print(db)
        ########################################################################################################################################################################

            if iniciar == 4 :
                print(db)

            if iniciar == 5:
                if data_save == 1: 
                    print('Não existem alterações.\n')                   
                    menu_save()
                    save = int(input('Deseja guardar?\n'))
                    if save == 1:
                        db.save()
                        data_save = 1
                elif data_save == 0:
                    print('Existem alterações que ainda não foram salvas.\n')                   
                    menu_save()
                    save = int(input('Deseja guardar?\n'))
                    if save == 1:
                        db.save()
                        data_save = 1
                else:
                    continue


    if iniciar == 2:

        #Apresentação de todos os elementos da base de dados
        print("""
        Produtos da lista
        ___________________________
        """)
        print(db)

        if data_save == 0:
            print('Existem alterações que ainda não foram salvas!\n')
            menu_save()
            save = int(input('Deseja guardar?\n'))
            if save == 1:
                db.save()
            else:
                pass


    while user_input_1 != 4:
        print('Menu principal\n')
        menu()
        user_input_1 = int(input('Qual a sua opção\n'))

        if user_input_1 == 1:    #Inserir artigos
            print('Inserir novo artigo no orçamento\n')
            num_artigo = 1
            contagem = 0
            continuar = 0
            soma = 0
            preco = 0
            user_input_1_1 = 0

            while user_input_1_1 != 3:
                menu1_1()
                user_input_1_1 = int(input('Qual a sua opção\n'))

                if user_input_1_1 == 1:      #Inserir artigo único
                    print('Inserir artigo único\n')
                    print('Artigo', num_artigo, '\n')
                    inserir_produto = input('Introduza o código do produto desejado.\n')
                    if db.check_code(inserir_produto):
                        print(db.get_elem_as_str(inserir_produto))
                        quantidade = int(input('Qual a quantidade que deseja?\n'))
                        preco = quantidade * (i['Price'])
                        soma = (soma + (quantidade * i['Price']))
                        contagem = contagem + quantidade
                        artigos = {}
                        index = index + 1
                        artigos['Index'] = index
                        now = datetime.datetime.now()
                        data = now.strftime('%d-%m-%Y')
                        artigos['Date'] = data
                        artigos['Code'] = i['Code']
                        artigos['Name'] = i['Name']
                        artigos['Quanti'] = quantidade
                        artigos['Price'] = (quantidade * i['Price'])
                        orcamento.append(artigos)
                        print('Inserido com sucesso.\n')
                        print(' Resumo do orçamento:', contagem, 'artigos.\n', 'Total do orçamento:', soma, '€\n')
                        num_artigo = num_artigo + 1

                elif user_input_1_1 == 2:    #Inserir multi-artigos
                    print('Inserir artigos múltiplos\n')
                    quantidade_items = 0
                    continuar = 0
                    quantidade_items = int(input('Quantos artigos deseja inserir?\n'))

                    while quantidade_items > 0 and continuar != 2:  
                        print('Artigo', num_artigo, '\n')
                        inserir_produto = input('Introduza o código do produto desejado.\n')
                        for i in dados:
                            if inserir_produto == i['Code']:
                                print(i['Code'], '          ', i['Name'], '          ', i['Price'], '\n')
                                quantidade = int(input('Qual a quantidade que deseja?\n'))
                                preco = quantidade * (i['Price'])
                                soma = (soma + (quantidade * i['Price']))
                                artigos = {}
                                index = index + 1
                                artigos['Index'] = index
                                now = datetime.datetime.now()
                                data = now.strftime('%H:%M:%S %d-%m-%Y')
                                artigos['Date'] = data
                                artigos['Code'] = i['Code']
                                artigos['Name'] = i['Name']
                                artigos['Quanti'] = quantidade
                                artigos['Price'] = (quantidade * i['Price'])
                                orcamento.append(artigos)
                                print('Inserido', quantidade, 'com sucesso, no total de:', preco, '€\n')
                                quantidade_items = quantidade_items - 1
                                num_artigo = num_artigo + 1
                                contagem = contagem + quantidade
                                while continuar != 2 and quantidade_items != 0:
                                    menu_continuar()
                                    continuar = int(input('Deseja continuar?\n'))
                                    if continuar == 1 or continuar == 2:
                                        break
                                    else:
                                        print('Por favor introduza uma opção válida!\n')
                                print(' Resumo do orçamento:', contagem, 'artigos.\n', 'Total do orçamento:', soma, '€\n')


        elif user_input_1 == 2:  #Editar orçamento
            print('Editar artigos do orçamento\n')
            user_input_1_2 = 0

            while user_input_1_2 != 2:
                print('Editar artigos\n')
                print("""
                        Produtos do orçamento
                    ___________________________
                    Código    Name       Preço
                    """)
                for i in orcamento:         #Print dos elementos do orçamento
                    print(i['Código'],'   ', i['Produto'], '                           ', i['Quantidade'], '                            ', i['Preço'], '€\n')

                menu1_2()
                user_input_1_2 = int(input('Qual a sua opção\n'))

                if user_input_1_2 == 1:
                    editar_produto = input('Insira o código do produto que pretende alterar.')
                    sair_editor = 0
                    while sair_editor != 1:
                        for edit in orcamento:
                            if editar_produto == edit['Código']:
                                print(edit['Código'])
                                print("""
                                Produtos da lista
                                ___________________________
                                Código    Name       Preço
                                """)
                                for i in dados:
                                    print(' ', i['Code'], '   ', i['Name'], '   ', i['Price'], '\n')
                                novo_produto = input('Insira o novo produto a substituir.')
                                for i in dados:
                                    if novo_produto == i['Code']:
                                        print(i['Code'], '          ', i['Name'], '          ', i['Price'], '\n')
                                        quantidade = int(input('Qual a quantidade que deseja?\n'))
                                        edit['Quantidade'] = quantidade
                                        edit['Código'] = i['Code']
                                        edit['Produto'] = i['Name']
                                        edit['Preço'] = (quantidade * i['Price'])
                        else:
                            print('O código que introduziu não existe no orçamento.')
                            break

        elif user_input_1 == 3:  #Print terminal do orçamento
            menu_save()
            save = int(input('Deseja Guardar?'))
            if save == 1:
                with open("orcamentos.json", "w") as json_file:
                    json.dump(orcamento, json_file,indent=4)
            else:
                print('Não guardou o orçamento.')

            iva = float(input('Qual o valor do IVA?'))
            iva = iva/100
            print('Terminar e emitir orçamento\n')
            print("""
                _____________________________________________________________________________
                |                                                                            |
                |                Escola Superior de Gestão e Tecnologia de Lamego            |
                |----------------------------------------------------------------------------|
                |                                 Orçamento                                  |
                |----------------------------------------------------------------------------|
                Data:      Número:
                
                Código:      Nome:                         Quantidade:           Preço:
                """)
            for i in orcamento:
                print(i['Código'],'   ', i['Produto'], '                                         ', i['Quantidade'], '               ', i['Preço'], '€\n\n' )
            
            
            
            custo_iva = (soma * iva)
            total = (soma + custo_iva)
            print('                                                Total S/ IVA:', round(soma,2), '€')
            print('                                                         IVA:', round(custo_iva,2), '€')
            print('                                               Total a Pagar:', round(total,2), '€')


