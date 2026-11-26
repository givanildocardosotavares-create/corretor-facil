from clientes import clientes
from imoveis import imoveis, mostrar_imovel
from utils import ler_inteiro

def imoveis_disponiveis():
    print("\n--- Imóveis disponíveis ---")
    achou = False
    for i in imoveis:
        if i["status"] == "disponível":
            mostrar_imovel(i)
            achou = True
    if not achou:
        print("Nenhum imóvel disponível.")

def resumo_por_status():
    print("\n--- Resumo por status ---")
    for status in ["disponível", "negociando", "vendido"]:
        lista = [i for i in imoveis if i["status"] == status]
        total = sum(i["valor"] for i in lista)
        print(f"{status}: {len(lista)} imóvel(is) | R$ {total:.2f}")

def imoveis_por_proprietario():
    print("\n--- Imóveis por proprietário ---")
    for c in clientes:
        qtd = len([i for i in imoveis if i["id_proprietario"] == c["id"]])
        if qtd > 0:
            print(f"{c['nome']}: {qtd} imóvel(is)")

def menu_relatorios():
    while True:
        print("\n=== RELATÓRIOS ===")
        print("1 - Imóveis disponíveis")
        print("2 - Resumo por status")
        print("3 - Imóveis por proprietário")
        print("0 - Voltar")
        op = ler_inteiro("Opção: ")
        if op == 1: imoveis_disponiveis()
        elif op == 2: resumo_por_status()
        elif op == 3: imoveis_por_proprietario()
        elif op == 0: break
        else: print("Opção inválida.")
