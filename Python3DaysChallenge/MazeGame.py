import numpy as np
import queue
import time
input = np.loadtxt("maze1.txt", dtype='str', delimiter=' ')
input = np.array(input).tolist()
array = []
for obj in input:
    arr = []
    for objsub in obj:
        if objsub == "1":
            arr.append("#")
        elif objsub == "0":
            arr.append(" ")
        elif objsub == "s":
            arr.append("O")
        elif objsub == "e":
            arr.append("X")
    array.append(arr)


def printMaze(maze, path=""):
    start = 0
    for x, pos in enumerate(maze[1]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    start = 0
    for x, pos in enumerate(maze[1]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
    start = 0
    for x, pos in enumerate(maze[1]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False


# MAIN ALGORITHM
nums = queue.Queue()
nums.put("")
add = ""
maze = array
print("start")
start_time = time.time()
while not findEnd(maze, add):
    add = nums.get()
    # print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)
print("--- %d minute ---" % ((time.time() - start_time)/60))
print("finished")