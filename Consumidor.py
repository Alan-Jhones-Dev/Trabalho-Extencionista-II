from codigo.Consultar import Consultar
from codigo.Reservar import Reservar


class Consumidor:
    def __init__(self):
        pass

    def run(self):
        while True:
            print('Escolha entre as opções:')
            print('1. Consultar Peça')
            print('2. Reservar peça')
            print('3. Cancelar Reserva')
            print('4. Fechar aplicativo\n')

            opcao = int(input('Opção desejada:>>'))

            if opcao == 1:
                Consultar().run()
                continue
            elif opcao == 2:
                Reservar().run()
                continue
            elif opcao == 3:
                pass
            elif opcao == 4:
                raise SystemExit('Programa encerrado com sucesso')

            break
