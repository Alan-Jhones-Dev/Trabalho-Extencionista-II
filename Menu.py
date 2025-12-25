from codigo.Comerciante import Comerciante
from codigo.Consumidor import Consumidor


class Menu:
    def __init__(self):
        pass

    def run(self):
        while True:
            try:
                print(' 1 . Comerciante: \n',
                      '2 . Consumidor:')

                menu_option = int(input('>>'))
                if menu_option == 1:
                    #password
                    Comerciante().run()
                elif menu_option == 2:
                    #password
                    Consumidor().run()
                else:
                    print('Ecolha invalida. Tente novamente')
                    continue
            except ValueError:
                print('Valor invalido! Escolha apenas um dos numeros do painel abaixo:')
                continue


