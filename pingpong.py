import tkinter as tk
import random as ran

button1 = 0
button2 = 0
chain1 = 0
chain2 = 0

def reset():
    button1 = 0
    button2 = 0
    chain1 = 0
    chain2 = 0
    print("the game has been reset")
    update_score()

def update_score():
    home_score.set(button1)
    away_score.set(button2)
    special()

def increment():
    global button1, chain1, chain2
    button1 += 1
    chain1 += 1
    chain2 = 0
    update_score()

def decrement():
    global button2, chain1, chain2
    button2 += 1
    chain2 += 1
    chain1 = 0
    update_score()

def special():
    if(button1 == 21 and button2 < 20):
        print("Home team wins")
        reset()
    elif(button2 == 21 and button1 < 20):
        print("Away team wins")
        reset()
    elif(button1 > 19 and button1 == button2):
        print("deuce")
    elif(button1 == button2 + 2 and button2 > 19):
        print("Home team wins")
        reset()
    elif(button2 == button1 + 2 and button1 > 19):
        print("Away team wins")
        reset()
    elif(button1 == button2 + 1 and button2 > 19):
        print("Advantege Home team")
    elif(button2 == button1 + 1 and button1 > 19):
        print("Advantege Away team")
    elif(button1 == button2):
        print("tie game")
    elif(button1 == 20):
        print("Home team is about to win")
    elif(button2 == 20):
        print("Away team is about to win")
    elif(button1 > button2 + 10 and chain1 != 0):
        print("Home team is destroying Away team")
    elif(button2 > button1 + 10 and chain2 != 0):
        print("Away team is destroying Home team")
    
    if(button1 > button2 + 2 and chain2 == 5):
        print("Away team is on come back")
    elif(button2 > button1 + 2 and chain1 == 5):
        print("Home team is on come back")

    if(chain1 == 3):
        print("Home team is heating up")
    elif(chain2 == 3):
        print("Away team is heating up")
    elif(chain1 == 5):
        print("Home team is on fire")
    elif(chain2 == 5):
        print("Away team is on fire")
    elif(chain1 == 7):
        print("Home team needs to be stoped")
    elif(chain2 == 7):
        print("Away team needs to be stoped")
    


print("Welcome to the national basement ping pong competion\n")

parent = tk.Tk()
frame = tk.Frame(parent)
frame.pack()

home_score = tk.IntVar()
away_score = tk.IntVar()
result = tk.StringVar()

label_home = tk.Label(frame, text="Home: ")
label_home_score = tk.Label(frame, textvariable=home_score)
label_home.pack(side=tk.LEFT)
label_home_score.pack(side=tk.LEFT)

label_away = tk.Label(frame, text=" Away: ")
label_away_score = tk.Label(frame, textvariable=away_score)
label_away.pack(side=tk.LEFT)
label_away_score.pack(side=tk.LEFT)

text_disp = tk.Button(frame, text="Home", command=increment)
text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame, text="Away", fg="green", command=decrement)
exit_button.pack(side=tk.RIGHT)

label_result = tk.Label(frame, textvariable=result)
label_result.pack()

parent.mainloop()

        
