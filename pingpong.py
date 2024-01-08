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


class Scoreboard:
    def __init__(self, maxScore, winby):
        self.score1 = 0
        self.score2 = 0
        self.chain1 = 0
        self.chain2 = 0
        self.winby = winby
        self.maxScore = maxScore
        self.tm = tm1637.TM1637(clk=Pin(4), dio=Pin(0)) # Pins D2 and D3
    def reset(self):
        self.score1 = 0
        self.score2 = 0
        self.chain1 = 0
        self.chain2 = 0
        print("the game has been reset")
        self.update_score()
    def update_score(self):
        self.display()
        self.special()
    def player1_scored(self):
        self.score1 += 1
        self.chain1 += 1
        self.chain2 = 0
        self.update_score()
    def player2_scored(self):
        self.score2 += 1
        self.chain2 += 1
        self.chain1 = 0
        self.update_score()
    def display(self):
        self.tm.numbers(self.score1, self.score2)
    def special(self):
        if(self.score1 == self.maxScore and self.score2 < (self.maxScore -1)):
            print("Home team wins")
            self.reset()
        elif(self.score2 == self.maxScore and self.score1 < (self.maxScore -1)):
            print("Away team wins")
            self.reset()
        elif(self.score1 > (self.maxScore -self.winby) and self.score1 == self.score2):
            print("deuce")
        elif(self.score1 == self.score2 + self.winby and self.score2 > (self.maxScore -self.winby)):
            print("Home team wins")
            self.reset()
        elif(self.score2 == self.score1 + self.winby and self.score1 > (self.maxScore -self.winby)):
            print("Away team wins")
            self.reset()
        elif(self.score1 == self.score2 + 1 and self.score2 > (self.maxScore -self.winby)):
            print("Advantege Home team")
        elif(self.score2 == self.score1 + 1 and self.score1 > (self.maxScore -self.winby)):
            print("Advantege Away team")
        elif(self.score1 == self.score2):
            print("tie game")
        elif(self.score1 == (self.maxScore -1)):
            print("Home team is about to win")
        elif(self.score2 == (self.maxScore -1)):
            print("Away team is about to win")
        elif(self.score1 > self.score2 + 10 and self.chain1 != 0):
            print("Home team is destroying Away team")
        elif(self.score2 > self.score1 + 10 and self.chain2 != 0):
            print("Away team is destroying Home team")
        if(self.score1 > self.score2 + self.winby and self.chain2 == 5):
            print("Away team is on come back")
        elif(self.score2 > self.score1 + self.winby and self.chain1 == 5):
            print("Home team is on come back")
        if(self.chain1 == 3):
            print("Home team is heating up")
        elif(self.chain2 == 3):
            print("Away team is heating up")
        elif(self.chain1 == 5):
            print("Home team is on fire")
        elif(self.chain2 == 5):
            print("Away team is on fire")
        elif(self.chain1 == 7):
            print("Home team needs to be stoped")
        elif(self.chain2 == 7):
            print("Away team needs to be stoped")
        
print("Welcome to the national basement ping pong competion\n")

button1 = Pin(12, Pin.OUT)

button2 = Pin(14, Pin.OUT)
#pin2 = Signal(self.winby, Pin.OUT, inverted=True)

def main():
    sb = Scoreboard(21 , 2)
    button1 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP) # Pin D6
    button2 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP) # Pin D5
    while True:
        sb.display()
        if (button1.value() == 1):
             sb.player1_scored()
             time.sleep(1) 
        elif (button2.value() == 1):
             sb.player2_scored()
             time.sleep(1) 
        
    


        
