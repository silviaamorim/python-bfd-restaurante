# main.py
from classes import Cliente, Funcionario, Produto, Pedido

clientes = [
    Cliente ("Ana Silva", "123.456.789-00", "(11) 91234-5678", "1"),
    Cliente ("Bruno Souza", "987.654.321-00", "(21) 99876-5432", "2"),
]
funcionarios = [
    Funcionario ("Carlos Pereira", "111.222.333-44", "(31) 91111-2222", "Garçom"),
    Funcionario("Diana Costa", "555.666.777-88", "(41) 93333-4444", "Cozinheira"),
]
pedidos = []

# 🔹 Lista inicial de produtos
produtos = [
    Produto(1, "Risoto com Ababora","Suco Laranja", "Sorvete de Maracujá", 50.90),
    Produto(2, "Strogonff Vegano", "Suco de Cajú", "Mousse de chocolate", 45.50),
    Produto(3, "Moqueca de Palmito", "Suco de Acerola", "Torta vegana de Limão", 47.20),
]

def cadastrar_cliente():
    print("\n=== CADASTRO DE CLIENTE ===")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    codigo = input("Código do cliente: ")

    cliente = Cliente(nome, cpf, telefone, codigo)
    clientes.append(cliente) # adiciona o objeto cliente ao final da lista clientes
    print("Cliente cadastrado com sucesso!")

def cadastrar_funcionario():
    print("\n=== CADASTRO DE FUNCIONÁRIO ===")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    cargo = input("Cargo: ")

    funcionario = Funcionario(nome, cpf, telefone, cargo)
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")


def cadastrar_produto():
    print("\n=== CADASTRO DE PRODUTO ===")
    codigo = input("Código do produto: ")
    descricao = input("Descrição: ")
    suco = input("Suco: ")
    sobremesa = input("Sobremesa: ")
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
    for c in clientes:
        print(f"Código: {c.codigo} | Nome: {c.nome} ({c.cpf})")

    codigo_cliente = input("Digite o código do cliente: ")

    # procurar o cliente com esse código
    cliente = None
    for c in clientes:
        if str(c.codigo) == codigo_cliente:
            cliente = c
            break

    if cliente is None:
        print("⚠ Cliente não encontrado!")
    else:
        print(f"✅ Cliente selecionado: {cliente.nome}")

    # Escolher funcionário
    print("\n-- Funcionários disponíveis --")
    for i, f in enumerate(funcionarios):
        print(f"{i} - {f.nome} ({f.cargo})")
    idx_func = int(input("Escolha o funcionário (número): "))
    funcionario = funcionarios[idx_func]


    # Escolher produto
    print("\n-- Produtos disponíveis --")
    for i, p in enumerate(produtos):
       
        print(f"{i} - {p.descricao} + {p.suco} + {p.sobremesa} | Preço:R$ ({p.valor:.2f})")
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

# 🔹  FUNÇÃO: Excluir pedido
def excluir_pedido():
    print("\n=== EXCLUSÃO DE PEDIDO ===")
    if not pedidos:
        print("Nenhum pedido cadastrado para excluir.")
        return

    listar_pedidos()
    codigo = input("Digite o código do pedido que deseja excluir: ")

    pedido_encontrado = None
    for p in pedidos:
        if str(p.codigo) == codigo:
            pedido_encontrado = p
            break

    if pedido_encontrado:
        pedidos.remove(pedido_encontrado)
        print(f"✅ Pedido {codigo} excluído com sucesso!")
    else:
        print("⚠ Pedido não encontrado!")
def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Funcionário")
        print("3 - Cadastrar Produto")
        print("4 - Cadastrar Pedido")
        print("5 - Listar Pedidos")
        print("6 - Excluir Pedido")
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
        elif opcao == "6":
            excluir_pedido()
        elif opcao == "0":
            print("Saindo do sistema... 👋")
            break
        else:
            print("⚠️ Opção inválida!")

if __name__ == "__main__":
    menu()