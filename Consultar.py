from codigo.Const import LISTA_PECA
class Consultar:
    def __init__(self):
        pass

#A CLASSE CONSULTAR NÃO ESTA MONSTRANDO TODOS OS PRODUTOS CLASSIFICADOS NA CATEGORIA ESCOLHIDA:

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

            if 1 <= classificar <= 5:
                s_regiao = classificar
                peca = next((p for p in LISTA_PECA if p['Regiao'] == s_regiao), None)

                if peca is not None:
                    print('\n Peças em estoque:\n')
                    for keys, value in peca.items():
                        print(f'{keys} = {value}\n')

                else:
                    print('Peça não encontrada')
                    continue
                    print()

            elif classificar == 6:
                print()
            else:
                print('Escolha um valor entre 1 á 6')
                continue
            print()
