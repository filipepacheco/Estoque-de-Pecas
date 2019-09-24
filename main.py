from PartsControl import PartsControl
from Util import menu

Parts = PartsControl()

while True:
    print("1 - List")
    print("2 - Register")
    print("3 - Remove")
    print("4 - Edit")
    print("5 - Sell")
    print("6 - Sales Report")
    print("7 - Export (Save to File partscontrol.bin)")
    print("8 - Upload (Load File partscontrol.bin)")
    print("0 - Exit")
    option = int(input("Choose an Option: "))

    if option < 1:
        break

    menu(option, Parts)
