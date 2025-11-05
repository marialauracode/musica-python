import time # biblioteca que possui o comando time.sleep()
import sys # biblioteca que controla a saída de caracteres no terminal

def print_lyrics():
    lyrics = [
        " Maybe it's 6:45", 
        "Maybe I'm barely alive",
        "Maybe you've taken my shit for the last time, yeah",
        "Maybe I know that I'm drunk",
        "Maybe I know you're the one",
        "Maybe you thinking it's better if you drive",
        ".......Oh, 'cause girls like you run 'round with guys like me",
        "Til sun down when I come through",
        "I need a girl like you, yeah"
    ]

    # tempo de pausa (em segundos)
    delays = [0.7, 0.2, 0.5, 0.5, 0.5, 1.1, 0.5, 0.5, 0.3]
    print("Girls Like you: \n")
    time.sleep(1.2)

    # Primeiro FOR: percorre a lista lyrics
    # enumerate(lyrics): comando que acessa o (índice,elemento)
    # índice seria 0, 1, 2... elemento seria cada linha que está compatível com o índice

    # Segundo FOR: percorre cada letra de cada linha
    # sys.stdout.write(char): imprime cada letra de forma contínua
    # sys.stdout.flush(): garante que cada caractere apareça no terminal no mesmo instante - sem armazenar no buffer
    # time.sleep(0.06): controla a velocidade da digitação

    for i, line in enumerate(lyrics): 
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print() # imprime uma linha vazia logo depois da execução da linha anterior
        time.sleep(delays[i]) # há uma pausa de cada índice conforme a lista delays

print_lyrics()
