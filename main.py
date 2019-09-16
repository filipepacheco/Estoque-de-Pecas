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
    print("7 - Export")
    print("8 - Upload File")
    print("0 - Exit")
    option = int(input("Choose an option: "))

    if option < 1:
        break

    menu(option, Parts)


"""
Opções:

6. mostrar relatorio de vendas
listar todas vendas efetuadas:
para cada venda efetuada mostrar,
    codigo e nome da peça vendida
    quantidade vendida daquela peça
    valor desta venda
               3. mostrar valor total (somatório) das vendas

7. armazenar (salvar/gravar) cadastro em um arquivo

8. carregar (ler) um cadastro a partir de um arquivo 

Obs.: 
a) organizar as opções em funções
b) mostrar para o usuário um menu de opções; a partir da opção escolhida, 
a função correspondente é então chamada pelo programa.
"""
