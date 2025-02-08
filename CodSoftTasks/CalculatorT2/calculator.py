from colorama import Fore,Style

# Basic Calculator Operations

def Addition(a, b):
    return a+b

def Subtraction(a,b):
    return a-b

def Multiplication(a,b):
    return a*b

def Division(a,b):
    if (b == 0):
        return "Syntax Error"
    else:
        return a/b

# Taking Input From User

while(True):
    num1 = int(input(Fore.LIGHTYELLOW_EX+"\n\033[1mEnter first number : \033[0m"))
    num2 = int(input(Fore.LIGHTYELLOW_EX+"\n\033[1mEnter second number : \033[0m"))
    print(Fore.LIGHTYELLOW_EX+'''\n\033[1m1.Addition[+]             2.Subraction[-] \n\n3.Multiplication[*]       4.Division[/] \n\n5.Exit''')
    operator=input(Fore.LIGHTYELLOW_EX+"\n\033[1mEnter Your Operation :")
# calling operations as per user input
    if operator=='5':
        print(Fore.RED+"\n\033[1mExiting....")
        print(Style.RESET_ALL)
        exit(0)
    elif  operator == "+" or operator=='1':
        add = Addition(num1, num2)
        print(Fore.GREEN+"\n\033[1mAddition of {} + {} = {} ".format(num1, num2, add))

    elif  operator == "-" or operator=='2':
        sub = Subtraction(num1, num2)
        print(Fore.GREEN+"\n\033[1mSubtraction of {} - {} = {}".format(num1, num2, sub))

    elif  operator == "*" or operator=='3':
        mul = Multiplication(num1, num2)
        print(Fore.GREEN+"\n\033[1mMultiplication of {} * {} = {}".format(num1, num2, mul))

    elif  operator == "/" or operator=='4':
        div = Division(num1, num2)
        if(div!="Syntax Error"):
            print("\n\033[1mDivision of {} / {} = {}".format(num1, num2, div))
        else:
            print("\n\033[1mdivision with zero not possible {}".format(div))
    cal=input(Fore.CYAN+"\n\033[1mPress ({}) to Do again or prompt ({}) to exit :".format("ENTER"," . "))
    if cal==".":
        print(Fore.RED+"\n\033[1mExiting....")
        break
print(Style.RESET_ALL)
