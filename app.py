from clientes import menu_clientes
from imoveis import menu_imoveis
from utils import ler_inteiro

def main():
    while True:
        print("\n" + "=" * 40)
        print("          CORRETOR FÁCIL")
        print("    Sistema de Gerenciamento")
        print("=" * 40)
        print("MENU PRINCIPAL")
        print("1 - Gerenciar Clientes")
        print("2 - Gerenciar Imóveis")
        print("0 - Sair do Sistema")
        print("=" * 40)
        op = ler_inteiro("Digite a opção desejada: ")
        if op == 1: menu_clientes()
        elif op == 2: menu_imoveis()
        elif op == 0:
            print("Até logo!")
            break
        else: print("Opção inválida.")

main()