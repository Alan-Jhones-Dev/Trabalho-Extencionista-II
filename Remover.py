from codigo.Const import LISTA_PECA
class Remover:
    def __init__(self):
        pass

#O CODIGO AINDA FALTA SER TESTADO, PRIMEIRO O ERRO DA CLASSE CONSULTAR TEM QUE SER CORRIGIDO


    def run(self):
        while True:
            print('1. Parte Superior')
            print('2. Parte Inferior')
            print('3. Calçados')
            print('4. Acessórios')
            print('5. Equipamentos Eletrônicos')

            classificar = int(input('Qual classificação está a peça deseja remover? >>\n'))

            if 1 <= classificar <= 5:
                s_regiao = classificar
                peca = next((p for p in LISTA_PECA if p['Regiao'] == s_regiao), None)

                if peca is not None:
                    print('\n Peças em estoque:\n')
                    for keys, value in peca.items():
                        print(f'{keys} = {value}\n')
                    break
                else:
                    print('Peça não encontrada.\n')
                break


        s_lote = int(input('Qual o lote do produto? >>\n'))
        peca = next((p for p in LISTA_PECA if p['lote'] == s_lote), None)
        if peca:
            LISTA_PECA.remove(peca)
            print('Peça de roupa removida com sucesso\n')

