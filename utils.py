def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Campo obrigatório.")

def ler_inteiro(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit():
            return int(valor)
        print("Digite um número inteiro válido.")

def ler_valor(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(valor)
            if numero > 0:
                return numero
            print("O valor deve ser maior que zero.")
        except ValueError:
            print("Digite um número válido.")

def confirmar(mensagem):
    return input(mensagem + " (s/n): ").strip().lower() == "s"