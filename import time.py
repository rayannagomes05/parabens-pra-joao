import time
import sys
import random
from colorama import Fore, Style, init

# Inicializa o colorama para funcionar no Windows e Linux
init(autoreset=True)

def digitar_efeito(texto, velocidade=0.05):
    """Faz o texto aparecer como se estivesse sendo digitado."""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def animacao_final():
    """Cria uma explosão de cores e confetes."""
    cores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    formatos = ["*", "°", "•", "🎉", "✨", "🎈"]
    
    print("\n" + "="*40)
    for _ in range(15):
        linha = ""
        for _ in range(40):
            cor = random.choice(cores)
            formato = random.choice(formatos)
            linha += f"{cor}{formato} "
        print(linha)
        time.sleep(0.1)
    print("="*40)

def parabens_animado(nome):
    print("\n" + Style.BRIGHT + Fore.CYAN + "--- MENSAGEM RECEBIDA ---")
    time.sleep(1)
    
    digitar_efeito(f"{Fore.YELLOW}Iniciando protocolos de celebração...")
    time.sleep(0.5)
    
    print(f"\n{Fore.GREEN}Preparando o bolo... 🎂")
    time.sleep(0.8)
    print(f"{Fore.GREEN}Enchendo os balões... 🎈")
    time.sleep(0.8)
    print(f"{Fore.GREEN}Aumentando o som... 🎶\n")
    time.sleep(1)

    # O grande momento
    texto_principal = f"✨ PARABÉNS, {nome.upper()}!!! ✨"
    print(Style.BRIGHT + Fore.MAGENTA + "!" * (len(texto_principal) + 4))
    digitar_efeito(f"! {texto_principal} !", velocidade=0.1)
    print(Style.BRIGHT + Fore.MAGENTA + "!" * (len(texto_principal) + 4))
    
    animacao_final()
    
    print(f"\n{Style.BRIGHT}{Fore.WHITE}Que seu dia seja incrível e seu código rode sem erros! 🚀")

# --- EXECUÇÃO ---
nome_aniversariante = input("Quem é a pessoa incrível de hoje? ")
parabens_animado("João Pedro")