# main.py
from classes import Endereco, Cliente, Funcionario, Produto, Pedido

clientes = []
funcionarios = []
produtos = []
pedidos = []


def cadastrar_cliente():
    print("\n=== CADASTRO DE CLIENTE ===")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    codigo = input("Código do cliente: ")

    print("--- Endereço ---")
    cep = input("CEP: ")
    rua = input("Rua: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")

    endereco = Endereco(cep, rua, numero, bairro, cidade, estado)
    cliente = Cliente(nome, cpf, telefone, endereco, codigo)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")


def cadastrar_funcionario():
    print("\n=== CADASTRO DE FUNCIONÁRIO ===")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    cargo = input("Cargo: ")

    print("--- Endereço ---")
    cep = input("CEP: ")
    rua = input("Rua: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")

    endereco = Endereco(cep, rua, numero, bairro, cidade, estado)
    funcionario = Funcionario(nome, cpf, telefone, endereco, cargo)
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")


def cadastrar_produto():
    print("\n=== CADASTRO DE PRODUTO ===")
    codigo = input("Código do produto: ")
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))

    produto = Produto(descricao, valor, codigo) 
    produtos.append(produto)
    print(" Produto cadastrado com sucesso!")


def cadastrar_pedido():
    if not clientes or not funcionarios or not produtos:
        print("\n É necessário ter pelo menos 1 cliente, 1 funcionário e 1 produto cadastrados!")
        return

    print("\n=== CADASTRO DE PEDIDO ===")
    codigo = input("Código do pedido: ")

    # Escolher cliente
    print("\n-- Clientes disponíveis --")
    for i, c in enumerate(clientes):
        print(f"{i} - {c.nome} ({c.cpf})")
    idx_cliente = int(input("Escolha o cliente (número): "))
    cliente = clientes[idx_cliente]

    # Escolher funcionário
    print("\n-- Funcionários disponíveis --")
    for i, f in enumerate(funcionarios):
        print(f"{i} - {f.nome} ({f.cargo})")
    idx_func = int(input("Escolha o funcionário (número): "))
    funcionario = funcionarios[idx_func]

    # Escolher produto
    print("\n-- Produtos disponíveis --")
    for i, p in enumerate(produtos):
        #print(f"{i} - {p}")
        print(f"{i} - {p.descricao} ({p.valor:.2f})")
    idx_produto = int(input("Escolha o produto (número): "))
    produto = produtos[idx_produto]

    pedido = Pedido(codigo, cliente, funcionario, produto)
    pedidos.append(pedido)
    print(" Pedido cadastrado com sucesso!")


def listar_pedidos():
    print("\n=== LISTA DE PEDIDOS ===")
    if not pedidos:
        print("Nenhum pedido cadastrado.")
        return
    for p in pedidos:
        print(p.apresentar())
        print("-" * 50)


def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Funcionário")
        print("3 - Cadastrar Produto")
        print("4 - Cadastrar Pedido")
        print("5 - Listar Pedidos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_funcionario()
        elif opcao == "3":
            cadastrar_produto()
        elif opcao == "4":
            cadastrar_pedido()
        elif opcao == "5":
            listar_pedidos()
        elif opcao == "0":
            print("Saindo do sistema... 👋")
            break
        else:
            print("⚠️ Opção inválida!")


if __name__ == "__main__":
    menu()
