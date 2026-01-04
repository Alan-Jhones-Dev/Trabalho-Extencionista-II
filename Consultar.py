from codigo.Const import PECA_SUPERIOR, PECA_INFERIROR, CALCADO, ACESSORIO, EQUIPAMENTO_ELETRONICO


class Consultar:
    def __init__(self):
        pass

    def consultando(self, lista_consulta): # VERIFICA SE EXISTEM PEÇAS NA LISTA ESCOLHIDA
        produto = 'Não contem peças no estoque' if not lista_consulta else lista_consulta # CONSULTA COM OPERADOR TERNARIO
        print(produto)

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

            classificar = int(input('Qual classificação está a peça desejada?\n'))


            if classificar == 1:
                self.consultando(PECA_SUPERIOR)
                break
            elif classificar == 2:
                self.consultando(PECA_INFERIROR)
                break
            elif classificar == 3:
                self.consultando(CALCADO)
                break
            elif classificar == 4:
                self.consultando(ACESSORIO)
                break
            elif classificar == 5:
                self.consultando(EQUIPAMENTO_ELETRONICO)
                break
            elif classificar == 6:
                break
            else:
                print('Classificação invalida!')
                continue
