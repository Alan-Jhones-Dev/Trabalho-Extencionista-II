from codigo.Const import PECA_SUPERIOR, PECA_INFERIROR, CALCADO, ACESSORIO, EQUIPAMENTO_ELETRONICO


class Remover:
    def __init__(self):
        pass

    def removendo(self, lista_remocao):
        print(lista_remocao)
        try:
            s_lote = int(input('Qual o lote do produto deseja remover?\n >>'))
        except ValueError:
            print('Apenas numeros!')

        peca = next((p for p in lista_remocao if p['Lote'] == s_lote), None)

        lista_remocao.remove(peca)
        print('Peça de roupa removida com sucesso\n')
        return lista_remocao


    def run(self):
        while True:
            print('Qual a classificação que deseja remover produtos?')
            print('1. Parte Superior')
            print('2. Parte Inferior')
            print('3. Calçados')
            print('4. Acessórios')
            print('5. Equipamentos Eletrônicos')
            print('6. Retornar')

            classificar = int(input(' >>\n'))

            match classificar:
                case 1:
                    if len(PECA_SUPERIOR) == 0:
                        print('Sem produtos no estoque')
                        break
                    else:
                        self.removendo(PECA_SUPERIOR)
                case 2:
                    if len(PECA_INFERIROR) == 0:
                        print('Sem produtos no estoque')
                        break
                    else:
                        self.removendo(PECA_INFERIROR)
                case 3:
                    if len(CALCADO) == 0:
                        print('Sem produtos no estoque')
                        break
                    else:
                        self.removendo(CALCADO)
                case 4:
                    if len(ACESSORIO) == 0:
                        print('Sem produtos no estoque')
                        break
                    else:
                        self.removendo(ACESSORIO)
                case 5:
                    if len(EQUIPAMENTO_ELETRONICO) == 0:
                        print('Sem produtos no estoque')
                        break
                    else:
                        self.removendo(EQUIPAMENTO_ELETRONICO)
                case _:
                    print('classificação invalida')
                    continue
