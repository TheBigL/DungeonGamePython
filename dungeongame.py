#Author: Leban Mohamed
#Project: Dungeon Game

import random
import sys
import os
#pylint: disable=unused-variable

monsterCount = 0
def setDifficulty():
    easy = 4
    normal = 8
    hard = 12
    veryHard = 16
    intense = 20
    
    

    while True:
        print("Select your difficulty")
        print("Type EASY, NORMAL, HARD, VERY HARD or INTENSE")
        difficulty = input(">").upper()
        if difficulty == 'EASY':
            monsterCount = easy
            difficulty = easy
            edge = easy
            buildMap(difficulty)
            break

        elif difficulty == 'NORMAL':
            difficulty = normal
            monsterCount = normal
            edge = normal
            buildMap(difficulty)

        elif difficulty == 'HARD':
            difficulty = hard
            monsterCount = hard
            edge = hard
            buildMap(difficulty)

        elif difficulty == 'VERY HARD':
            difficulty = veryHard
            monsterCount = veryHard
            buildMap(difficulty)

        elif difficulty == 'INTENSE':
            difficulty = intense
            monsterCount = intense
            buildMap(difficulty)

        else:
            print("Not a valid response!")
            print("Please pick the following difficulties")        

def buildMap(size):
    xAxis = list(range(0, size))
    yAxis = list(range(0, size))
    dungeonMAP = []
    

    for xPoint in xAxis:
        for yPoint in yAxis:
            gridPoint = (xPoint, yPoint)
            dungeonMAP.append(gridPoint)
    return dungeonMAP

def exit():
    sys.exit()
      



monsterCount = 0
print("Welcome to the Dungeon Game")
setDifficulty()
