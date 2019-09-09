# coding=utf-8
from Part import Part
from Util import is_int, clearConsole


class PartsControl:
    def __init__(self, parts=[]):
        self.parts = parts
        self.partsIds = []
        self.partsNames = []
        for part in parts:
            self.partsIds.append(part.id)
            self.partsNames.append(part.name)

    """
        1. mostrar todas as pecas cadastradas ou 
        2. mostrar a partir de filtro em campo numérico
            para isto, escolher qual campo numérico (preço por ex.) e definir em seguida os limites inferior e superior. 
            Ex.: mostrar todas peças com preço >= a 45.50 e preço <= a 90.00
    """

    def listParts(self):
        print("1 - List all")
        print("2 - Filter by numeric field")
        option = int(input("Choose and option: "))
        clearConsole()

        condition = ""
        arg1 = 0
        arg2 = 0
        if option != 1:
            print("Filter by...\nid\ncategory\nprice\namount")
            condition = input("\nType a condition: ")
            if condition != "":
                arg_aux = input("First Argument (INT): ")
                if is_int(arg_aux):
                    arg1 = int(arg_aux)
                    arg_aux = input("Second Argument (INT - OPTIONAL): ")
                    if is_int(arg_aux):
                        arg2 = int(arg_aux)

        parts = self.filterPartsByCondtion(condition, arg1, arg2)

        if not parts:
            print("0 parts found.")
        else:
            for part in parts:
                part.print()

    def filterPartsByCondtion(self, condition="", arg1=0, arg2=0):
        parts = []
        if condition == "":
            for part in self.parts:
                parts.append(part)
        else:
            for part in self.parts:
                if arg2 == 0:
                    if getattr(part, condition, -1) == arg1:
                        parts.append(part)
                else:
                    if getattr(part, condition, -1) in range(arg1, arg2):
                        parts.append(part)

        return parts

    def register(self):
        try:
            newPart = Part(input("ID: "),
                           input("Name: "),
                           input("Category: "),
                           input("Price: "),
                           input("Amount: "),
                           self)
        except (AssertionError, ValueError) as Error:
            print("UNABLE TO CREATE NEW PART.\nERROR:", Error)
        else:
            self.parts.append(newPart)
            self.partsIds.append(newPart.id)
            self.partsNames.append(newPart.name)
            clearConsole()
            print("PART SUCCESSFULLY REGISTERED.")

    # def remove(self):
    #
    # def edit(self):
    #
    # def sell(self):
    #
    # def report(self):
    #
    # def export(self):
    #
    # def upload(self):

