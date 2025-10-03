# classes.py

class Pessoa:
   
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        
    def apresentar(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Tel: {self.telefone}"

class Cliente(Pessoa):
    #def __init__(self, nome, cpf, telefone, endereco: Endereco, codigo):
    def __init__(self, nome, cpf, telefone, codigo):
        super().__init__(nome, cpf, telefone)
        self.codigo = codigo

    def apresentar(self):
        return f"[Cliente {self.codigo}] {super().apresentar()}"

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, cargo):
        super().__init__(nome, cpf, telefone)
        self.cargo = cargo

    def apresentar(self):
        return f"[Funcionário: {self.cargo}] {super().apresentar()}"

class Produto:
    def __init__(self, codigo, descricao, suco, sobremesa, valor):
        self.codigo = codigo
        self.descricao = descricao
        self.suco = suco
        self.sobremesa = sobremesa
        self.valor = valor

    def __str__(self):
        return f"[{self.codigo}] {self.descricao} - R${self.valor:.2f}"

class Pedido:
    def __init__(self, codigo, cliente: Cliente, funcionario: Funcionario, produto: Produto):
        self.codigo = codigo
        self.cliente = cliente
        self.funcionario = funcionario
        self.produto = produto
        
    def apresentar(self):
        return (
            f"Pedido {self.codigo}: {self.produto.descricao} + {self.produto.suco} + {self.produto.sobremesa} "
            f"- R${self.produto.valor:.2f}\n"
            f"Atendido por: {self.funcionario.nome} ({self.funcionario.cargo})"
        )
