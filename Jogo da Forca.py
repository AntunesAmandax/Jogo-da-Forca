#Criar uma lista aleatória de palavras
import random 

print("Bem-vindo ao jogo da forca! Vamos começar a jogar.")

palavras = [
    "Cachorro", "Astronauta", "Montanha", "Guitarra", "Chocolate", "Tempestade",
    "Biblioteca", "Avião", "Lua", "Castelo", "Maçã", "Computador", "Praia", "Girassol",
    "Sombra", "Espelho", "Aventura", "Tigre", "Piano", "Aconchegante", "Sussurro",
    "Vento", "Espaço", "Cacto", "Fogueira", "Serenidade", "Arco-íris", "Livro",
    "Café", "Veludo", "Neve", "Elefante", "Balão", "Dança", "Brilho", "Cabana",
    "Mistério", "Trampolim", "Harmonia", "Criança", "Bolo", "Selva", "Aquarela",
    "Farol", "Risada", "Miragem", "Lua cheia", "Tesouro", "Aurora boreal", "Unicórnio"
    ]

#Cria a função sorteio:
def sorteio():
    return random.choice(palavras).lower()

#Cria a função pra exibir a forca:
def forca(vidas):
    if vidas == 0:
        print('''
      -+++++
      |    |
      O    |
    / | \  |
     / \   |
           |
    ==============
   ''')
    elif vidas == 1:
        print('''
      -+++++
      |    |
      O    |
    / | \  |
     /     |
           |
    ==============
''')
    elif vidas == 2:
        print('''
      -+++++
      |    |
      O    |
    / | \  |
           |
           |
    ==============
   ''')
    elif vidas == 3:
        print('''
      -+++++
      |    |
      O    |
    / |    |
           |
           |
    ==============
   ''')
    elif vidas == 4:
        print('''
      -+++++
      |    |
      O    |
     |     |
           |
           |
    ==============
   ''')
    elif vidas == 5:
        print('''
      -+++++
      |    |
      O    |
      |    |
           |
           |
    ==============
   ''')
    elif vidas == 6:
        print('''
      -+++++
      |    |
      O    |
           |
           |
           |
    ==============
   ''')

    elif vidas == 7:
        print('''
      -+++++
      |    |
           |
           |
           |
           |
    ==============
   ''')
        
sorteada = random.choice(palavras)
palavra = sorteada
tam = len(palavra)
adivinhada = "_" * tam
vidas = 6
letras = set()

#Loop principal
while vidas>0 and "_" in adivinhada:
    print()
    print(adivinhada)
    print(f"Vidas restantes: {vidas}")
    print("Letras já escolhidas:", " ".join(letras))
    
    letra = input("Escolha uma letra: ").lower()
    print("A palavra sorteada tem ", len(sorteada), " letras.")
    while letra in letras:
        letra = input("Você já escolheu essa letra. Tente novamente, escolha uma letra:").lower()
    letras.add(letra)

    #Verificar se a letra está na palavra:
    if letra in palavra:
        indices = [i for i, caractere in enumerate(palavra) if caractere == letra]
        for indice in indices:
            adivinhada = adivinhada[:indice] + letra + adivinhada[indice + 1:]
    else:
        vidas -= 1
        print("Letra incorreta, você perdeu uma vida.")
        forca(vidas)

#Checar resultado
if "_" not in adivinhada:
    print("Parabéns, você adivinhou a palavra:", palavra)
else:
    print("Sinto muito, você perdeu... a palavra era:", palavra)
    forca(vidas)



