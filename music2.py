import time
import sys

def print_lyrics():
    lyrics = [
        "Quando a luz dos olhos meus",
        "E a luz dos olhos teus",
        "Resolvem se encontrar",
        "Ai que bom que isso é meu Deus",
        "Que frio que me dá o encontro desse olhar",
        "Mas se a luz dos olhos teus",
        "Resiste aos olhos meus só pra me provocar",
        "Meu amor, juro por Deus, me sinto incendiar",
        "\nMeu amor, juro por Deus",
        "Que a luz dos olhos meus já não pode esperar",
        "Quero a luz dos olhos meus",
        "Na luz dos olhos teus sem mais lará-rará",
        "Pela luz dos olhos teus",
        "Eu acho, meu amor",
        "E só se pode achar",
        "Que a luz dos olhos meus precisa se casar"
    ]

    delays = [0.6, 0.9, 0.8, 1.3, 0.2, 0.7, 1.5, 2.5, 0.6, 1.3, 1.0, 1.0, 1.2, 0.5, 0.6, 1.0, 2.0]

    print("Pela Luz dos Olhos Teus ♥ \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(delays[i])

print_lyrics()
