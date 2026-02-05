import sys
from rich import print
from time import sleep

def printLyrics():
    lines = [

    ("Eu vejo tua cara e teu querer perverso", 0.12),
    ("A gente fica bem aqui no chão da sala", 0.11),
    ("Eu te queria a vida toda, te confesso", 0.11),
    ("Por mim, a gente nem precisa mais da estrada", 0.08),
    ("Eu vejo você longe e quero você perto", 0.11),           
    ("Fica na minha sombra, eu posso ser teu rastro", 0.09),
    ("Não quero tu na linha, Vivo, morto ou Claro", 0.11),
    ("Eu quero tu na minha boca", 0.12),
    ("E a minha boca quer você", 0.20),
    ("Quer você", 0.33),
    ("Diga pra mim que é real", 0.22),
    ("Que eu te prometo meu melhor", 0.11),
    ("Fala pra mim o que eu quero ouvir", 0.15),
    ("Que tu sentiu o que eu senti", 0.21),
]

    delays = [ 0.5, 0.5, 0.6, 0.4,
    0.5, 0.5, 0.5, 0.4,
    0.4, 0.6, 0.4, 0.4,
    0.4, 1]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            if line == "Eu vejo você longe e quero você perto":
                print(f"[bold italic violet]{char}[/bold italic violet]", end="")
            else:
                print(f"[bold italic purple]{char}[/bold italic purple]", end="")
            sys.stdout.flush()
            sleep(char_delay)
        print()
        sleep(delays[i])

printLyrics()
 