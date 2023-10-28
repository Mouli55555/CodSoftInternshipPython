import random
from colorama import Fore,Style

#Score

Your_score=0
computer_score=0

#User Choice
while(True):

    print(Fore.LIGHTYELLOW_EX+'''\n\033[1m>> Rock\n>> Paper\n>> Scissor\n''')
    user_choice=input("Enter Choice :")

#Computer Choice

    elements=("ROCK","PAPER","SCISSOR")
    computer_choice=random.choice(elements)

#Winner Decision

    if user_choice.lower()==computer_choice.lower():
        print(Fore.BLUE+"\n\033[1mTie")
        print("\n{} == {}".format(user_choice.upper(),computer_choice))
        Your_score+=1
        computer_score+=1

    elif (user_choice.lower()=="rock") and computer_choice=="PAPER":
        print(Fore.RED+"\n\033[1mYou lost try again")
        print("\n{} Beats {}".format(computer_choice,user_choice.upper()))
        computer_score+=1

    elif (user_choice.lower()=="rock") and computer_choice=="SCISSOR":
        print(Fore.GREEN+"\n\033[1mYou are the winner ")
        print("{} Beats {}".format(user_choice.upper(),computer_choice))
        Your_score+=1

    elif (user_choice.lower()=="paper") and computer_choice=='ROCK':
        print(Fore.GREEN+"\n\033[1mYou are the winner ")
        print("{} Beats {}".format(user_choice.upper(),computer_choice))
        Your_score+=1

    elif (user_choice.lower()=="paper") and computer_choice=='SCISSOR':
        print(Fore.RED+"\n\033[1mYou lost try again")
        print("\n{} Beats {}".format(computer_choice,user_choice.upper()))
        computer_score+=1

    elif (user_choice.lower()=="scissor") and computer_choice=='ROCK':
        print(Fore.RED+"\n\033[1mYou lost try again ")
        print("{} Beats {}".format(computer_choice,user_choice.upper()))
        computer_score+=1

    elif (user_choice.lower()=="scissor") and computer_choice=='PAPER':
        print(Fore.GREEN+"\n\033[1mYou are the winner ")
        print("\n{} Beats {}".format(user_choice.upper(),computer_choice))
        Your_score+=1
    else:
        print(Fore.RED+"\n\033[1mPlease Enter A valid Input ")

#Score Display
    print(Fore.LIGHTBLUE_EX+"\n\033[1mYour Score     = ",Your_score)
    print(Fore.LIGHTBLUE_EX+"\n\033[1mComputer Score = ",computer_score)

#Rematch or exiting by declaring final winner
    rematch=input(Fore.LIGHTMAGENTA_EX+"\n\033[1mPress ({}) to play again or prompt ({}) to exit :".format("ENTER"," . "))
    if(rematch=="."):
        if(Your_score>computer_score):
            print(Fore.GREEN+"\n\033[1m congratulations You are the winner")
            print(Fore.LIGHTBLUE_EX+"\n\033[1mYour Score     = ",Your_score)
            print(Fore.LIGHTBLUE_EX+"\n\033[1mComputer Score = ",computer_score)
            print(Fore.RED+"\n\033[1mExiting...")
        elif(Your_score==computer_score):
            print(Fore.BLUE+"\n\033[1mMatch is Tie")
            print(Fore.LIGHTBLUE_EX+"\n\033[1mYour Score     = ",Your_score)
            print(Fore.LIGHTBLUE_EX+"\n\033[1mComputer Score = ",computer_score)
            print(Fore.RED+"\n\033[1mExiting...")
        else:
            print(Fore.RED+"\n\033[1mYou lost better luck next time ")
            print(Fore.LIGHTBLUE_EX+"\n\033[1mYour Score     = ",Your_score)
            print(Fore.LIGHTBLUE_EX+"\n\033[1mComputer Score = ",computer_score)
            print(Fore.RED+"\n\033[1mExiting...")
        break
print(Style.RESET_ALL)