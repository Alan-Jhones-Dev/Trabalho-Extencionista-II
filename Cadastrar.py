
from codigo.Const import LISTA_PECA

class Cadastrar:

    def __init__(self):
        pass

    def run(self, lote):
        print('A peça esta classificada como:')
        print('1. Parte Superior')
        print('2. Parte Inferior')
        print('3. Calçados')
        print('4. Acessósrios')
        print('5. Equipamentos Eletrônicos')
        print()
        classificador = int(input('>>'))
        item = input('Descreva: (blusa, short, calça) >>')
        valor = int(input('Qual o valor da peça?'))
        print()

        peca = {
            'Produto': item,
            'Regiao': classificador,
            'Valor': valor,
            'Lote': lote[0]
        }

        LISTA_PECA.append(peca.copy())
        print('\nProduto cadastrado com sucesso!')

