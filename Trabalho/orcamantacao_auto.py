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


selec = int(input('Novo: 1, Editar: 2, Sair: 0'))
artigos = {}
while selec != 0:

    if selec == 1:
        ciclo = int(input('Quantos artigos vai inserir?'))
        if ciclo != 0:
            for i in range(ciclo):  
                prod = input('Nome)')
                qua = int(input('Quantidade'))
                artigos[prod] = qua
                print(artigos)
        selec = int(input('Novo: 1, Editar: 2, Sair: 0'))
    elif selec == 2:
        print(artigos)
        selec = int(input('Novo: 1, Editar: 2, Sair: 0'))

iva = float(input('Qual o valor IVA a faturar?'))
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
    print('     ', k,'                                                            ', v )

print('                                                Total S/ IVA:', count)
print('                                                         IVA:', iva)
print('                                               Total a Pagar:', count * iva)
