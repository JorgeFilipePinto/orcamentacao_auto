import json                                                             #Importação da biblioteca JSOM

with open('dados.json', encoding='utf-8') as data_base:                 #Importação do ficheiro dados.json e codificação dos caracteres
    dados = json.load(data_base)

#Apresentação de todos os elementos da base de dados
print("""
   Produtos da lista
___________________________
 Código    Name       Preço
""")
for i in dados:
    print(' ', i['Code'], '   ', i['Name'], '   ', i['Price'], '\n')

orcamento = []
num_artigo = 1
contagem = 0
soma = 0
preco = 0
user_input_1 = 0

def menu():         #Menu principal
    print('1 - Inserir novo artigo no orçamento')
    print('2 - Editar artigos do orçamento')
    print('3 - Terminar e emitir orçamento')
    print('4 - Sair')

def menu1_1():      #Menu inserir artigos
    print('1 - Inserir artigo único')
    print('2 - Inserir artigos múltiplos')
    print('3 - Voltar ao menu principal')

def menu1_2():      #Menu editar artigos
    print('1 - Editar')
    print('2 - Voltar ao menu principal')

def menu_continuar():#Menu confirmar inserir artigos multiplos
    print('1 - Sim')
    print('2 - Não') 

def sair():          #Sair do menu de edição
    print('1 - Sim')
    print('2 - Não')

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
                        else:
                            continue 

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
        print('                                                Total S/ IVA:', soma, '€')
        print('                                                         IVA:', round(custo_iva,2), '€')
        print('                                               Total a Pagar:', total, '€')

