from codigo.Cadastrar import Cadastrar
from codigo.Const import LOTE_GERAL
from codigo.Consultar import Consultar


class Comerciante:
    def __init__(self):
        pass

    def run(self):
        while True:
            print('Escolha a opção desejável:')
            print('1. Cadastrar peça')
            print('2. Consultar peça')
            print('3. Remover peça')
            print('4. Voltar ao inicio')
            print('5. Fechar Aplicativo')

            opcao = int(input('>>'))

            if opcao == 1:
                LOTE_GERAL[0] += 1
                cadastro = Cadastrar()
                cadastro.run(LOTE_GERAL)
                continue
            elif opcao == 2:
                Consultar().run()
                continue
            elif opcao == 3:

                continue
            elif opcao == 4:
                pass
            elif opcao == 5:
                print('Fechando aplicativo...')
            break
