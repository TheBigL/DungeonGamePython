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
    edge = 0
    doorCount = 0

    

    while True:
        print("Select your difficulty")
        print("Type EASY, NORMAL, HARD, VERY HARD or INTENSE")
        print("..or you can type QUIT or EXIT to leave the game")
        try:
            level = input(">").upper()
            if level == 'EASY':
                difficulty = easy
                monsterCount = difficulty
                edge = difficulty
                doorCount = 5
                break

            elif level == 'NORMAL':
                difficulty = normal
                monsterCount = normal
                edge = difficulty
                doorCount = 4
                break


            elif level == 'HARD':
                difficulty = hard
                monsterCount = difficulty
                edge = difficulty
                doorCount = 3
                break


            elif level == 'VERY HARD':
                difficulty = veryHard
                monsterCount = veryHard
                doorCount = 2
                edge = veryHard
                break


            elif level == 'INTENSE':
                difficulty = intense
                monsterCount = intense
                doorCount = 1
                edge = intense
                break
            elif level == 'QUIT' or level == 'EXIT':
                print('Goodbye for now...')
                break
                exit()
                

            else:
                print("Not a valid response!")
    
                
        except:
            print("Didn't catch that...")
    return monsterCount, doorCount, edge        
        


        

             


def generateLocations(monsterCount, doorCount, dungeonMAP, monsters, doors):
 
    while True:

        player = random.choice(dungeonMAP)

            #Creating and Generating the Monsters and Doors
        while len(monsters) < monsterCount:
            monster = random.choice(dungeonMAP)
            monsters.append(monster)

        while len(doors) < doorCount:
            door = random.choice(dungeonMAP)
            doors.append(door)
        if not (monster == player and monster == door and player == door):
            break
    return monsters, player, doors                

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
doors = []
monsters = []
doorCount = 0
print("Welcome to the Dungeon Game")
input("Press ENTER to play the game!")

monsterCount, doorCount, edge = setDifficulty()
dungeonMAP = buildMap(monsterCount)
startPositions = generateLocations(monsterCount, doorCount, dungeonMAP, monsters, doors)



#def playGame():
    
