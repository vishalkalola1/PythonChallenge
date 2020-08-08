import numpy as np
import queue
import time
input = np.loadtxt("Maze2.txt", dtype='str', delimiter=' ')
input = np.array(input).tolist()
array = []
for obj in input:
    arr = []
    for objsub in obj:
        if objsub == "1":
            arr.append(0)
        elif objsub == "0":
            arr.append(1)
        elif objsub == "s":
            arr.append(1)
        elif objsub == "e":
            arr.append(1)
        else:
            arr.append(1)

    array.append(arr)

print(array)
def printMaze(maze,  startposititon, path=""):
    start = 0
    for x, pos in enumerate(maze[1]):
        if pos == startposititon:
            start = x
            break

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


def valid(maze, moves,startposititon):
    start = 0
    for x, pos in enumerate(maze[1]):
        if pos == startposititon:
            start = x
            break

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


def findEnd(maze, moves,startposititon,endposition):
    start = 0
    for x, pos in enumerate(maze[1]):
        if pos == startposititon:
            start = x
            break

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

    if maze[j][i] == endposition:
        print("Found: " + moves)
        printMaze(maze, startposititon, moves)
        return True

    return False


def main(array,startposiiton,endposition):
    # MAIN ALGORITHM
    nums = queue.Queue()
    nums.put("")
    add = ""
    maze = array
    print("start")
    start_time = time.time()
    while not findEnd(maze, add,startposiiton,endposition):
        add = nums.get()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(maze, put,startposiiton):
                nums.put(put)
    print("--- %d minute ---" % ((time.time() - start_time) / 60))
    print("finished")

main(array,"O","X")
for i, r in enumerate(array):
    for j, c in enumerate(r):
        if c == "b":
            array[i][j] = " "
print(array)
main(array,"O","X1")