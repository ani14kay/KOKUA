# -*- coding: utf-8 -*-
"""
Created on Sun May 05 09:19:13 2019

@author: Aaryan Hebbalkar, Akshat Singh, Anisha Katiyar
"""
#%%
from random import *
import pickle as pkl
#%%
def Help():
    a = '''You wanna know what I can do? Here is a list:
        1. 'Help': See this list again
        2. 'Tell me a Joke': I tell you a joke! I have an excellent sense of humour!
        3. 'Answer my question': Ask me a Yes/No question and I'll give you the answer! I only have a 50% chance of being correct...
        4. 'Spin the Wheel': You will input choices and I will spin the wheel of fate to help you make a choice!
        5. 'Secret Santa':  Who is gonna give a gift to whom? Let's find out...
        6. 'Rock Scissors Paper': Join in to play the classic game where two new characters join in the fun!
        7. 'Minesweeper': Play the classic game!
        8. 'Password': Will lead you into a password generator!
        9. 'Bye': You are satisfied with my care!'''
    print(a)
#%%
def joke():
        jokes = {}
        jokes[1] = '''My sister and I often laugh about how competitive we are.
But I laugh more.'''
        jokes[2] = 'If we shouldn’t eat at night, why do they put a light in the fridge?'
        jokes[3] = 'Velcro - What a rip off!'
        jokes[4] = """Don't you hate it when someone answers their own questions?
I do"""
        jokes[5] = ''' So what if I don't know what Armageddon means?
It's not the end of the world...'''
        jokes[6] = '''Never criticize someone until you’ve walked a mile in their shoes.
That way, when you criticize them, they won’t be able to hear you from that far away.
Plus, you’ll have their shoes.'''
        jokes[7] = '''I hate Russian Dolls
They are so full of themselves.'''
        jokes[8] = '''What happens to a frog's car when it breaks down?
It gets toad away.'''
        jokes[9] = '''Just burned 2,000 calories.
That's the last time I leave brownies in the oven while I nap.'''
        jokes[10] = ''' I hate people who use big words just to make themselves look perspicacious.'''
        f1 = open('jokes.dat','wb+')
        pkl.dump(jokes, f1)
        f1.seek(0)
        list_of_jokes = pkl.load(f1)
        f1.close()
        a = randint(1,10)
        print(list_of_jokes[a])
#%%
def Magic_8_Ball():
        print('''You have entered the Magic-8 Ball Protocol!
You will now ask a question that determines your future. I will then give my opinion on the matter.
                            WARNING
We do not recommend that you shake the device after inputting your question!''')
        sent = input('Ask a question. ')
        ball = []
        ball.append('It is certain.\n')
        ball.append('It is decidedly so.\n')
        ball.append('You may rely on it.\n')
        ball.append('Signs point to yes.\n')
        ball.append('Yes - definitely.\n')
        ball.append('Cannot predict now.\n')
        ball.append('Try again later.\n')
        ball.append("Don't count on it\n")
        ball.append('It is highly doubtful.\n')
        ball.append('My sources say no.\n')
        a = randint(0,9)
        f2 = open('MAGIC.txt', 'w+')
        f2.writelines(ball)
        f2.seek(0)
        list_of_8_ball_outputs = f2.readlines()
        print(list_of_8_ball_outputs[a])
#%%
def wheel():
        l = []
        n = int(input('Enter the number of choices. '))
        for i in range(n):
            print(i+1)
            cho = input('Enter the choice. ')
            l.append(cho)
        a = randrange(n)
        print('The choice selected is', l[a])
#%%
def secret_santa():
        n = 1
        while n <= 1:
            n = int(input('Enter the number of participants. '))
            if n == 1:
                print('''Don't be silly! You can't gift yourself a Secret Santa Gift!
                      Try Again!''')
            elif n < 1:
                print('''Oof! You need at least one person for gift-giving to occur!
                      Try Again''')
        givers = []
        receivers = []
        final_list = {}
        x = 0
        for i in range(n):
            x = input('Enter Name here. ')
            print(x, 'added.')
            givers.append(x)
            receivers.append(x)
        while x != n:
            a = choice(givers)
            b = choice(receivers)
            if a != b:
                final_list[a] = b
                givers.remove(a)
                receivers.remove(b)
            else:
                continue
            x = len(final_list)
        print(final_list)
#%%
def RScPLSp():
        print(''' Rules:
      Scissors cuts paper, paper covers rock, rock crushes lizard,
      lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard,
      lizard eats paper, paper disproves Spock, Spock vaporizes rock and
      rock crushes scissors.
      You get 2 points for every win and 1 point for a Twinsie!''')
        a = input('Enter username: ')
        print(a, 'vs Computer')
        n = int(input('Enter number of rounds. '))
        p = 0
        c = 0
        for i in range(n):
            l = ['Rock', 'Scissors', 'Paper', 'Lizard', 'Spock']
            player = input('Rock, Paper, Scissors, Lizard or Spock? ')
            if player in l:
                print(player, 'vs', end = ' ')
                index = randrange(0,5)
                computer = l[index]
                print(computer)
                if player == computer:
                    print('Twinsies...')
                    p += 1
                    c += 1
                elif player == 'Paper':
                    if computer == 'Rock':
                            print('Paper covers rock.')
                            p += 2
                    elif computer == 'Scissors':
                        print('Scissors cuts paper.')
                        c += 2
                    elif computer == 'Lizard':
                        print('Lizard eats paper.')
                        c += 2
                    elif computer == 'Spock':
                        print('Paper disproves Spock.')
                        p += 2
                elif player == 'Scissors':
                    if computer == 'Rock':
                        print('Rock crushes Scissors.')
                        c += 2
                    elif computer == 'Paper':
                        print('Scissors cuts paper.')
                        p += 2
                    elif computer == 'Lizard':
                        print('Scissors decapitates lizard.')
                        p += 2
                    elif computer == 'Spock':
                        print('Spock smashes Scissors.')
                        c += 2
                elif player == 'Rock':
                    if computer == 'Paper':
                        print('Paper covers rock.')
                        c += 2
                    elif computer == 'Scissors':
                        print('Rock crushes Scissors.')
                        p += 2
                    elif computer == 'Lizard':
                        print('Rock crushes Lizard.')
                        p += 2
                    elif computer == 'Spock':
                        print('Spock vaporizes Rock.')
                        c += 2
                elif player == 'Lizard':
                    if computer == 'Rock':
                        print('Rock crushes Lizard.')
                        c += 2
                    elif computer == 'Scissors':
                        print('Scissors decapitates Lizard.')
                        c += 2
                    elif computer == 'Paper':
                        print('Lizard eats paper.')
                        p += 2
                    elif computer == 'Spock':
                        print('Lizard poisons Spock.')
                        p += 2
                elif player == 'Spock':
                    if computer == 'Rock':
                        print('Spock vaporises rock.')
                        p += 2
                    elif computer == 'Scissors':
                        print('Spock smashes Scissors.')
                        p += 2
                    elif computer == 'Lizard':
                        print('Lizard poisons Spock.')
                        c += 2
                    elif computer == 'Paper':
                        print('Paper disproves Spock.')
                        c += 2
                else:
                    print('Enter a valid name.')
                    continue
        print('Kokua:', c)
        print(a, ': ', p, sep ='')
        if p > c:
            print(a, 'Wins!')
        elif c > p:
            print('Woohoo! I Win!')
        elif c == p:
            print('DRAW')
#%%
def Mines():
    print('                      MINESWEEPER                           ')
    print('''Please enter the corresponding position number in the grid. The top left corner is 1, the one to its right is 2 and so on...''')
    print('''If you score 4 points, your chosen position has a mine at the preceding and succeesing positions.
          If you score 2 point, your chosen position is either preceded or succeeded by a mine.
          If you score one point, your preceding and succeeding positions are safe.
          ALL THE BEST!''')
    dim=int(input('Enter dimension of square grid: '))
    nmines=int(input('Enter number of mines: '))
    for i in range(dim):                     #Generating Grid
        for j in range(dim):
            print('O',end=' ')
        print()
    List=[]
    for b in range(1,dim**2 + 1):
        List.append(b)
    poslist=[]
    for c in range(nmines):            #Choosing mine positions
        pos=choice(List)
        poslist.append(pos)
        List.remove(pos)
    life=True
    score=0
    tries=[]
    while life==True:
        if List == tries:
            print('YOU WIN!!')
            break
        place=int(input('Enter position number you would like to try: '))
        if place in tries:
            print('You have already tried this place')
            continue
        tries.append(place)
        if place in poslist:            #If hit mine
            life=False        
            break
        else:               #Scoring on basis of  relative closeness of mines
            if (place-1) in poslist and (place+1) in poslist:  
                score+=4
            elif (place-1) in poslist or (place+1) in poslist:
                score+=2
            else:
                score+=1
            for d in range(dim):
                for d1 in range(1,dim+1):
                    expr=d*dim +d1
                    n=0
                    if expr in tries:      #Checking number of surrounding mines and printing
                        if expr-1 in poslist and expr-1>0:
                            n+=1
                        if expr+1 in poslist and expr+1<dim**2+1:
                            n+=1
                        if expr+dim in poslist and expr+dim<dim**2+1:
                            n+=1
                        if expr+dim-1 in poslist and expr+dim-1<dim**2+1 and expr+dim-1!=expr+1:
                            n+=1
                        if expr+dim+1 in poslist and expr+dim+1<dim**2+1:
                            n+=1
                        if expr-dim in poslist and expr-dim>0:
                            n+=1
                        if expr-dim-1 in poslist and expr-dim-1>0:
                            n+=1
                        if expr-dim+1 in poslist and expr-dim+1>0 and expr-dim+1!=expr-1:
                            n+=1
                            print(n,end=' ')                    
                    else:
                        print('O',end=' ')
                print()
            print('Score is',score)
    if life == False:
        tries.pop()
        print('You have died')
        for e in range(dim):
            for e1 in range(1,dim+1):
                expr2=e*dim + e1
                if expr2 in poslist:
                    print('X',end=' ')
                elif expr2 in tries:
                    print('+',end=' ')
                else:
                    print('O',end=' ')
            print()
        print('Your score is',score)
#%%
def pwd():
    print("WELCOME TO PASSWORD GENERATOR")
    print("=============================")
    d={}
    print()
    print('Note:This program works in 5 steps')
    print()
    print('STEP-1:')
    a=input("Would you like to input the characters to be used for password generation?\n'yes' or 'no'? ")
    b=['yes','no']
    if a==b[0]:
        chars=input("enter characters you would like to use without any gaps: ")
        c=int(input('Enter the number of passwords to be generated: '))
        length=int(input('password length: '))
        for p in range(c):
            e=input('enter a username: ')
            key=e
            password=''
            for i in range(length):
                password+=choice(chars)                    
                value=password
                d[key]=value    
    elif a==b[1]:  
        chars='abcdefghijklmnopqrstuvwxyz1234567890!@#$%&'
        c=int(input('Enter the number of passwords to be generated: '))
        length=int(input('password length: '))
        for p in range(c):
            e=input('enter a username: ')
            key=e
            password=''
            for i in range(length):
                password+=choice(chars)                    
                value=password
                d[key]=value  
    else:
        print("enter a valid input")
        a=input("So, would you like to input the characters to be used for password generation?\n'yes' or 'no'?: ")
        b=['yes','no']
        for a in (c):
            if a==b[0]:
                chars=input("enter characters you would like to use without any gaps: ")
                c=int(input('Enter the number of passwords to be generated: '))
                length=int(input('password length: '))
                for p in range(c):
                    e=input('enter a username: ')
                    key=e
                    password=''
                    for i in range(length):
                        password+=choice(chars)                    
                        value=password
                        d[key]=value
                   
            elif a==b[1]:  
                chars='abcdefghijklmnopqrstuvwxyz1234567890!@#$%&'
                c=int(input('Enter the number of passwords to be generated: '))
                length=int(input('password length: '))
                for p in range(c):
                    e=input('enter a username: ')
                    key=e
                    password=''
                    for i in range(length):
                        password+=choice(chars)                    
                        value=password
                        d[key]=value
    print()
    print('STEP-2:')
    f=input("Do you wish to view passwords generated for any username in particular or maybe for all? 'y' or 'n': ")
    g=['y','n']
    if f==g[0]:
        h=int(input('Enter the number of usernames for which you would like to view their passwords: '))
        j=input('enter usernames seperated by commas: ')
        k=list(j.split(','))
        for i in range(h):
            if k[i] in d:
                print('username : ',k[i],'     ','password: ',d[k[i]])
    elif f==g[1]:
        print('Okay')
    else:
        print('enter a valid input: ')
        g=input("So, do you wish to view passwords generated for any username in particular or maybe for all? 'y' or 'n': ")
        if f==g[0]:
            h=int(input('Enter the number of usernames for which you would like to view their passwords: '))
            j=input('enter usernames seperated by commas: ')
            k=list(j.split(','))
            for i in range(h):
                if k[i] in d:
                    print('username : ',k[i],'     ','password: ',d[k[i]])                
    print()  
    print('STEP-3:')
    l=input('Do you want to change any password? "yay" or "nay": ')
    m=['yay','nay']
    if l==m[0]:
        p=int(input('Enter no. of usernames for which you would like to change password: '))
        for i in range(p):
            n=input("enter the username for which you would like to change the password: ")
            o=input("enter a new password: ")
            if n in d:
                d[n]=o
    elif l==m[1]:
        print('okay')
    elif l not in("yay","nay"):
        print("enter a valid input")
        l=input('So, do you want to change any password? "yay" or "nay": ')    
        if l==m[0]:
            p=int(input('Enter no. of usernames for which you would like to change password: '))
            for i in range(p):
                n=input("enter the username for which you would like to change the password: ")
                o=input("enter a new password: ")
                if n in d:
                    d[n]=o
    print()
    print('STEP-4:')
    q=input('do you want to cross check for your final password by doing a mock login? "yes" or "no": ')
    if q=='yes':
        r=int(input('Enter no. of usernames for which you would like to try for: '))
        for i in range(r):
            s=input("enter username: ")
            t=input("enter password: ")
            if s in d:
                if d[s]==t:
                    print("Correct password entered")
                    print('Yippee!... you are logged in')
                else:
                    print("Incorrect password entered")
                    t=input("enter password again: ")
                    if d[s]==t:
                        print("Correct password entered")
                        print('Yipee!... you are logged in')
            else:
                print("Enter a valid username")
                s=input("enter username: ")
                t=input("enter password: ")
                if s in d:
                    if d[s]==t:
                        print("Correct password entered: ")
                        print('Yippee!... you are logged in')
                    else:
                        print("Incorrect password entered")
                        t=input("enter password again")
                        if d[s]==t:
                            print("Correct password entered")
                            print('Yipee!... you are logged in')
    elif q=='no':
        print('Okay')
    elif q not in('yes','no'):
        print('Enter a valid input')
        q=input('do you want to cross check for your final password by doing a mock login? "yes" or "no" ')
        if q=='yes':
            r=int(input('Enter no. of usernames for which you would like to try for: '))
            for i in range(r):
                s=input("enter username: ")
                t=input("enter password: ")
                if s in d:
                    if d[s]==t:
                        print("Correct password entered")
                        print('Yipee!... you are logged in')
                    else:
                        print("Incorrect password entered")
                        t=input("enter password again: ")
                        if d[s]==t:
                            print("Correct password entered")
                            print('Yipee!... you are logged in')
                else:
                    print("Enter a valid username")
                    s=input("enter username: ")
                    t=input("enter password: ")
                    if s in d:
                        if d[s]==t:
                            print("Correct password entered")
                            print('Yipee!... you are logged in')
                        else:
                            print("Incorrect password entered")
                            t=input("enter password again: ")
                            if d[s]==t:
                                print("Correct password entered")
                                print('Yipee!... you are logged in')
    print()
    print('STEP-5: Printing the result')
    print('................')
    print('...processing...')
    print('................')
    print('Result:The final passwords for the entered usernames are as follows- ')
    for i in d:
        print('Username : ',i,'     ','Password: ',d[i])
    print()            
    print('=======================')
    print('Thank you for visiting!')
""" import mysql.connector as m
    db=m.connect(host="localhost",user="root",password="",database="password")
    c=db.cursor()
    q1='''create table passwordlogins
          (username varchar(20) primary key,
           password varchar(20));'''
    db.commit()
    q2='select * from passwordlogin;'
    c.execute(q2)
    for i in c:
        i=a,b
        if a==e:
            print("you are already a member ")
            ask=input("would you like to update or keep it the same ")
            if ask=="update":
                password=input("enter a new password ")
                q3='''update passwordlogin set password=%s where username=%s'''
                val=(password,a)
                c.execute(q3,val)
                db.commit()
            else:
                print("THANK YOU")
        else:
            q='''insert into passwordlogins(username,password)values(%s,%s)'''
            val=(e,password) #e=username , password=password
            c.execute(q,val)  
            db.commit()"""
#%%
print('Hi! I am Kōkua! Your Personal assistant!', ':}')
print('It is my duty to make your life as convenient as possible.')
print('To get a full list of my functions, type "HELP"')
print('Type "Bye" to send me away.' )
inp = ''
while inp != 'bye':
    inp = input('How can I help you? ')
    inp = inp.lower()
    if inp == 'help':
        Help()
    elif inp == 'tell me a joke':
        joke()
    elif inp == 'answer my question':
        Magic_8_Ball()
    elif inp == 'bye':
        print('Bye! It was my pleasure serving you...')
    elif inp == 'spin the wheel':
        wheel()
    elif inp == 'secret santa':
        secret_santa()
    elif inp == 'rock scissors paper':
        RScPLSp()
    elif inp == 'minesweeper':
        Mines()
    elif inp == 'password':
        pwd()
    else:
        print('Invalid Input! Kindly type "HELP" to check list of valid inputs.') 





