import random
def hangman():
    list_of_words=["eduyear","hangman","india","python","happy"]
    Word=random.choice(list_of_words)
    Turns=10
    Guesmade=''
    Valid_entry=set('abcdeghijklmnopqrstuvwxyz')
    while len(Word)>0:
        main_word=""
        missed=0

        for letter in Word:
            if letter in Guesmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_ "
        if main_word==Word:
            print(main_word)
            print("you won!!")
            break
    
        print("quess the words", main_word)
        guess=input()

        if guess in Valid_entry:
            Guesmade=Guesmade+guess
        else:
            print("enter valid charchter")
            guess=input()
        if guess not in Word:
            Turns=Turns-1

            if Turns==9:
                print("9 turns left!!")
                print("-----------------")
            if Turns==8:
                print("8 turns left!!")
                print("--------")
                print("        O             ")
            if Turns==7:
                print("7 turns left!!")
                print("--------")
                print("        O             ")
                print("        |         ")
            if Turns==6:
                print("6  turns are left!!")
                print("--------")
                print("        O         ")
                print("        |         ")
                print("        /         ")
            if Turns==5:
                print(" 5 turns are left!!")
                print("--------")
                print("        O         ")
                print("        |         ")
                print("       / \        ")
            if Turns==4:
                print(" 4 turns are left!!")
                print("--------")
                print("     \  O         ")
                print("        |         ")
                print("       / \        ")
            if Turns==3:
                print(" 3 turns are left!!")
                print("--------")
                print("     \  O  /       ")
                print("        |         ")
                print("       / \        ")
            if Turns==2:
                print(" 2 turns are left!!")
                print("--------")
                print("     \  O  /_|    ")
                print("        |         ")
                print("       / \        ")
            if Turns==1:
                print(" only 1 turns are left!! Hangman on his last breath")
                print("--------")
                print("     \  O  /_|    ")
                print("        |         ")
                print("       / \        ")
            if Turns==0:
                print("You loose ")
                print("you let a good man die")
                print("--------")
                print("        O  _|    ")
                print("       /|\        ")
                print("       / \        ")
                break

                 




            




                 

                   


















name1=input("ENTER YOUR NAME->")
print("Welcome", name1,"!")
print("---------------------")
print("Try to guess the word less than 10 attemps->")
hangman()
