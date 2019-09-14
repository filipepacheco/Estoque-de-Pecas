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
        arg1 = ""
        arg2 = ""
        if option != 1:
            print("Filter by...\n- id\n- category\n- price\n- amount")
            condition = input("\nType a condition: ")
            if condition != "":
                arg1 = input("First Argument: ")
                if arg1 != "":
                    arg2 = input("Second Argument (OPTIONAL): ")

        parts = self.filterPartsByCondtion(condition, arg1, arg2)

        if not parts:
            print("0 parts found.")
        else:
            for part in parts:
                part.print()

    def filterPartsByCondtion(self, condition="", arg1="", arg2=""):
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
                    if getattr(part, condition, -1) in range(int(arg1), int(arg2)):
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
            print("Remove by...\n- id\n- name\n- category")
            condition = input("\nType a condition: ")
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
            condition = input("\nType a condition: ")
            arg = input("First Argument: ")

            index = self.getPartIndexes(condition, arg)

            assert (len(index) > 0), "PART NOT FOUND!"
            index = index[0]

            while True:
                self.parts[index].print()
                prop = input("What do you want to edit? (Enter 0 to exit) ")
                if prop == 0:
                    break
                if prop not in self.parts[0].__dict__.keys():
                    print("ATTRIBUTE %r DOESNT EXISTS!" % condition)
                    continue

                newValue = input("New value: ")
                newPart = self.parts[index].copy()
                setattr(newPart, prop, newValue)
                self.parts[index].validatePart()

        except (AssertionError, ValueError) as Error:
            print("UNABLE TO EDIT NEW PART.\nERROR:", Error)
        else:
            print("PART SUCCESSFULLY EDITED.")


    # def sell(self):
    #
    # def report(self):
    #
    # def export(self):
    #
    # def upload(self):

