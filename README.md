# Embedded Ping Pong Scoreboard

This is a scoreboard for ping pong (or other games) where each player has a button and when pressed it increments their score.  By default the game goes to 21 points and you must win by 2 points.

This project uses [MicroPython](https://micropython.org/) on a ESP8266 microcontroller ([Wemos D1 Mini](https://www.wemos.cc/en/latest/d1/d1_mini.html)). The code reads the button presses, updates the score and displays it on two [Quad 7-Segment Displays](https://lastminuteengineers.com/tm1637-arduino-tutorial/).
