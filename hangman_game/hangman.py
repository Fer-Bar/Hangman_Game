import random
import os
import time
from words_and_img import WORDS, IMAGES
#Lee los puntajes del archivo txt 
def read_score(path):
    with open(path, "r") as f:
        score = f.read() #Score es del tipo str
        try:
            if int(score) < 0: #Si el puntaje es menor a cero, ponemos el puntaje a 0 para evitar num negativos
                score = 0
        except ValueError:
            score = 0 #Si el archivo esta vacio ponemos 0 a score para evitar errores
    return score
# Escribe el puntaje si se gana +10 o -10 si se pierde
def write_score(score,path):    
    with open(path, "w") as f:
        f.write(str(score)) #Escribimos el score que tiene que ser si o si un str y NO un int

# Refresca la página para que aparezca un nueva tabla(IMAGEN) 
def refresh_page():
    os.system("clear")

# Revisa que solo se reciba una letra, y no una cadena vacia o numero
def check_and_report():
    global current_letter
    while True:
        current_letter = str(input("Pon una letra: "))
        checking = current_letter.isalpha()
        if (len(current_letter) != 1) or checking == False: #Si lo que pedimos tiene + de un 1 caracter o un numero
            print("Trata introduciendo solo UNA LETRA ¡Por favor!\nLos números no estan permitidos")
            time.sleep(4)
            break
        else:
            break

# Muestra el tablero de juego
def display_board(hidden_word,tries,score):
    print("""
              -----------------------------------------
              W E L C O M E  TO  H A N G M A N  G A M E
              -----------------------------------------""")
    print(IMAGES[tries])
    print(f"Puntaje global: {score}")
    print("Adivina la palabra")
    print(hidden_word)

def run():
    # Path debera contener la ruta donde se encuentre el archivo board_score.txt
    path = "C:/Users/Equipo/Documents/hangman_game/board_score.txt"
    score = read_score(path)
    letter_list = []
    tries = 0 
    hidden_word = ["-"] * len(word) # Fijamos un "-" por cada letra de la palabra oculta
    while "-" in hidden_word: # Este ciclo se ejecutara hasta que no haya mas "-" en la palabra      
        display_board(hidden_word,tries,score)
        check_and_report()

        for idx, letter in enumerate(word): # Aca iteramos sobre la palabra  
            if letter.upper() == current_letter.upper(): # Si la letra que da el usuario es igual a una letra de la palabra oculta.
                hidden_word[idx] = letter  # Cambiamos el "-" por la letra                                          
                letter_list.append(letter) # Agregamos la letra a la lista

        if len(letter_list) == 0: # Si la lista esta vacia, o sea no se encontro la letra
            tries += 1 # Sumamos un intento 
            if tries == 7: # Si los intentos llegan a 10
                display_board(hidden_word,tries,score)
                print(f"Perdiste cracko. Suerte en la próxima\nLa palabra era: {word}") # rompemos el ciclo y le decimos la palabra
                score = int(score) - 15 # Perdio y se quita 15 puntos a su score
                break
        else:
            letter_list = [] # Vaciamos la lista, para estar listos a la proxima letra que pondra el usuario

        refresh_page()
    # Si ya no hay "-" en la palabra oculta significa que ganaste
    else:
        print(f"Ganaste cracko!!!!\nLa palabra era: {word}")
        score = int(score) + 15 # Gano y se suma 15 puntos a su score

    write_score(score,path) #El último paso del programa sera escribir el puntaje ya sea que gane o pierda
if __name__ == "__main__":
    word = random.choice(WORDS).upper()
    run()

