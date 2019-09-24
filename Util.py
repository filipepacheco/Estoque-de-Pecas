
def menu(option, parts):
    clearConsole()

    if option == 1:
        parts.listParts()
    elif option == 2:
        parts.register()
    elif option == 3:
        parts.remove()
    elif option == 4:
        parts.edit()
    elif option == 5:
        parts.sell()
    elif option == 6:
        parts.report()
    elif option == 7:
        parts.export()
    elif option == 8:
        parts.importParts()
    else:
        print("Invalid option.")


def clearConsole():
    print('\n' * 10)


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_int(val):
    return type(val) == int or (val != "" and val.lstrip("-+").isdigit())
