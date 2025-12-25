from codigo.Cadastrar import Cadastrar
from codigo.Const import LOTE_GERAL
from codigo.Consultar import Consultar
from codigo.Remover import Remover


class Comerciante:
    def __init__(self):
        pass

    def run(self):
        while True:
            try:
                print('Escolha a opção desejável:')
                print('1. Cadastrar peça')
                print('2. Consultar peça')
                print('3. Remover peça')
                print('4. Fechar Aplicativo')

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
                    Remover().run()
                    continue
                elif opcao == 4:
                    raise SystemExit('Programa encerrado com sucesso')
                else:
                    print('\nEscolha invalida. Tente novamente.\n')
                    continue
            except ValueError:
                print('\nValor invalido. Digite apenas números.\n')
                continue
