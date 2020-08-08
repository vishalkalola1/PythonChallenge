import pygame
import sys
from BackTrack import Maze, Test
from sprites import *
pygame.init()

xposition = 0
yposition = 0
width = 50
height = 50
GREEN =(0,200,0)

test = Test("Maze2.txt")
data = test.maze.data

screen = pygame.display.set_mode((width * len(data), width * len(data)))
screen.fill(GREEN)

blockimg = pygame.image.load("sprites/block.png")
avatar = pygame.image.load("sprites/pacman.png")
path = pygame.image.load("sprites/path.png")
result = pygame.image.load("sprites/reward.png")
a = pygame.image.load("sprites/green_key.png")
b = pygame.image.load("sprites/green_door.png")


def player(x,y):
    return screen.blit(avatar, (x, y))

players = player(width, height)

def makeBoard(data, xposition,yposition):
    for (i,tempdata) in enumerate(data):
        for (j,obj) in enumerate(tempdata):
            if obj == "1":
                screen.blit(blockimg,(xposition,yposition))
            elif obj == "e":
                screen.blit(result, (xposition, yposition))
            elif obj == "a":
                screen.blit(a, (xposition, yposition))
            elif obj == "b":
                screen.blit(b, (xposition, yposition))
            else:
                screen.blit(path, (xposition, yposition))
            xposition += width
        yposition += height
        xposition = 0

makeBoard(data,xposition,yposition)

test.solveProblem()
test.test()
solution = test.solution

running = True
temp = height
tempx = temp
tempy = temp
count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    temp += 1
    if temp % width == 0:
        count += 1

    if temp < 100:
        tempy = temp

    if solution[count] == "v":
        tempy += 1
    if solution[count] == "^":
        tempy -= 1
    if solution[count] == ">":
        tempx += 1
    if solution[count] == "<":
        tempx -= 1

    player(tempx,tempy)

    pygame.display.update()
