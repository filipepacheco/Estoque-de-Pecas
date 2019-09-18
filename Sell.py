
class Sell:

    def __init__(self, control, partIndex, amount):
        part = control.parts[partIndex]
        self.idPart = part.id
        self.namePart = part.name
        self.amount = amount
        self.price = int(amount) * int(part.price)

    def print(self):
        print("-------------------------------")
        print("| ID PART: \t\t\t|\t", self.idPart, "\t\t|")
        print("| NAME PART: \t\t\t|\t", self.namePart, "\t\t|")
        print("| AMOUNT: \t|\t", self.amount, "\t\t|")
        print("| PRICE: \t\t|\t$", self.price, "\t|")
        print("-------------------------------")
