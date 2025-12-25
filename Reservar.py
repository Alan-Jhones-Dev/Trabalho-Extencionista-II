class Reservar:
    def __init__(self):
        pass

    def run(self):
        while True:
            print()
            print('Diga o lote da peça que você deseja reservar:')
            print()
            id_lote = int(input('Digite aqui:'))

            peca = next((p for p in lista_peca if p['lote'] == id_lote), None)

            if peca is not None:
                lista_reserva.append(peca.copy())  # adiciona a "PEÇA" dentro da lista_reserva

                for keys, value in peca.items():
                    print(f'{keys} = {value}')
                print()
                print('Produto reservado com sucesso')
                menu_consumidor()
            else:
                print()
                print('Peça não encontrada com esse Lote')
                menu_consumidor()

            break