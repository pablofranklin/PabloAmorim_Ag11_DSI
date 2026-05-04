from colorama import Fore, Style, init

init(autoreset=True)

niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

print("=" * 40)
print("  SISTEMA DE MONITORAMENTO - RESERVATÓRIO")
print("=" * 40)

for i in range(len(niveis)):
    cor = definir_cor(i + 1)
    print(cor + niveis[i])

print(Style.RESET_ALL)
print("=" * 40)
print("Monitoramento concluído.")