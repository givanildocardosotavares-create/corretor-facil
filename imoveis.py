from utils import ler_texto, ler_inteiro, ler_valor, confirmar
from clientes import buscar_cliente_por_id

imoveis = []
proximo_id = 1
TIPOS = ["casa", "apartamento", "terreno"]
FINALIDADES = ["venda", "aluguel"]
STATUS = ["disponível", "negociando", "vendido"]

def buscar_imovel_por_id(id_imovel):
    for i in imoveis:
        if i["id"] == id_imovel:
            return i
    return None

def cliente_tem_imoveis(id_cliente):
    for i in imoveis:
        if i["id_proprietario"] == id_cliente:
            return True
    return False

def escolher_opcao(titulo, opcoes):
    for n, o in enumerate(opcoes, 1):
        print(f"{n} - {o}")
    while True:
        op = ler_inteiro(titulo)
        if 1 <= op <= len(opcoes):
            return opcoes[op - 1]
        print("Opção inválida.")

def mostrar_imovel(i):
    dono = buscar_cliente_por_id(i["id_proprietario"])
    nome = dono["nome"] if dono else "?"
    print(f"ID {i['id']} | {i['tipo']} | {i['endereco']} | "
          f"R$ {i['valor']:.2f} | {i['finalidade']} | {i['status']} | "
          f"Proprietário: {nome}")

def cadastrar_imovel():
    global proximo_id
    print("\n--- Cadastrar imóvel ---")
    dono = buscar_cliente_por_id(ler_inteiro("ID do proprietário: "))
    if dono is None:
        print("Proprietário não encontrado. Cadastre o cliente primeiro.")
        return
    if dono["tipo"] != "proprietário":
        print("Só clientes do tipo proprietário podem ter imóveis.")
        return
    endereco = ler_texto("Endereço: ")
    tipo = escolher_opcao("Tipo: ", TIPOS)
    valor = ler_valor("Valor (R$): ")
    finalidade = escolher_opcao("Finalidade: ", FINALIDADES)
    imoveis.append({"id": proximo_id, "endereco": endereco, "tipo": tipo,
                    "valor": valor, "finalidade": finalidade,
                    "status": "disponível", "id_proprietario": dono["id"]})
    print(f"Imóvel cadastrado com ID {proximo_id}.")
    proximo_id += 1

def listar_imoveis():
    print("\n--- Lista de imóveis ---")
    if not imoveis:
        print("Nenhum imóvel cadastrado.")
        return
    for i in imoveis:
        mostrar_imovel(i)

def consultar_imovel():
    i = buscar_imovel_por_id(ler_inteiro("ID do imóvel: "))
    if i is None:
        print("Imóvel não encontrado.")
    else:
        mostrar_imovel(i)

def alterar_imovel():
    i = buscar_imovel_por_id(ler_inteiro("ID do imóvel: "))
    if i is None:
        print("Imóvel não encontrado.")
        return
    if i["status"] == "vendido":
        print("Imóvel vendido não pode ser alterado.")
        return
    print("Enter mantém o valor atual.")
    i["endereco"] = input(f"Endereço [{i['endereco']}]: ").strip() or i["endereco"]
    if confirmar("Alterar o valor?"):
        i["valor"] = ler_valor("Novo valor (R$): ")
    if confirmar("Alterar o status?"):
        i["status"] = escolher_opcao("Status: ", STATUS)
    print("Imóvel alterado.")

def excluir_imovel():
    i = buscar_imovel_por_id(ler_inteiro("ID do imóvel: "))
    if i is None:
        print("Imóvel não encontrado.")
        return
    if confirmar(f"Excluir o imóvel {i['endereco']}?"):
        imoveis.remove(i)
        print("Imóvel excluído.")

def menu_imoveis():
    while True:
        print("\n=== IMÓVEIS ===")
        print("1 - Cadastrar\n2 - Listar\n3 - Consultar")
        print("4 - Alterar\n5 - Excluir\n0 - Voltar")
        op = ler_inteiro("Opção: ")
        if op == 1: cadastrar_imovel()
        elif op == 2: listar_imoveis()
        elif op == 3: consultar_imovel()
        elif op == 4: alterar_imovel()
        elif op == 5: excluir_imovel()
        elif op == 0: break
        else: print("Opção inválida.")