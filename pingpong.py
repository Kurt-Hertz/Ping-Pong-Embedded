import time
from machine import Pin, Signal

import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('TaylorMade', 'Taz/Mania')

import mip
mip.install("github:mcauser/micropython-tm1637")

import tm1637
# Pinout for Wemos D1 mini:
# https://static3.gleanntronics.ie/eng_pl_WeMos-D1-Mini-ESP8266-12F-Module-Arduino-IoT-426_2.jpg
tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

score1 = 0
score2 = 0
chain1 = 0
chain2 = 0

def reset():
    global score1, score2, chain1, chain2
    score1 = 0
    score2 = 0
    chain1 = 0
    chain2 = 0
    print("the game has been reset")
    update_score()

def update_score():
    display()
    special()

def player1_scored():
    global score1, chain1, chain2
    score1 += 1
    chain1 += 1
    chain2 = 0
    update_score()

def player2_scored():
    global score2, chain1, chain2
    score2 += 1
    chain2 += 1
    chain1 = 0
    update_score()

def display():
    global tm
    tm.numbers(score1, score2)

def special():
    global score1, score2, chain1, chain2
    if(score1 == 21 and score2 < 20):
        print("Home team wins")
        reset()
    elif(score2 == 21 and score1 < 20):
        print("Away team wins")
        reset()
    elif(score1 > 19 and score1 == score2):
        print("deuce")
    elif(score1 == score2 + 2 and score2 > 19):
        print("Home team wins")
        reset()
    elif(score2 == score1 + 2 and score1 > 19):
        print("Away team wins")
        reset()
    elif(score1 == score2 + 1 and score2 > 19):
        print("Advantege Home team")
    elif(score2 == score1 + 1 and score1 > 19):
        print("Advantege Away team")
    elif(score1 == score2):
        print("tie game")
    elif(score1 == 20):
        print("Home team is about to win")
    elif(score2 == 20):
        print("Away team is about to win")
    elif(score1 > score2 + 10 and chain1 != 0):
        print("Home team is destroying Away team")
    elif(score2 > score1 + 10 and chain2 != 0):
        print("Away team is destroying Home team")
    
    if(score1 > score2 + 2 and chain2 == 5):
        print("Away team is on come back")
    elif(score2 > score1 + 2 and chain1 == 5):
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

pin2 = Pin(2, Pin.OUT)
#pin2 = Signal(2, Pin.OUT, inverted=True)

def main():
    global score1, score2
    while True:
        display()
        player1_scored()
        player2_scored()
        if score1 >= 21 or score2 >= 21:
            reset()
    


        
