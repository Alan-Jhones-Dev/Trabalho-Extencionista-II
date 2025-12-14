'''
from codigo.Comerciante import Comerciante
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
            'name': item,
            'região': classificador,
            'valor': valor,
            'lote': lote
        }

        LISTA_PECA.append(peca.copy())
        print('Produto cadastrado com sucesso!')
        menu_comerciante = Comerciante()
        menu_comerciante.run()
        print()
'''