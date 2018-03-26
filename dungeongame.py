#Author: Leban Mohamed
#Project: Dungeon Game

import random
import sys
import os

#pylint-disable:unused-variable


#Sets the difficulty for the 

def setDifficulty():
    easy = 4
    normal = 8
    hard = 12
    veryHard = 16
    intense = 20
    monsterCount = 0
    monsters = []
    dungeonMAP = []
    edge = 0

    

    while True:
        print("Select your difficulty")
        print("Type EASY, NORMAL, HARD, VERY HARD or INTENSE")
        try:
            difficulty = input(">").upper()
            if difficulty == 'EASY':
                difficulty = easy
                monsterCount = difficulty
                edge = difficulty
                doorCount = 5
                level = 'easy'
                dungeonMAP = buildMap(difficulty)
                break

            elif difficulty == 'NORMAL':
                difficulty = normal
                monsterCount = normal
                edge = normal
                dungeonMAP = buildMap(difficulty)
                doorCount = 4
                break


            elif difficulty == 'HARD':
                difficulty = hard
                monsterCount = hard
                edge = hard
                dungeonMAP = buildMap(difficulty)
                doorCount = 3
                level = 'hard'
                break


            elif difficulty == 'VERY HARD':
                difficulty = veryHard
                monsterCount = veryHard
                dungeonMAP = buildMap(difficulty)
                doorCount = 2
                level = 'very hard'
                break


            elif difficulty == 'INTENSE':
                difficulty = intense
                monsterCount = intense
                dungeonMAP = buildMap(difficulty)
                doorCount = 1
                level = 'intense'
                break
            else:
                print("Not a valid response!")
            return difficulty, monsterCount, edge, level    
                
        except:
            print("Didn't catch that...")
            print("Please pick the following difficulties")
            print("Select your difficulty")
            print("Type EASY, NORMAL, HARD, VERY HARD or INTENSE")
            input("\n>")
        


        

             


def generateLocations(monsterCount, dungeonMAP, monsters, doors):
    locations = {}
    monsters = []
    
    while True:

        player = random.choice(dungeonMAP)

        for monster in monsterCount:
            monster = random.choice(dungeonMAP)
            monsters.append(monster)
            for door in doors:
                door = random.choice(dungeonMAP)
                doors.append(door)

                if monster not in player:
                    continue
                elif monster not in door:
                    continue    
                elif door not in player:
                    continue


        
            
        

        
        if door not in player and monsters not in door and monsters not in player:
         break
    return monsters, player, door                

def draw_map(player, currentRoom, monsters, doorCount):
    print(" _" * edge)
    row = edge - 1

    

    tile = "|{}"
                    


def buildMap(size):
    xAxis = list(range(0, size))
    yAxis = list(range(0, size))
    
    

    for xPoint in xAxis:
        for yPoint in yAxis:
            gridPoint = (xPoint, yPoint)
            dungeonMAP.append(gridPoint)
    return dungeonMAP

def exit():
    sys.exit()
      



monsterCount = 0
edge = 0
dungeonMAP = []
print("Welcome to the Dungeon Game")
input("Press ENTER to play the game!")
setDifficulty()



#def playGame():
    
