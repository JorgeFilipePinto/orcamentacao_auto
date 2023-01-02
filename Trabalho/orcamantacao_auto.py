import json


with open('dados.json', encoding='utf-8') as data_base:
    dados = json.load(data_base)


print("""
   Produtos da lista
_______________________
 Código           Name
""")


for i in dados:
    print(' ', i['Código'], '           ', i['Name'])


#criação de segunda base de dados para acumulação de items adquiridos
#ciclo while lê o elemennto do dic guarda em variavel, usa-se a variavel 
# como fonte de apresentação do nome na input do utilizador
#Quando o utilizador inserir o valor o mesmo é guardado numa variavel correspondente

selec = int(input('Novo: 1, Editar: 2, Sair: 0'))
artigos = []
while selec != 0:

    if selec == 1:
        artigos.apped()
    
    elif selec == 2:
        print(artigos)

    elif selec == 0:
        print(artigos)

    selec = int(input('Novo: 1, Editar: 2, Sair: 0'))
print("""
_____________________________________________________________________________
|                                                                            |
|                Escola Superior de Gestão e Tecnologia de Lamego            |
|----------------------------------------------------------------------------|
|                                 Orçamento                                  |
|----------------------------------------------------------------------------|
""")

#print('|    Item2                                               ', Variavel,     '  |')
#print('|                                                                            |')
#print('|                                                                            |')
#print('|                                                Total S/ IVA:', Variavel, ' |')
#print('|                                                         IVA:', Variavel, ' |')
#print('|                                               Total a Pagar:', Variavel, ' |')
#print('|____________________________________________________________________________|')
