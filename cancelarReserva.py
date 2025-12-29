from codigo.Const import LISTA_RESERVA

class CancelarReserva:
    def __init__(self):
        pass

    def RemoverProduto(self, valorLote):

        valorLote = next((p for p in LISTA_RESERVA if p['Lote'] == valorLote), None)

        if valorLote is None:
            print('Lista de reserva inexistente')

        else:
            LISTA_RESERVA.remove(valorLote)
            print('Produto removido com sucesso!\n')
            print('lista de reservas atualizadas:')
            print(LISTA_RESERVA)


    def run(self):
        if not LISTA_RESERVA:
            print('Não existem produtos reservados"')
        else:
            print('Lista de Reservas:')
            print(LISTA_RESERVA)

        while True:
            print('Qual o lote do produto você deseja cancelar?')
            produto = int(input('>>>'))

            self.RemoverProduto(produto)
            break



