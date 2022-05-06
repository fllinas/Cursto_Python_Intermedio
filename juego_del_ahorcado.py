import random
import os

def run():
    words = read()
    word = words[random.randint(0, len(words))]
    underscore = "_ "*len(word)
    print(word)
    intentos = 0
    aciertos = 0
    limite = 5

    while "_" in underscore:
        os.system('cls')
        print("\n")
        print(underscore)
        print("\n")
        letter = input("Inserta una letra: ")
        assert letter.isalpha(), "Solo se permiten letras: "
        aciertos = 0

        for count,ele in enumerate(word):
            if ele == letter:
                underscore = underscore[:2*count] + ele + underscore[2*count+1:]
                aciertos = aciertos + 1

        if aciertos == 0:    
            intentos = intentos + 1

        if intentos >= limite:
            break
        
    
    if intentos >= limite:
        print("\n")
        print("Has Perdido :( , superaste el limite de intentos: " + str(limite))
        
    if "_" not in underscore:
        print("\n")
        print(underscore)
        print("\n")
        print("Has ganado!")


def read():
    words = []
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        for line in f:
            words.append(line.replace('\n', ''))
    return words

if __name__ == "__main__":
    run()