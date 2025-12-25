from codigo.Const import PECA_SUPERIOR, PECA_INFERIROR, CALCADO, ACESSORIO, EQUIPAMENTO_ELETRONICO


class Remover:
    def __init__(self):
        pass

    def run(self):
        while True:
            print('Qual a classificação que deseja remover produtos?')
            print('1. Parte Superior')
            print('2. Parte Inferior')
            print('3. Calçados')
            print('4. Acessórios')
            print('5. Equipamentos Eletrônicos')

            classificar = int(input('Qual classificação está a peça deseja remover? >>\n'))

            match classificar:
                case 1:
                    print(PECA_SUPERIOR)
                case 2:
                    print(PECA_INFERIROR)
                case 3:
                    print(CALCADO)
                case 4:
                    print(ACESSORIO)
                case 5:
                    print(EQUIPAMENTO_ELETRONICO)
                case _:
                    print('classificação invalida')
                    continue

            s_lote = int(input('Qual o lote do produto deseja remover?\n >>'))
            if classificar == 1:
                peca = next((p for p in PECA_SUPERIOR if p['Lote'] == s_lote), None)
                PECA_SUPERIOR.remove(peca)
                print(PECA_SUPERIOR)
                break
            elif classificar == 2:
                peca = next((p for p in PECA_INFERIROR if p['Lote'] == s_lote), None)
                PECA_INFERIROR.remove(peca)
                print(PECA_INFERIROR)
                break
            elif classificar == 3:
                peca = next((p for p in CALCADO if p['Lote'] == s_lote), None)
                CALCADO.remove(peca)
                print(CALCADO)
                break
            elif classificar == 4:
                peca = next((p for p in ACESSORIO if p['Lote'] == s_lote), None)
                ACESSORIO.remove(peca)
                print(ACESSORIO)
                break
            elif classificar == 5:
                peca = next((p for p in EQUIPAMENTO_ELETRONICO if p['Lote'] == s_lote), None)
                EQUIPAMENTO_ELETRONICO.remove(peca)
                print(EQUIPAMENTO_ELETRONICO)
                break
            else:
                print('Lote da classificação invalida')
                continue

        print('Peça de roupa removida com sucesso\n')
