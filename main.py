from PartsControl import PartsControl
from Util import switch

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

    switch(option, Parts)


"""
Opções:

2. inserir nova peça no cadastro
obs.: deve verificar se já não há peça cadastrada com mesmo código e/ou nome; se já houver, 
gera mensagem de erro e não insere esta peça.

3. remover peça 
nesta opção primeira ação é o usuário escolher o critério de remoção:
  pelo código
  pelo nome
  pela categoria (remove todas peças desta categoria)

4. editar peça
escolher o critério de seleção:
  pelo código
  pelo nome
deve permitir a modificação (atualização) dos campos deste item

5. vender peça
identificar a peça (pelo código ou nome)
solicitar pelo teclado a quantidade vendida (não permitir estoque negativo)
atualizar campo quantid da peça vendida

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
