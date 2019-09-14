from Util import is_int, is_float
"""
Estrutura Peça:

codigo (numérico int) //nao pode ser negativo
nome (string)
categoria (int) //valor entre 1 e 20
preco (numérico float) //nao pode ser negativo
quantid (numérico int) //nao pode ser negativo
"""


class Part:

    def __init__(self, id, name, category, price, amount, control=None):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.amount = amount
        self.validatePart(control)

    def validatePart(self, control=None, edit=False):
        assert (is_int(self.id)), "CODE TYPE EXPECTED <class 'int'>, VALUE RECEIVED: %r" % self.id
        id = int(self.id)
        assert (id > 0), "CODE MUST BE > 0, RECEIVED: %r" % id
        if control is not None:
            assert (id not in control.partsIds), "ID %r ALREADY EXISTS!" % id

        assert (type(self.name) is str), "NAME TYPE EXPECTED: <class 'str'>, RECEIVED: %r" % self.name
        if control is not None:
            assert (self.name not in control.partsNames), "NAME %r ALREADY EXISTS!" % self.name

        assert (is_int(self.category)), "CATEGORY TYPE EXPECTED: <class 'int'>, RECEIVED: %r" % self.category
        category = int(self.category)
        assert (category in list(range(1, 21))), "CATEGORY MUST BE BETWEEN 1 - 20, RECEIVED: %r" % category

        assert (is_float(self.price)), "PRICE TYPE EXPECTED: <class 'float'>, RECEIVED: %r" % self.price
        price = float(self.price)
        assert (price > 0), "PRICE MUST BE > 0, RECEIVED: %r" % price

        assert (is_int(self.amount)), "AMOUNT TYPE EXPECTED: <class 'int'>, RECEIVED: %r" % self.amount
        amount = int(self.amount)
        assert (amount > 0), "AMOUNT MUST BE > 0, RECEIVED: %r" % amount

    def print(self):
        print("-------------------------------")
        print("| NAME: \t\t|\t", self.name, "\t\t|")
        print("| ID: \t\t\t|\t", self.id, "\t\t|")
        print("| CATEGORY: \t|\t", self.category, "\t\t|")
        print("| PRICE: \t\t|\t$", self.price, "\t|")
        print("| AMOUNT: \t\t|\t", self.amount, "\t\t|")
        print("-------------------------------")
