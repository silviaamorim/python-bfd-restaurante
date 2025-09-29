# classes.py

class Endereco:
    def __init__(self, cep, rua, numero, bairro, cidade, estado):
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - CEP: {self.cep}"


class Pessoa:
    def __init__(self, nome, cpf, telefone, endereco: Endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco

    def apresentar(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Tel: {self.telefone}\nEndereço: {self.endereco}"


class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco: Endereco, codigo):
        super().__init__(nome, cpf, telefone, endereco)
        self.codigo = codigo

    def apresentar(self):
        return f"[Cliente {self.codigo}] {super().apresentar()}"


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco: Endereco, cargo):
        super().__init__(nome, cpf, telefone, endereco)
        self.cargo = cargo

    def apresentar(self):
        return f"[Funcionário: {self.cargo}] {super().apresentar()}"


class Produto:
    def __init__(self, descricao, valor, codigo):
        self.codigo = codigo
        self.descricao = descricao
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
            f"Pedido {self.codigo}: {self.produto.descricao} - R${self.produto.valor:.2f}\n"
            f"Cliente: {self.cliente.nome}\n"
            f"Atendido por: {self.funcionario.nome} ({self.funcionario.cargo})"
        )
