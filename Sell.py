
"""
Classe Sell
Utilizada para representar uma Venda.

Propriedades:
IDPART (int) - ID da parte vendida
NAME (str) - Nome da parte vendida, para fins de facilidade no relatório
AMOUNT (int) - Quantidade vendida
PRICE (float) - Preço da venda, calculado a partir da quantidade vendida * preço da preça
"""


class Sell:

    """
        Construtor Sell
    """
    def __init__(self, control, partIndex, amount):
        part = control.parts[partIndex]
        self.idPart = part.id
        self.namePart = part.name
        self.amount = amount
        self.price = int(amount) * float(part.price)

    """
        Impressão da venda.
    """
    def print(self):
        print("-".center(42, '-'))

        print("|", end='')
        print("ID PART:".center(20, ' '), end='|')
        print(str(self.idPart).center(20, ' '), end='|\n')

        print("|", end='')
        print("NAME:".center(20, ' '), end='|')
        print(str(self.namePart).center(20, ' '), end='|\n')

        print("|", end='')
        print("AMOUNT:".center(20, ' '), end='|')
        print(str(self.amount).center(20, ' '), end='|\n')

        print("|", end='')
        print("PRICE:".center(20, ' '), end='|')
        print(("$ "+str(self.price)).center(20, ' '), end='|\n')
        print("-".center(42, '-'))

