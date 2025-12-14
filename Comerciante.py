from codigo.Cadastrar import Cadastrar
from codigo.Const import LOTE_GERAL


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
            print()
            if opcao == 1:
                LOTE_GERAL[0] += 1
                novo_cadastro = Cadastrar
                novo_cadastro.run(LOTE_GERAL)
            elif opcao == 2:
                pass
            elif opcao == 3:
                pass
            elif opcao == 4:
                pass
            elif opcao == 5:
                print('Fechando aplicativo...')
            break
