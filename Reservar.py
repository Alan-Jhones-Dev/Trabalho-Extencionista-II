
from codigo.Const import PECA_SUPERIOR, PECA_INFERIROR, CALCADO, ACESSORIO, EQUIPAMENTO_ELETRONICO, LISTA_RESERVA

class Reservar:
    def __init__(self):
        pass

    def reservar_produto(self, lista_produtos):
        print(lista_produtos)
        try:
            lote = int(input('Qual lote do produto que deseja reservar? >> '))
        except ValueError:
            print('Digite apenas números.')
            return

        produto = next((p for p in lista_produtos if p['Lote'] == lote), None)

        if produto is None:
            print('❌ Lote inexistente.')
        else:
            LISTA_RESERVA.append(produto)
            print('✅ Produto reservado com sucesso!')
            print('Lista de reservas:')
            print(LISTA_RESERVA)

    def run(self):
        if not LISTA_RESERVA:
            print('Você ainda não reservou nada\n')
        else:
            print('Sua lista de reservas:')
            print(LISTA_RESERVA)

        while True:
            print('\nQual a classificação do produto que deseja reservar?')
            print('1. Parte Superior')
            print('2. Parte Inferior')
            print('3. Calçados')
            print('4. Acessórios')
            print('5. Equipamentos Eletrônicos')
            print('0. Sair')

            try:
                opcao = int(input('>> '))
            except ValueError:
                print('Digite apenas números.')
                continue

            if opcao == 1:
                self.reservar_produto(PECA_SUPERIOR)
            elif opcao == 2:
                self.reservar_produto(PECA_INFERIROR)
            elif opcao == 3:
                self.reservar_produto(CALCADO)
            elif opcao == 4:
                self.reservar_produto(ACESSORIO)
            elif opcao == 5:
                self.reservar_produto(EQUIPAMENTO_ELETRONICO)
            elif opcao == 0:
                print('Saindo...')
                break
            else:
                print('Opção inválida.')