
"""
Classe Peça
Utilizada para representar uma Peça.

Propriedades:
ID (int) - unique
NAME (str) - unique
CATEGORY (int) - between 1-20
PRICE (float) - price > 0
AMOUNT (int) - amount > 0
"""

from Util import is_int, is_float


class Part:

    """
        Construtor Part
    """
    def __init__(self, id, name, category, price, amount, control=None):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.amount = amount
        self.validatePart(control, True)

    """
        Asserts para validar se uma parte é ou não válida.
        Uma parte NÃO é válida se:
            - ID NÃO É INT
            - ID MENOR QUE 1
            - ID JÁ EXISTE
            
            - NOME NÃO É STR
            - NOME JÁ EXISTE
            
            - CATEGORIA NÃO É INT
            - CATEGORIA NÃO É ENTRE 1 - 20
            
            - PREÇO NÃO É FLOAT
            - PREÇO MENOR QUE 1
            
            - QUANTIDADE NÃO É INT
            - QUANTIDADE MENOR QUE 1
    """
    def validatePart(self, control=None, edit=True):

        if edit:
            assert (is_int(self.id)), "ID TYPE EXPECTED <class 'int'>, VALUE RECEIVED: %r" % self.id
            id = int(self.id)
            assert (id > 0), "ID MUST BE > 0, RECEIVED: %r" % id
            if control is not None:
                assert (str(self.id) not in control.partsIds), "ID %r ALREADY EXISTS!" % self.id

            assert (type(self.name) is str), "NAME TYPE EXPECTED: <class 'str'>, RECEIVED: %r" % self.name
            if control is not None:
                assert (self.name.lower() not in control.partsNames), "NAME %r ALREADY EXISTS!" % self.name

        assert (is_int(self.category)), "CATEGORY TYPE EXPECTED: <class 'int'>, RECEIVED: %r" % self.category
        category = int(self.category)
        assert (category in list(range(1, 21))), "CATEGORY MUST BE BETWEEN 1 - 20, RECEIVED: %r" % category

        assert (is_float(self.price)), "PRICE TYPE EXPECTED: <class 'float'>, RECEIVED: %r" % self.price
        price = float(self.price)
        assert (price > 0), "PRICE MUST BE > 0, RECEIVED: %r" % price

        assert (is_int(self.amount)), "AMOUNT TYPE EXPECTED: <class 'int'>, RECEIVED: %r" % self.amount
        amount = int(self.amount)
        assert (amount >= 0), "AMOUNT MUST BE >= 0, RECEIVED: %r" % amount

    """
        Impressão de todas as propriedades da parte
    """
    def print(self):
        print("-".center(42, '-'))

        print("|", end='')
        print("ID:".center(20, ' '), end='|')
        print(str(self.id).center(20, ' '), end='|\n')

        print("|", end='')
        print("NAME:".center(20, ' '), end='|')
        print(str(self.name).center(20, ' '), end='|\n')

        print("|", end='')
        print("CATEGORY:".center(20, ' '), end='|')
        print(str(self.category).center(20, ' '), end='|\n')

        print("|", end='')
        print("AMOUNT:".center(20, ' '), end='|')
        print(str(self.amount).center(20, ' '), end='|\n')

        print("|", end='')
        print("PRICE:".center(20, ' '), end='|')
        print(("$ "+str(self.price)).center(20, ' '), end='|\n')

        print("-".center(42, '-'))
