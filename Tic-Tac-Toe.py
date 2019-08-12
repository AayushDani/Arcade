from tkinter import *

wnd = Tk()
#BOARD
cvs1 = Canvas(wnd, width=800, height=600, bg = 'black')
h_line1 = cvs1.create_line(200,250,600,250,width=5,fill='white')
h_line2 = cvs1.create_line(200,400,600,400,width=5,fill='white')
v_line1 = cvs1.create_line(300,150,300,500,width=5,fill='white')
v_line2 = cvs1.create_line(500,150,500,500,width=5,fill='white')
cvs1.pack()

#ENTRIES
a = input("Enter symbol of choice for player 1 (X or O): ").upper()
if a != 'X' and a != 'O':
    print("Please enter a valid symbol: 'X' or 'O'")
b = input("Enter symbol of choice for player 2 (X or O): ").upper()
if b != 'X' and b != 'O':
    print("Please enter a valid symbol: 'X' or 'O'")
check = input("Are you sure?(Y/N): ").upper()

if check == 'N':
    print("Please restart and choose the symbol of your choice.")

print("""               (1)    |     (2)   |   (3)
            -------------------------
               (4)    |     (5)   |   (6)
            ------------------------- 
               (7)    |     (8)   |   (9) """)
print("Use the number keys(1-9) to choose which space to fill your symbol in:")
print("The first row is denoted by the numbers (1-3), second row by (4-6) and the third row by (7-9).")

#GAMEPLAY
x = int(input("Player one enter your symbol in position of your choice: "))
def gameplay(x):
    if x == 1:
        if a == 'X':
            cvs1.create_line(230,180,265,230,width=4,fill = 'white')
            cvs1.create_line(230,230,265,180,width=4,fill = 'white')
        elif a == 'O':
            cvs1.create_oval(230,180,285,230,width=4,outline= 'white')
    elif x==2:
        if a == 'X':
            cvs1.create_line(380,180,415,230,width=4,fill = 'white')
            cvs1.create_line(380,230,415,180,width=4,fill = 'white')
        elif a == 'O':
            cvs1.create_oval(380,180,435,230,width=4,outline= 'white')
    elif x==3:
        if a == 'X':
            cvs1.create_line(530,180,565,230,width=4,fill = 'white')
            cvs1.create_line(530,230,565,180,width=4,fill = 'white')
        elif a == 'O':
            cvs1.create_oval(530,180,585,230,width=4,outline= 'white')
    elif x ==4:
        if a == 'X':
            cvs1.create_line(230,310,265,345,width=4,fill = 'white')
            cvs1.create_line(230,345,265,310,width=4,fill = 'white')
        elif a == 'O':
            cvs1.create_oval(230,300,285,350,width=4,outline= 'white')
    elif x == 5:
        if a == 'X':
            cvs1.create_line(380,310,415,345,width=4,fill = 'white')
            cvs1.create_line(380,345,415,310,width=4,fill = 'white')
        elif a == 'O':
            cvs1.create_oval(370,300,425,350,width=4,outline= 'white')
    elif x==6:
        if a == 'X':
            cvs1.create_line(530,310,565,345,width=4,fill = 'white')
            cvs1.create_line(530,345,565,310,width=4,fill = 'white')
        elif a == 'O':
            cvs1.create_oval(520,300,575,350,width=4,outline= 'white')
    elif x==7:
        if a == 'X':
            cvs1.create_line(230,440,265,475,width=4,fill = 'white')
            cvs1.create_line(230,475,265,440,width=4,fill = 'white')
        elif a == 'O':
            cvs1.create_oval(230,430,285,485,width=4,outline= 'white')
    elif x==8:
        if a == 'X':
            cvs1.create_line(380,440,415,475,width=4,fill = 'white')
            cvs1.create_line(380,475,415,440,width=4,fill = 'white')
        elif a == 'O':
            cvs1.create_oval(370,430,425,485,width=4,outline= 'white')
    elif x==9:
        if a == 'X':
            cvs1.create_line(530,440,565,475,width=4,fill = 'white')
            cvs1.create_line(530,475,565,440,width=4,fill = 'white')
        elif a == 'O':
            cvs1.create_oval(520,430,575,485,width=4,outline= 'white')
gameplay(x)
wnd.update()

y = int(input("Player two enter your symbol in position of your choice: "))
if y == x:
    print("Already filled, provide different position.")
    y = int(input("Player two enter your symbol in position of your choice: "))
def game_play(y):
    if y == 1:
        if b == 'X':
            cvs1.create_line(230,180,265,230,width=4,fill = 'white')
            cvs1.create_line(230,230,265,180,width=4,fill = 'white')
        elif b == 'O':
            cvs1.create_oval(230,180,285,230,width=4,outline= 'white')
    elif y==2:
        if b == 'X':
            cvs1.create_line(380,180,415,230,width=4,fill = 'white')
            cvs1.create_line(380,230,415,180,width=4,fill = 'white')
        elif b == 'O':
            cvs1.create_oval(380,180,435,230,width=4,outline= 'white')
    elif y==3:
        if b == 'X':
            cvs1.create_line(530,180,565,230,width=4,fill = 'white')
            cvs1.create_line(530,230,565,180,width=4,fill = 'white')
        elif b == 'O':

            cvs1.create_oval(530,180,585,230,width=4,outline= 'white')
    elif y ==4:
        if b == 'X':
            cvs1.create_line(230,310,265,345,width=4,fill = 'white')
            cvs1.create_line(230,345,265,310,width=4,fill = 'white')
        elif b == 'O':
            cvs1.create_oval(230,300,285,350,width=4,outline= 'white')
    elif y == 5:
        if b == 'X':
            cvs1.create_line(380,310,415,345,width=4,fill = 'white')
            cvs1.create_line(380,345,415,310,width=4,fill = 'white')
        elif b == 'O':
            cvs1.create_oval(370,300,425,350,width=4,outline= 'white')
    elif y==6:
        if b == 'X':
            cvs1.create_line(530,310,565,345,width=4,fill = 'white')
            cvs1.create_line(530,345,565,310,width=4,fill = 'white')
        elif b == 'O':
            cvs1.create_oval(520,300,575,350,width=4,outline= 'white')
    elif y==7:
        if b == 'X':
            cvs1.create_line(230,440,265,475,width=4,fill = 'white')
            cvs1.create_line(230,475,265,440,width=4,fill = 'white')
        elif b == 'O':
            cvs1.create_oval(230,430,285,485,width=4,outline= 'white')
    elif y==8:
        if b == 'X':
            cvs1.create_line(380,440,415,475,width=4,fill = 'white')
            cvs1.create_line(380,475,415,440,width=4,fill = 'white')
        elif b == 'O':
            cvs1.create_oval(370,430,425,485,width=4,outline= 'white')
    elif y==9:
        if b == 'X':
            cvs1.create_line(530,440,565,475,width=4,fill = 'white')
            cvs1.create_line(530,475,565,440,width=4,fill = 'white')
        elif b == 'O':
            cvs1.create_oval(520,430,575,485,width=4,outline= 'white')
game_play(y)
wnd.update()

p = int(input("Player one enter your symbol in position of your choice: "))
gameplay(p)
wnd.update()
q = int(input("Player two enter your symbol in position of your choice: "))
game_play(q)
wnd.update()
r = int(input("Player one enter your symbol in position of your choice: "))
gameplay(r)
wnd.update()
s = int(input("Player two enter your symbol in position of your choice: "))
game_play(s)
wnd.update()
u = int(input("Player one enter your symbol in position of your choice: "))
gameplay(u)
wnd.update()
v = int(input("Player two enter your symbol in position of your choice: "))
game_play(v)
wnd.update()
w = int(input("Player one enter your symbol in position of your choice: "))
gameplay(w)
wnd.update()

#player one win check
for i in [x,p,r,u,w]:
    if i==1:
        for j in [x,p,r,u,w]:
            if j==2:
                for k in [x,p,r,u,w]:
                    if k==3:
                        cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER ONE WINS!!")
                        wnd.update()
            elif j==4:
                for k in [x,p,r,u,w]:
                    if k==7:
                        cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER ONE WINS!!")
                        wnd.update()
            elif j==5:
                for k in [x,p,r,u,w]:
                    if k==9:
                        cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER ONE WINS!!")
                        wnd.update()
        if i==2:
            for j in [x,p,r,u,w]:
                if j==5:
                    for k in [x,p,r,u,w]:
                        if k==8:
                            cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER ONE WINS!!")
                            wnd.update()
        if i==3:
            for j in [x,p,r,u,w]:
                if j==6:
                    for k in [x,p,r,u,w]:
                        if k==9:
                            cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER ONE WINS!!")
                            wnd.update()
                elif j==5:
                    for k in [x,p,r,u,w]:
                        if k==7:
                            cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER ONE WINS!!")
                            wnd.update()
        if i==4:
            for j in [x,p,r,u,w]:
                if j==5:
                    for k in [x,p,r,u,w]:
                        if k==6:
                            cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER ONE WINS!!")
                            wnd.update()
        if i==7:
            for j in [x,p,r,u,w]:
                if j==8:
                    for k in [x,p,r,u,w]:
                        if k==9:
                            cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER ONE WINS!!")
                            wnd.update()
#player two win check              
for i1 in [y,q,s,v]:
    if i1==1:
        for j1 in [y,q,s,v]:
            if j1==2:
                for k1 in [y,q,s,v]:
                    if k1==3:
                        cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER TWO WINS!!")
                        wnd.update()
            elif j1==4:
                for k1 in [y,q,s,v]:
                    if k1==7:
                        cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER TWO WINS!!")
                        wnd.update()
            elif j1==5:
                for k1 in [y,q,s,v]:
                    if k1==9:
                        cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER TWO WINS!!")
                        wnd.update()
        if i1==2:
            for j1 in [y,q,s,v]:
                if j1==5:
                    for k1 in [y,q,s,v]:
                        if k1==8:
                            cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER TWO WINS!!")
                            wnd.update()
        if i1==3:
            for j1 in [y,q,s,v]:
                if j1==6:
                    for k1 in [y,q,s,v]:
                        if k1==9:
                            cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER TWO WINS!!")
                            wnd.update()
                elif j1==5:
                    for k1 in [y,q,s,v]:
                        if k1==7:
                            cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER TWO WINS!!")
                            wnd.update()
        if i1==4:
            for j1 in [y,q,s,v]:
                if j1==5:
                    for k1 in [y,q,s,v]:
                        if k1==6:
                            cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER TWO WINS!!")
                            wnd.update()
        if i1==7:
            for j1 in [y,q,s,v]:
                if j1==8:
                    for k1 in [y,q,s,v]:
                        if k1==9:
                            cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="PLAYER TWO WINS!!")
                            wnd.update()
        cvs1.create_text(200,50,fill="white",font="Georgia 20 bold",
                                         text="THE GAME IS DRAW")
        wnd.update()
cvs1.pack()
