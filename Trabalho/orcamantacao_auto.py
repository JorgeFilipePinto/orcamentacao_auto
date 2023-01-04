import json                                                             #Importação da biblioteca JSOM

with open('dados.json', encoding='utf-8') as data_base:                 #Importação do ficheiro dados.json e codificação dos caracteres
    dados = json.load(data_base)

orcamento = []
num_artigo = 1
contagem = 0
continuacar = 0
soma = 0
preco = 0
mn1 = 0

#Menus
def menu():
    print('1 - Inserir novo artigo no orçamento')
    print('2 - Editar artigos do orçamento')
    print('3 - Terminar e emitir orçamento')
    print('4 - Sair')

def menu1_1():
    print('1 - Inserir artigo único')
    print('2 - Inserir artigos múltiplos')
    print('3 - Voltar ao menu principal')

def menu1_2():
    print('1 - Editar')
    print('2 - Voltar ao menu principal')

def menu_continuar():
    print('1 - Sim')
    print('2 - Não') 


#Apresentação de todos os elementos da base de dados
print("""
   Produtos da lista
___________________________
 Código    Name       Preço
""")

for i in dados:
    print(' ', i['Code'], '   ', i['Name'], '   ', i['Price'], '\n')


while mn1 != 4:
    print('Menu principal\n')
    menu()
    mn1 = int(input('Qual a sua opção\n'))

    if mn1 == 1:
        print('Inserir novo artigo no orçamento\n')
        num_artigo = 1
        contagem = 0
        continuacar = 0
        soma = 0
        preco = 0
        mn1_1 = 0

        while mn1_1 != 3:
            menu1_1()
            mn1_1 = int(input('Qual a sua opção\n'))

            if mn1_1 == 1:
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

            elif mn1_1 == 2:
                print('Inserir artigos múltiplos\n')
                quantidade_items = 0
                quantidade_items = int(input('Quantos artigos deseja inserir?\n'))



                while quantidade_items > 0 and continuacar != 2:  
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
                    
                    if continuacar != 2 and quantidade_items != 0:  
                        menu_continuar()
                        continuacar = int(input('Deseja continuar?\n'))
                print(' Resumo do orçamento:', contagem, 'artigos.\n', 'Total do orçamento:', soma, '€\n')

    elif mn1 == 2:
        print('Editar artigos do orçamento\n')
        mn1_2 = 0

        while mn1_2 != 2:
            menu1_2()
            mn1_2 = int(input('Qual a sua opção\n'))

            if mn1_2 == 1:
                print('Editar artigos\n')
                print("""
                    Produtos da lista
                ___________________________
                Código    Name       Preço
                """)

                for i in orcamento:
                    print(i['Código'],'   ', i['Produto'], '                                                        ', i['Preço'], '€' )


    elif mn1 == 3:
        print(orcamento)
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
            """)
        for i in orcamento:
            print(i['Código'],'   ', i['Produto'], '                                                        ', i['Preço'], '€' )
        
        
        
        custo_iva = (soma * iva)
        total = (soma + custo_iva)
        print('                                                Total S/ IVA:', soma, '€')
        print('                                                         IVA:', round(custo_iva,2), '€')
        print('                                               Total a Pagar:', total, '€')

