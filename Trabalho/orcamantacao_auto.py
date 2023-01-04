import json                                                             #Importação da biblioteca JSOM

with open('dados.json', encoding='utf-8') as data_base:                 #Importação do ficheiro dados.json e codificação dos caracteres
    dados = json.load(data_base)

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

def mncont():
    print('1 - Sim')
    print('2 - Não')


#Apresentação de todos os elementos da base de dados
print("""
   Produtos da lista
___________________________
 Código    Name       Preço
""")


for i in dados:
    print(' ', i['Código'], '   ', i['Name'], '   ', i['Price'], '\n')



artigos = {}
mn1 = 0

while mn1 != 4:
    print('Menu principal\n')
    menu()
    mn1 = int(input('Qual a sua opção\n'))

    if mn1 == 1:
        print('Inserir novo artigo no orçamento\n')
        mn1_1 = 0

        while mn1_1 != 3:
            menu1_1()
            mn1_1 = int(input('Qual a sua opção\n'))

            if mn1_1 == 1:
                print('Inserir artigo único\n')
                prod = input('Nome)')
                qua = int(input('Quantidade'))
                artigos[prod] = qua
                print('Artigo inserido com sucesso\n')

            elif mn1_1 == 2:
                print('Inserir artigos múltiplos\n')
                quantidade_items = 0
                quantidade_items = int(input('Quantos artigos deseja inserir?'))
                contagem = 1
                continuacar = 0


                while quantidade_items > 0 and continuacar != 2:  
                    print('Artigo', contagem, '\n')
                    prod = input('Nome)')
                    qua = int(input('Quantidade'))
                    artigos[prod] = qua
                    print('Inserido com sucesso\n')
                    quantidade_items = quantidade_items - 1
                    contagem = contagem + 1

                    if continuacar != 2 and quantidade_items != 0:  
                        mncont()
                        continuacar = int(input('Deseja continuar?'))
                print(contagem, 'Artigos inseridos com sucesso\n')

    elif mn1 == 2:
        print('Editar artigos do orçamento\n')
        mn1_2 = 0

        while mn1_2 != 2:
            menu1_2()
            mn1_2 = int(input('Qual a sua opção\n'))

            if mn1_2 == 1:
                print('Editar artigos\n')
                print(artigos)

    elif mn1 == 3:
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
        count = 0
        for k,v in artigos.items():
            count = count + v
            print('     ', k,'                                                            ', v, '€' )
        custo_iva = (count * iva)
        total = (count + custo_iva)
        print('                                                Total S/ IVA:', count, '€')
        print('                                                         IVA:', round(custo_iva,2), '€')
        print('                                               Total a Pagar:', total, '€')

