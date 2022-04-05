import random

last_lenguage = "en"
game_difficulty = 2
allowed_errors = 7
tips = 0

def main():
    #Gets language and game diffuculty
    global tips
    global allowed_errors
    global game_difficulty
    global last_lenguage
    if last_lenguage == "en": 
        game_difficulty_str = input("Choose game difficulty (easy, medium or hard): ")
        language = input("Insert the language of the game (it or en): ")
        #----------------------------------------------------------------
        if game_difficulty_str == "easy":
            game_difficulty = 1
        elif game_difficulty_str == "medium":
            game_difficulty = 2
        elif game_difficulty_str == "hard":
            game_difficulty = 3
        else:
            print("You inserted an invalid game difficulty!")
            main()

        if game_difficulty == 1:
            tips = 4
            allowed_errors = 15
        elif game_difficulty == 2:
            tips = 2
            allowed_errors = 10
        elif game_difficulty == 3:
            tips = 0
            allowed_errors = 7
        else:
            return
         
        
        if language == "it":
            last_lenguage = "it"
            mainit()
            
        elif language == "en":
            last_lenguage = "en"
            mainen()
            
        else:
            print("You inserted an invalid language please insert it or en!")
            main()
            #-----------------------------------------------------------------
    elif last_lenguage == "it":
        game_difficulty_str = input("Scegli una difficolta' (semplice, medio o difficile): ")
        language = input("Inserisci la lingua del gioco (it o en): ")
        
        if game_difficulty_str == "semplice":
            game_difficulty = 1
        elif game_difficulty_str == "medio":
            game_difficulty = 2
        elif game_difficulty_str == "difficile":
            game_difficulty = 3
        else:
            print("Hai inserito una difficolta' di gioco non valida!")
            main()

        if game_difficulty == 1:
            tips = 4
            allowed_errors = 15
        elif game_difficulty == 2:
            tips = 2
            allowed_errors = 10
        elif game_difficulty == 3:
            tips = 0
            allowed_errors = 7
        else:
            return

        if language == "it":
            last_lenguage = "it"
            mainit()
           
        elif language == "en":
            last_lenguage = "en"
            mainen()
           
        else:
            print("Hai inserito una lingua non valida, scegli tra it o en!")
            main()
       

#game in english
def mainen():
    global allowed_errors
    global tips

    #selecting the word
    with open("word-en.txt", "r") as file:
	    allText = file.read()
	    words = list(map(str, allText.split()))
    global word
  
    word_temp = str(random.sample(words, 1))
    word_temp =  word_temp.replace("'","")
    word_temp = word_temp.replace("[","")
    word = word_temp.replace("]","")
    if len(word) < 5:
        mainen()
    
    guesses  = []
    done = False
    #constructing the ui for the game
    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")
        #return of the guess
        guess = input(str(f"Allowed errors left {allowed_errors}, next guess: "))
        guesses.append(guess.lower())
        if guess not in word:
            allowed_errors -= 1
            if allowed_errors == 0:
 
                break

        done = True
        for letter in word:
            if letter not in guesses:
                done = False


    #end of the game
    if done == True:
        print(f"You found the word! It was {word}!")
        play_agn = input(f"Type a to play again or m to return to the main menu: ")
        if play_agn == "a":
            print(" ")
            print("---------NEW GAME----------")
            mainen()
        elif play_agn == "m":
            print(" ")
            print("---------MAIN MENU----------")
            main()
           

    else:
        print(f"Game Over! The word was {word}!")
        play_agn = input(f"Type a to play again or m to return to the main menu: ")
        if play_agn == "a":
            print(" ")
            print("---------NEW GAME----------")
            mainen()
        elif play_agn == "m":
            print(" ")
            print("---------MAIN MENU----------")
            main()

def mainit():
    global allowed_errors
    global tips
    with open("word-it.txt", "r") as file:
	    allText = file.read()
	    words = list(map(str, allText.split()))
    global word
  
    word_temp = str(random.sample(words, 1))
    word_temp =  word_temp.replace("'","")
    word_temp = word_temp.replace("[","")
    word = word_temp.replace("]","")
    if len(word) < 3:
        mainen()
    
    guesses  = []
    done = False

    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")

        guess = input(str(f"Ti sono rimasti {allowed_errors} errori, prossimo tentativo: "))
        guesses.append(guess.lower())
        if guess not in word:
            allowed_errors -= 1
            if allowed_errors == 0:
 
                break

        done = True
        for letter in word:
            if letter not in guesses:
                done = False



    if done == True:
        print(f"Hai trovato la parola! Era {word}!")
        play_agn = input(f"Digita a per giocare di nuovo o m per tornare al menu principale: ")
        if play_agn == "a":
            print(" ")
            print("---------NUOVA PARTITA----------")
            mainen()
        elif play_agn == "m":
            print(" ")
            print("---------MENU PRINCIPALE----------")
            main()
           

    else:
        print(f"Hai perso :(! La parola era {word}!")
        play_agn = input(f"Digita a per giocare di nuovo o m per tornare al menu principale: ")
        if play_agn == "a":
            print(" ")
            print("---------NUOVA PARTITA----------")
            mainen()
        elif play_agn == "m":
            print(" ")
            print("---------MENU PRINCIPALE----------")
            main()
#running the game
main()