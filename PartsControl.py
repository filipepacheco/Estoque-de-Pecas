# coding=utf-8
from Part import Part
from Util import clearConsole
from copy import copy
from Sell import Sell
from pickle import dump, load

"""
Classe PartsControl

Propriedades:
PARTS (list) - Lista de Part, contendo todas as partes cadastradas
PARTSIDS (list) - Lista de INT, contendo todos os IDS das partes para facilitar controle de IDS repetidas
PARTSNAMES (list) - Lista de STR, contendo todos os NAMES das partes para facilitar controle de NAMES repetidas
SELLINGS (list) - Lista de Sell, contendo todas as vendas feitas.
    
"""


class PartsControl:
    def __init__(self, parts=[]):
        self.parts = parts
        self.partsIds = []
        self.partsNames = []
        self.sellings = []
        for part in parts:
            self.partsIds.append(part.id)
            self.partsNames.append(part.name.lower())

    """
        DESCRIÇÃO:
            1. mostrar todas as pecas cadastradas ou 
            2. mostrar a partir de filtro em campo numérico
                para isto, escolher qual campo numérico (preço por ex.) e definir em seguida os limites inferior e 
                superior. 
                Ex.: mostrar todas peças com preço >= a 45.50 e preço <= a 90.00
                
        FUNCIONALIDADE:
            SE o usuário escolhe listar todas as peças 
                ENTAO loop em todas as peças, imprimindo uma por uma
            SENAO o usuário escolhe filtrar as peças cadastradas
                ENTAO o usuário manualmente digita um argumento que corresponde ao nome da propriedade da classe Sell
                (id, category, price ou amount)
                    SE o usuário fornece apenas um número como argumento
                        ENTAO busca a peça cuja propriedade se encaixa no argumento
                    SENAO o usuário fornece dois números como argumentos
                        ENTAO busca a peça cuja propriedade se encaixa entre os dois argumentos recebidos
    """
    def listParts(self):
        print("1 - List all ")
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
            condition = input("\nType the name of the condition: ")
            if condition != "":
                print("If you input two arguments, then you'll make a search by range (between 1st and 2nd arguments)")
                arg1 = input("First Argument: ")
                if arg1 != "":
                    arg2 = input("Second Argument (OPTIONAL): ")

        parts = self.getPartsByCondtion(condition, arg1, arg2)

        if not parts:
            print("0 parts found.")
        else:
            for part in parts:
                part.print()

    """
        Retorna uma lista de partes que correspondem aos respectivos argumentos.
        condition = nome da propriedade que sera testada (se nao recebido nenhuma condition, retorna todas as peças)
        arg1 = valor a ser procurado
        arg2 = se recebido, transforma a busca em uma busca por range entre arg1 e arg2
    """
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

    """
        Retorna uma lista de indices das partes que correspondem a condicao e argumento recebidos
        condition = nome da propriedade a ser testada
        arg = valor da propriedade em condition
    """
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
        Registra uma nova peça.
        Recebe todas as propriedades a partir do usuario e cria uma nova instancia de Part.
        Testa a Part e trata asserts.
        Caso a Part tenha sido criada com sucesso, popula a lista de partes, a lista de ids e lista de nomes.
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
        Remover peças.
        Para remover uma peça, é solicitado ao usuario que escolha um filtro.
        O usuario escreve o nome da propriedade e o valor dela, para filtrar na lista de Parts.
        A Part é encontrada e removida da lista de partes bom como seu nome e seu ID é removido das 
        respectivas listas auxiliares.
    """
    def remove(self):
        try:
            print("Remove by condition...\n- id\n- name\n- category\n(Enter 0 to exit)")
            condition = input("\nType a condition: ")
            if condition == '0':
                return True
            arg = input("Argument: ")

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
        O usuário primeiro escolhe a condicao para filtrar a peça a ser editado.
        Após, a peça encontrada é impressa na tela.
        Então ele entra em modo de ediçnao e é solicitado ao usuário qual propriedade da Part será editada e seu 
        novo valor.
    """
    def edit(self):
        try:
            print("Edit by condition...\n- id\n- name")
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

    """
        Edita uma Part.
        Recebe o indice da Part, a propriedade a ser alterada e o novo valor dela.
        Após a edição, a Part é validada e realiza os asserts necessários.
    """
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
        O usuário filtra uma peça por alguma condição e define quantas unidades desta peça serão vendidas.
        Após o usuário informar a quantidade de vendas, uma nova instância de Sell é criada e append na lista de vendas.
    """
    def sell(self):
        try:
            print("Sell by condition...\n- id\n- name")
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

    """
        Imprime um relatório de todas as vendas, com os detalhes da Part vendida, o valor vendido e o total de vendas. 
    """
    def report(self):
        totalSellings = 0
        for sell in self.sellings:
            totalSellings += sell.price
            sell.print()

        if totalSellings == 0:
            print("No sale has been made yet!")
        else:
            print("Total: $ ", totalSellings)

    """
        Salva toda a instância atual da classe PartsControl no arquivo partscontrol.bin
    """
    def export(self):
        with open('partscontrol.bin', 'wb') as pcfile:
            dump(self, pcfile)
            print("Parts and Sellings successfully saved to file partscontrol.bin!")

    """
        Carrega todo o conteudo de partscontrol.bin para uma nova instancia da classe PartsControl.
    """
    def importParts(self):
        with open('partscontrol.bin', 'rb') as pcfile:
            fileParts = load(pcfile)
            self.parts = fileParts.parts
            self.partsIds = fileParts.partsIds
            self.partsNames = fileParts.partsNames
            self.sellings = fileParts.sellings
            print("Parts and Sellings successfully loaded from file partscontrol.bin!")

