import operator
import sys



class Maze(object):

    def __init__(self):
        self.start = ''
        self.data = []
        self.roadMap = []
        self.keys = []

    def read_file(self, path):
        maze = []
        with open(path) as f:
            for line in f.read().splitlines():
                ll = []
                for l in line:
                    if l != " ":
                        ll.append(l)
                maze.append(list(ll))
        self.data = maze

    def write_file(self, path):

        with open(path, 'w') as f:
            for r, line in enumerate(self.data):
                f.write('%s\n' % ''.join(line))

    def find(self, symbol):
        for r, line in enumerate(self.data):
            try:
                return r, line.index(self.start)
            except ValueError:
                pass

    def get(self, where):
        r, c = where
        return self.data[r][c]

    def set(self, where, symbol):
        r, c = where
        if where == '.':
            self.roadMap.pop()
        else:
            self.roadMap.append(str([r, c]))
        self.data[r][c] = symbol

    def _str_(self):
        return '\n'.join(''.join(r) for r in self.data)




class Test:

    def __init__(self,filename):
        self.res = []
        self.start = 's'
        self.end = 'a'
        self.solution = []
        self.filename = filename

        #source to key
        self.maze = Maze()
        self.maze.start = self.start
        self.maze.read_file(filename)

    def test(self):
        temp = self.solution
        self.start = 'a'
        self.end = 'e'
        self.maze.start = self.start
        self.maze.data = []
        self.maze.roadMap = []
        self.maze.keys = []
        self.maze.read_file(self.filename)
        self.changeSourceDestination()
        self.solveProblem()
        temp = temp[:-1]
        self.solution[0] = "v"
        temp += self.solution
        self.solution = temp

    def changeSourceDestination(self):
        for row in self.maze.data:
            for index in range(len(row)):
                if row[index] == 'b':
                    row[index] = "0"
                    break

    def solveProblem(self):
        self.solution = self.solve(self.maze)
        for i in self.maze.roadMap:
            if i not in self.res:
                self.res.append(i)
        if self.solution:
            print('Found end of maze at %s' % self.solution)
        else:
            print('No solution (no start, end, or path)')

    def solve(self, maze, where=None, direction=None):
        start_symbol = self.start
        end_symbol = self.end
        vacant_symbol = '0'

        backtrack_symbol = '.'
        directions = (0, 1), (1, 0), (0, -1), (-1, 0)
        direction_marks = '>', 'v', '<', '^'

        where = where or maze.find(start_symbol)
        if not where:
            # no start cell found
            return []
        if maze.get(where) == end_symbol:
            # standing on the end cell
            return [end_symbol]
        if maze.get(where) not in (vacant_symbol, start_symbol):
            # somebody has been here
            return []

        for direction in directions:
            next_cell = list(map(operator.add, where, direction))  # added `list()` for Python 3

            # spray-painting direction
            marker = direction_marks[directions.index(direction)]
            if maze.get(where) != start_symbol:
                maze.set(where, marker)

            sub_solve = self.solve(maze, next_cell, direction)
            if sub_solve:
                is_first_step = maze.get(where) == start_symbol
                return ([start_symbol] if is_first_step else []) + ([] if is_first_step else [marker]) + sub_solve

        # no directions worked from here - have to backtrack
        maze.set(where, backtrack_symbol)
        return []