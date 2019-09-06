"""
Estrutura Peça:

codigo (numérico int) //nao pode ser negativo
nome (string)
categoria (int) //valor entre 1 e 20
preco (numérico float) //nao pode ser negativo
quantid (numérico int) //nao pode ser negativo
"""


class Peca:
    def __init__(self, codigo, nome, categoria, preco, qtd):
        self.codigo = codigo  # int
        self.nome = nome  # str
        self.categoria = categoria  # int (1 - 20)
        self.preco = preco  # float > 0
        self.qtd = qtd  # int > 0


class Menu:
    def __init__(self, secoes):
        self.secoes = secoes

    def mostrar(self):
        for i, secao in enumerate(self.secoes):
            print(i, "-", secao.nome)
        userInput = int(input("Escolha uma opção: "))

        secaoEscolhida = self.secoes[userInput]

        for i, secao in enumerate(secaoEscolhida.opcoes):
            print(i, "-", secao.nome)

        userInput = int(input("Escolha uma opção: "))
        secaoEscolhida = secaoEscolhida.opcoes[userInput]
        secaoEscolhida.callback()


class Navegacao:
    def __init__(self, nome, opcoes, callback: callable = ''):
        self.nome = nome
        self.opcoes = opcoes
        self.callback = callback


def mostrarTodasPecas():
    print("hehe")


sec = [
    Navegacao('Mostrar Peças', [
        Navegacao("Tudo", [], mostrarTodasPecas),
        Navegacao("Filtro", [])
    ]),
    Navegacao('Nova Peça', []),
    Navegacao('Remover Peça', [
        Navegacao("Por código", []),
        Navegacao("Por nome", []),
        Navegacao("Por categoria", [])
    ]),
    Navegacao('Editar Peça', [
        Navegacao("Por código", []),
        Navegacao("Por nome", [])
    ]),
    Navegacao('Vender Peça', [
        Navegacao("Por código", []),
        Navegacao("Por nome", [])
    ]),
]

teste = Menu(sec)
teste.mostrar()

"""
Opções:

1. 
mostrar cadastro
    mostrar todo cadastro
    mostrar a partir de filtro em campo numérico
        para isto, escolher qual campo numérico (preço por ex.) e definir em seguida os limites inferior e superior. 
        Ex.: mostrar todas peças com preço >= a 45.50 e preço <= a 90.00

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
