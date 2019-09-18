# coding=utf-8
from Part import Part
from Util import clearConsole
from copy import copy
from Sell import Sell


class PartsControl:
    def __init__(self, parts=[]):
        self.parts = parts
        self.partsIds = []
        self.partsNames = []
        self.sellings = []
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
        print("0 - Return to menu")
        option = int(input("Choose and option: "))
        if option == 0:
            return True
        clearConsole()

        condition = ""
        arg1 = ""
        arg2 = ""
        if option != 1:
            print("Filter by...\n- id\n- category\n- price\n- amount")
            condition = input("\nType a condition: ")
            if condition != "":
                arg1 = input("First Argument: ")
                if arg1 != "":
                    arg2 = input("Second Argument (OPTIONAL): ")

        parts = self.getPartsByCondtion(condition, arg1, arg2)

        if not parts:
            print("0 parts found.")
        else:
            for part in parts:
                part.print()

    def getPartsByCondtion(self, condition="", arg1="", arg2=""):
        parts = []

        if len(self.parts) == 0:
            return parts

        if condition == "":
            for part in self.parts:
                parts.append(part)
        else:
            assert (condition in self.parts[0].__dict__.keys()), "ATTRIBUTE %r DOESNT EXISTS!" % condition
            for part in self.parts:
                if arg2 == "":
                    if getattr(part, condition, -1) == arg1:
                        parts.append(part)
                else:
                    if int(getattr(part, condition, -1)) in range(int(arg1), int(arg2) + 1):
                        parts.append(part)
        return parts

    def getPartIndexes(self, condition, arg):
        indexes = []

        if len(self.parts) == 0:
            return indexes

        assert (condition in self.parts[0].__dict__.keys()), "ATTRIBUTE %r DOESNT EXISTS!" % condition
        for index, item in enumerate(self.parts):
            if getattr(item, condition, -1) == arg:
                indexes.append(index)

        return indexes

    """
        2. inserir nova peça no cadastro
        obs.: deve verificar se já não há peça cadastrada com mesmo código e/ou nome; se já houver, 
        gera mensagem de erro e não insere esta peça.
    """
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

    """
        3. remover peça 
        nesta opção primeira ação é o usuário escolher o critério de remoção:
        pelo código
        pelo nome
        pela categoria (remove todas peças desta categoria)
    """

    def remove(self):
        try:
            print("Remove by...\n- id\n- name\n- category\n(Enter 0 to exit)")
            condition = input("\nType a condition: ")
            if condition == '0':
                return True
            arg = input("First Argument: ")

            indexes = self.getPartIndexes(condition, arg)

            for index in indexes:
                del self.parts[index]
                del self.partsIds[index]
                del self.partsNames[index]

        except (AssertionError, ValueError) as Error:
            print("UNABLE TO REMOVE PART.\nERROR:", Error)
        else:
            print("PART SUCCESSFULLY DELETED.")

    """
    4. editar peça
    escolher o critério de seleção:
      pelo código
      pelo nome
    deve permitir a modificação (atualização) dos campos deste item
    """
    def edit(self):
        try:
            print("Edit by...\n- id\n- name")
            condition = input("\nType a condition (Enter 0 to exit): ")
            if condition == '0':
                return True
            arg = input("First Argument: ")

            index = self.getPartIndexes(condition, arg)

            assert (len(index) > 0), "PART NOT FOUND!"
            index = index[0]

            while True:
                self.parts[index].print()
                prop = input("What do you want to edit? (Enter 0 to exit) ")
                if prop == '0':
                    break
                if prop not in self.parts[0].__dict__.keys():
                    print("ATTRIBUTE %r DOESNT EXISTS!" % condition)
                    continue

                newValue = input("New value: ")
                self.editPart(index, prop, newValue)
        except (AssertionError, ValueError) as Error:
            print("UNABLE TO EDIT NEW PART.\nERROR:", Error)
        else:
            print("PART SUCCESSFULLY EDITED.")

    def editPart(self, index, prop, newValue):
        newPart = copy(self.parts[index])
        setattr(newPart, prop, newValue)
        validateEdit = False
        if prop == 'id' or prop == 'name':
            validateEdit = True
        newPart.validatePart(self, validateEdit)
        self.parts[index] = newPart
        self.partsNames[index] = newPart.name
        self.partsIds[index] = newPart.id

    """
    5. vender peça
    identificar a peça (pelo código ou nome)
    solicitar pelo teclado a quantidade vendida (não permitir estoque negativo)
    atualizar campo quantid da peça vendida
    """
    def sell(self):
        try:
            print("Sell by...\n- id\n- name")
            condition = input("\nType a condition (Enter 0 to exit): ")
            if condition == '0':
                return True

            index = self.getPartIndexes(condition, input("First Argument: "))
            assert (len(index) > 0), "PART NOT FOUND!"

            index = index[0]
            self.parts[index].print()
            sellAmount = int(input("How much you want to sell? "))
            self.editPart(index, "amount", int(self.parts[index].amount) - sellAmount)
        except (AssertionError, ValueError, AttributeError) as Error:
            print("UNABLE TO SELL NEW PART.\nERROR:", Error)
        else:
            print("PART SUCCESSFULLY SOLD!")
            self.sellings.append(Sell(self, index, sellAmount))
            print(self.sellings)

    """
    6. mostrar relatorio de vendas
    listar todas vendas efetuadas:
    para cada venda efetuada mostrar,
        codigo e nome da peça vendida
        quantidade vendida daquela peça
        valor desta venda
        mostrar valor total (somatório) das vendas    
    """
    def report(self):
        totalSellings = 0
        for sell in self.sellings:
            totalSellings += sell.price
            sell.print()

        print("Total: $ ", totalSellings)

    # def export(self):
    #
    # def upload(self):

