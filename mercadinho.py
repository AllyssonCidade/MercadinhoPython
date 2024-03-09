class Cliente:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

class Produto:
    def __init__(self, codigo, nome, precoCusto, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.precoCusto = precoCusto
        self.precoVenda = precoCusto + (precoCusto * 0.55)  
        self.quantidade = quantidade

class Venda:
    def __init__(self, cliente, produto, quantidade):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.total = self.produto.precoVenda * quantidade 
        
class MinhaLoja:
    def __init__(self):
        self.clientes = []
        self.produtos = []

    def cadastrar_cliente(self, codigo, nome):
        cliente = Cliente(codigo, nome)
        self.clientes.append(cliente)

    def cadastrar_produto(self, codigo, nome, precoCusto, quantidade):
        produto = Produto(codigo, nome, precoCusto, quantidade)
        self.produtos.append(produto)

    def realizar_venda(self, codigo_cliente, codigo_produto, quantidade):
        cliente = None
        for c in self.clientes:
            if c.codigo == codigo_cliente:
                cliente = c
                break

        if cliente is None:
            print("Cliente não encontrado!")
            return

        produto = None
        for p in self.produtos:
            if p.codigo == codigo_produto:
                produto = p
                break

        if produto is None:
            print("Produto não encontrado!")
            return

        if quantidade > produto.quantidade:
            print("SaldoInsuficiente")
            return

        venda = Venda(cliente, produto, quantidade)
        produto.quantidade -= quantidade
        print("Venda realizada com sucesso!")
