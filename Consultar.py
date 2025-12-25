from codigo.Const import PECA_SUPERIOR, PECA_INFERIROR, CALCADO, ACESSORIO, EQUIPAMENTO_ELETRONICO


class Consultar:
    def __init__(self):
        pass


    def run(self):
        while True:
            print('Classificação das Peças')
            print('1. Parte Superior')
            print('2. Parte Inferior')
            print('3. Calçados')
            print('4. Acessórios')
            print('5. Equipamentos Eletrônicos')
            print('6. Retornar')
            print()

            classificar = int(input('Qual classificação está a peça desejada?'))
            print()

            if classificar == 1:
                estoque = 'Não contem peças no estoque' if not PECA_SUPERIOR else PECA_SUPERIOR
                print(estoque)
                print()
                break
            elif classificar == 2:
                estoque = 'Não contem peças no estoque' if not PECA_INFERIROR else PECA_INFERIROR
                print(estoque)
                print()
                break
            elif classificar == 3:
                estoque = 'Não contem peças no estoque' if not CALCADO else CALCADO
                print(estoque)
                print()
                break
            elif classificar == 4:
                estoque = 'Não contem peças no estoque' if not ACESSORIO else ACESSORIO
                print(estoque)
                print()
                break
            elif classificar == 5:
                estoque = 'Não contem peças no estoque' if not EQUIPAMENTO_ELETRONICO else EQUIPAMENTO_ELETRONICO
                print(estoque)
                print()
                break
            elif classificar == 6:
                break
            else:
                print('Classificação invalida!')
                continue
