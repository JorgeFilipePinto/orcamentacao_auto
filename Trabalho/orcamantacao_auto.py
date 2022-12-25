# import jason file, para pré enchimendo da nossa base de dados, utilizar o PANDAS
import json

with open('dados.json', 'r') as f:
    data_base = json.load(f)
print(data_base)

#apresentação dos items desponiveis



#criação de segunda base de dados para acumulação de items adquiridos
#ciclo while lê o elemennto do dic guarda em variavel, usa-se a variavel 
# como fonte de apresentação do nome na input do utilizador
#Quando o utilizador inserir o valor o mesmo é guardado numa variavel correspondente


#apresentação do pré folheto em terminal
print('_____________________________________________________________________________')
print('|                                                                            |')
print('|                Escola Superior de Gestão e Tecnologia de Lamego            |')
print('|----------------------------------------------------------------------------|')
print('|                                 Orçamento                                  |')
print('|----------------------------------------------------------------------------|')
print('|    Item1                                               ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|    Item                                                ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|    Item2                                               ', Variavel,     '  |')
print('|                                                                            |')
print('|                                                                            |')
print('|                                                Total S/ IVA:', Variavel, ' |')
print('|                                                         IVA:', Variavel, ' |')
print('|                                               Total a Pagar:', Variavel, ' |')
print('|____________________________________________________________________________|')














#exportar para PDF o orçamento possivelmente com o PANDAS