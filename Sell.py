
class Sell:

    def __init__(self, control, partIndex, amount):
        part = control.parts[partIndex]
        self.idPart = part.id
        self.namePart = part.name
        self.amount = amount
        self.price = int(amount) * float(part.price)

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

        # print("-------------------------------")
        # print("| ID PART: \t\t\t|\t", self.idPart, "\t\t|")
        # print("| NAME PART: \t\t\t|\t", self.namePart, "\t\t|")
        # print("| AMOUNT: \t|\t", self.amount, "\t\t|")
        # print("| PRICE: \t\t|\t$", self.price, "\t|")
        # print("-------------------------------")
