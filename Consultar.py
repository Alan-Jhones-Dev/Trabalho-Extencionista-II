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

            match classificar:
                case 1:
                    print(PECA_SUPERIOR)
                    break
                case 2:
                    print(PECA_INFERIROR)
                    break
                case 3:
                    print(CALCADO)
                    break
                case 4:
                    print(ACESSORIO)
                    break
                case 5:
                    print(EQUIPAMENTO_ELETRONICO)
                    break
                case _:
                    print('classificação invalida')
                    break
