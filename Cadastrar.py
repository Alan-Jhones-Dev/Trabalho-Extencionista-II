
from codigo.Const import PECA_SUPERIOR, PECA_INFERIROR, CALCADO, ACESSORIO, EQUIPAMENTO_ELETRONICO

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
        match classificador:
            case 1:
                PECA_SUPERIOR.append(peca)
                print()
            case 2:
                PECA_INFERIROR.append(peca)
            case 3:
                CALCADO.append(peca)
            case 4:
                ACESSORIO.append(peca)
            case 5:
                EQUIPAMENTO_ELETRONICO.append(peca)
            case _:
                print('Opção inválida, tente novamente')
        print('\nProduto cadastrado com sucesso!')

