from utils import ler_texto, ler_inteiro, confirmar

clientes = []
proximo_id = 1
TIPOS = ["comprador", "locatário", "proprietário"]

def buscar_cliente_por_id(id_cliente):
    for c in clientes:
        if c["id"] == id_cliente:
            return c
    return None

def telefone_existe(telefone, ignorar_id=None):
    for c in clientes:
        if c["telefone"] == telefone and c["id"] != ignorar_id:
            return True
    return False

def escolher_tipo():
    print("1 - Comprador | 2 - Locatário | 3 - Proprietário")
    while True:
        op = ler_inteiro("Tipo: ")
        if 1 <= op <= 3:
            return TIPOS[op - 1]
        print("Opção inválida.")

def mostrar_cliente(c):
    print(f"ID {c['id']} | {c['nome']} | {c['telefone']} | {c['email']} | {c['tipo']}")

def cadastrar_cliente():
    global proximo_id
    print("\n--- Cadastrar cliente ---")
    nome = ler_texto("Nome: ")
    telefone = ler_texto("Telefone: ")
    if telefone_existe(telefone):
        print("Já existe cliente com esse telefone.")
        return
    email = ler_texto("E-mail: ")
    tipo = escolher_tipo()
    clientes.append({"id": proximo_id, "nome": nome,
                     "telefone": telefone, "email": email, "tipo": tipo})
    print(f"Cliente cadastrado com ID {proximo_id}.")
    proximo_id += 1

def listar_clientes():
    print("\n--- Lista de clientes ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for c in clientes:
        mostrar_cliente(c)

def consultar_cliente():
    c = buscar_cliente_por_id(ler_inteiro("ID do cliente: "))
    if c is None:
        print("Cliente não encontrado.")
    else:
        mostrar_cliente(c)

def alterar_cliente():
    c = buscar_cliente_por_id(ler_inteiro("ID do cliente: "))
    if c is None:
        print("Cliente não encontrado.")
        return
    print("Enter mantém o valor atual.")
    nome = input(f"Nome [{c['nome']}]: ").strip() or c["nome"]
    telefone = input(f"Telefone [{c['telefone']}]: ").strip() or c["telefone"]
    if telefone_existe(telefone, c["id"]):
        print("Já existe outro cliente com esse telefone.")
        return
    email = input(f"E-mail [{c['email']}]: ").strip() or c["email"]
    c["nome"], c["telefone"], c["email"] = nome, telefone, email
    if confirmar("Alterar o tipo?"):
        c["tipo"] = escolher_tipo()
    print("Cliente alterado.")

def excluir_cliente():
    c = buscar_cliente_por_id(ler_inteiro("ID do cliente: "))
    if c is None:
        print("Cliente não encontrado.")
        return
    if confirmar(f"Excluir {c['nome']}?"):
        clientes.remove(c)
        print("Cliente excluído.")

def menu_clientes():
    while True:
        print("\n=== CLIENTES ===")
        print("1 - Cadastrar\n2 - Listar\n3 - Consultar")
        print("4 - Alterar\n5 - Excluir\n0 - Voltar")
        op = ler_inteiro("Opção: ")
        if op == 1: cadastrar_cliente()
        elif op == 2: listar_clientes()
        elif op == 3: consultar_cliente()
        elif op == 4: alterar_cliente()
        elif op == 5: excluir_cliente()
        elif op == 0: break
        else: print("Opção inválida.")