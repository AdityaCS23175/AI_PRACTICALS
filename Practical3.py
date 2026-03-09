# Analyze a suitable technique to build a tic-tac-toe game engine with an AI player in Python
import math

b = [" "]*9

def show():
    for i in range(0,9,3):
        print(b[i], "|", b[i+1], "|", b[i+2])
    print()

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),
         (1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[x]==b[y]==b[z]==p for x,y,z in w)

def minimax(ai):
    if win("O"): return 1
    if win("X"): return -1
    if " " not in b: return 0

    best = -math.inf if ai else math.inf
    for i in range(9):
        if b[i]==" ":
            b[i] = "O" if ai else "X"
            s = minimax(not ai)
            b[i] = " "
            best = max(best,s) if ai else min(best,s)
    return best

def ai():
    best, move = -math.inf, -1
    for i in range(9):
        if b[i]==" ":
            b[i]="O"
            s=minimax(False)
            b[i]=" "
            if s>best:
                best,move=s,i
    b[move]="O"

while True:
    show()
    p=int(input("Enter position 1-9: "))-1
    if b[p]==" ": b[p]="X"
    else: continue

    if win("X"): show(); print("You win"); break
    if " " not in b: show(); print("Draw"); break

    ai()
    if win("O"): show(); print("AI wins"); break