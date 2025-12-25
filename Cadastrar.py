from codigo.Const import PECA_SUPERIOR, PECA_INFERIROR, CALCADO, ACESSORIO, EQUIPAMENTO_ELETRONICO


class Cadastrar:

    def __init__(self):
        pass

    def run(self, lote):
        while True:
            print('A peça esta classificada como:')
            print('1. Parte Superior')
            print('2. Parte Inferior')
            print('3. Calçados')
            print('4. Acessósrios')
            print('5. Equipamentos Eletronicos')
            try:
                classificador = int(input('>>'))
                if not (classificador > 0 and classificador <= 5):
                    print('Opção inválida, tente novamente')
                    continue

                item = input('Descreva: (blusa, short, calça) >>')
                if item.isdigit():
                    print('Opção inválida, tente novamente')
                    continue
                valor = int(input('Qual o valor da peça?'))

                peca = {
                    'Produto': item,
                    'Regiao': classificador,
                    'Valor': valor,
                    'Lote': lote[0]
                }
                match classificador:
                    case 1:
                        PECA_SUPERIOR.append(peca)
                        break
                    case 2:
                        PECA_INFERIROR.append(peca)
                        break
                    case 3:
                        CALCADO.append(peca)
                        break
                    case 4:
                        ACESSORIO.append(peca)
                        break
                    case 5:
                        EQUIPAMENTO_ELETRONICO.append(peca)
                        break
            except ValueError:
                print('Valor invalido, apenas numeros')
                continue

        print('\nProduto cadastrado com sucesso!')
