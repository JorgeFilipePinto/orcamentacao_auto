#gestão de produtos
#evitar inseriri códigos repetidos
#criar novos orçamentos editar eliminar e guardar em json
#guardar com datetime
#https://zetcode.com/python/fstring/




import json                                                             #Importação da biblioteca JSOM
import datetime

with open('dados.json', encoding='utf-8') as data_base:                 #Importação do ficheiro dados.json e codificação dos caracteres
    dados = json.load(data_base)

def inicio():
    if supervisor == 0:
        print('1 - Gestão Base de Dados')
        print('2 - Orçamentos\n')
    else:
        print('2 - Orçamentos\n')

def menu_basedados():
    print("1- Inserir novo artigo")
    print("2- Editar artigo")
    print("3- Sair\n")

def menu_save():
    print('1 - Sim')
    print('2 - Não')

def menu():         #Menu principal
    print('1 - Inserir novo artigo no orçamento')
    print('2 - Editar artigos do orçamento')
    print('3 - Guardar / Editar orçamentos')
    print('4 - Sair')

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

for i in dados: #Colonar dados para dados clone
    dado_bd = {}
    dado_bd['Code'] = i['Code']
    dado_bd['Name'] = i['Name']
    dado_bd['Price'] = i['Price']
    dados_clone.append(dado_bd)

while iniciar != 2:
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

while iniciar !=3:
    menu_basedados()
    iniciar = int(input('Escolha a opção!'))
    if iniciar == 1:
        for v in dados_clone:
            print(' ', v['Code'], '   ', v['Name'], '   ', v['Price'], '\n')
        
        bd_code = int(input('Introduza o código do produto.\n'))
        dado_bd = {}
        bd_name = input('Introduza o nome do produto.')
        bd_price = float(input('Introduza o preço do produto.'))
        dado_bd['Code'] = bd_code
        dado_bd['Name'] = bd_name
        dado_bd['Price'] = bd_price
        dados_clone.append(dado_bd)
        for ii in dados_clone:
            print(' ', ii['Code'], '   ', ii['Name'], '   ', ii['Price'], '\n')

    if iniciar == 2:
        for v in dados_clone:
            print(' ', v['Code'], '   ', v['Name'], '   ', v['Price'], '\n')
        
        edit_code_bd = int(input('Insira o código do produto que pretende alterar.'))

        for i in dados_clone:
            if edit_code_bd == i['Code']:
                print(i['Code'], '          ', i['Name'], '          ', i['Price'], '\n')
                new_code_bd = int(input('Insira o novo produto a substituir.'))
                new_name_bd = input('Introduza o nome.\n')
                new_price_bd = int(input('Introduza o preço\n'))
                i['Code'] = new_code_bd
                i['Produto'] = new_name_bd
                i['Price'] = new_price_bd

    if iniciar == 4:
        code_del= int(input('Introduz o Código do item a deletar: '))

        for i, item in enumerate():
            if item["Code"] == code_del:
                del data["items"][i]
                break
                    
menu_save()
save = int(input('Deseja guardar?'))
if save == 1:
    with open("dados.json", "w") as json_file:
        json.dump(dados_clone, json_file,indent=4)



#Apresentação de todos os elementos da base de dados
print("""
   Produtos da lista
___________________________
 Código    Name       Preço
""")
for i in dados:
    print(' ', i['Code'], '   ', i['Name'], '   ', i['Price'], '\n')



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
                inserir_produto = int(input('Introduza o código do produto desejado.\n'))
                for i in dados:
                    if inserir_produto == i['Code']:
                        print(i['Code'], '          ', i['Name'], '          ', i['Price'], '\n')
                        quantidade = int(input('Qual a quantidade que deseja?\n'))
                        preco = quantidade * (i['Price'])
                        soma = (soma + (quantidade * i['Price']))
                        contagem = contagem + quantidade
                        artigos = {}
                        artigos['Código'] = i['Code']
                        artigos['Produto'] = i['Name']
                        artigos['Quantidade'] = quantidade
                        artigos['Preço'] = (quantidade * i['Price'])
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
                    inserir_produto = int(input('Introduza o código do produto desejado.\n'))
                    for i in dados:
                        if inserir_produto == i['Code']:
                            print(i['Code'], '          ', i['Name'], '          ', i['Price'], '\n')
                            quantidade = int(input('Qual a quantidade que deseja?\n'))
                            preco = quantidade * (i['Price'])
                            soma = (soma + (quantidade * i['Price']))
                            artigos = {}
                            artigos['Código'] = i['Code']
                            artigos['Produto'] = i['Name']
                            artigos['Quantidade'] = quantidade
                            artigos['Preço'] = (quantidade * i['Price'])
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
                editar_produto = int(input('Insira o código do produto que pretende alterar.'))
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
                            novo_produto = int(input('Insira o novo produto a substituir.'))
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
            now = datetime.datetime.now()
            data = now.strftime('%H:%M:%S %d-%m-%Y')
            index = index + 1
            orc_dados = {}
            orc_dados['Date'] = data
            orc_dados['Index'] = index
            orcamento.append(orc_dados)
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
            Código:      Nome:                         Quantidade:           Preço:
            """)
        for i in orcamento:
            print(i['Código'],'   ', i['Produto'], '                                         ', i['Quantidade'], '               ', i['Preço'], '€\n\n' )
        
        
        
        custo_iva = (soma * iva)
        total = (soma + custo_iva)
        print('                                                Total S/ IVA:', round(soma,2), '€')
        print('                                                         IVA:', round(custo_iva,2), '€')
        print('                                               Total a Pagar:', round(total,2), '€')


