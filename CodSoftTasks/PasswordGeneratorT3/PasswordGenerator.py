import random
import string

lower_case=string.ascii_lowercase
upper_case=string.ascii_uppercase
special=string.punctuation

password=""

while(True):
    length=int(input("\nEnter valid length of the password [>=4&<20] : "))
    if(length<4 or length>19):
        print("\nEnter valid length")
        continue
    complexity=int(input('''
                 \t  SELECT\n
                 \t1.EASY(num)\n
                 \t2.MEDIUM(num+char)\n
                 \t3.HARD(num+char+panctuation)  : '''))
    
    if(complexity==1):
        for i in range(length):
            password+=str(random.randint(0,9))
        print("\nThe Generated password is :",password)
        password=""

    elif(complexity==2):
        for i in range(length-2):
            password+=str(random.randint(0,9))
        password+=random.choice(upper_case)
        password+=random.choice(lower_case)
        temp=list(password)
        random.shuffle(temp)
        password="".join(temp)
        print("\nThe Generated password is :",password)
        password=""
    
    elif(complexity==3):
        for i in range(length-3):
            password+=str(random.randint(0,9))
        password+=random.choice(upper_case)
        password+=random.choice(lower_case)
        password+=random.choice(special)
        temp=list(password)
        random.shuffle(temp)
        password="".join(temp)
        print("\nThe Generated password is :",password)
        password=""

    inn=input("\n\033[1mPress ({}) to Do again or prompt ({}) to exit :".format("ENTER"," . "))
    if inn==".":
        print("\n\033[1mExiting....")
        break
    