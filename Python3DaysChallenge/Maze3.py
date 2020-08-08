import queue

yd = 'b'
yk = 'a'
rd = 'g'
rk = 'f'
gd = 'c'
gk = 'd'
bd = 'i'
bk = 'h'


class Node:

    def __init__(self, position: (), parent: ()):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    def _eq_(self, other):
        return self.position == other.position

    def _lt_(self, other):
        return self.f < other.f

    def _repr_(self):
        return ('({0},{1})'.format(self.position, self.f))


def result(map, width, height, spacing=2, **kwargs):
    for y in range(height):
        for x in range(width):
            print('%%-%ds' % spacing % result_char(map, (x, y), kwargs), end=' ')
        print()


def result_char(map, position, kwargs):
    value = map.get(position)

    if 'path' in kwargs and position in kwargs['path']:
        value = 'p'


    elif 'start' in kwargs and position == kwargs['start']:
        value = 's'


    elif 'goal' in kwargs and position == kwargs['goal']:
        value = 'e'

    return value


def asearch(map, start, end):
    open = []
    closed = []
    keys = []

    start_node = Node(start, None)
    goal_node = Node(end, None)

    open.append(start_node)

    while len(open) > 0:

        open.sort()

        current_node = open.pop(0)

        closed.append(current_node)

        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent

            return path[::-1]

        (x, y) = current_node.position

        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for next in neighbors:

            map_value = map.get(next)

            if (map_value == '1'):
                continue
            if map_value in (yd, rd, gd, bd):
                continue

            neighbor = Node(next, current_node)

            if (neighbor in closed):
                continue

            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(
                neighbor.position[1] - start_node.position[1])
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(
                neighbor.position[1] - goal_node.position[1])
            neighbor.f = neighbor.g + neighbor.h

            for node in open:
                if (neighbor == node and neighbor.f > node.f):
                    continue

            open.append(neighbor)

    return None


def main():
    # Get a map (grid)
    map = {}
    chars = ['k']
    start = None
    end = None
    row = 0
    col = 0
    colMain = 0

    fp = open('maze3.txt', 'r')
    keys = queue.Queue()
    doors = []
    gost = []

    while len(chars) > 0:

        chars = [str(i) for i in fp.readline().strip()]

        for x in range(len(chars)):
            if (chars[x] != ' '):
                map[(col, row)] = chars[x]
                if (chars[x] == 's'):
                    start = (col, row)
                elif (chars[x] == 'e'):
                    end = (col, row)
                elif chars[x] in (yk, rk, gk, bk):
                    keys.put((col, row))
                elif chars[x] in (yd, rd, gd, bd):
                    doors.append((col, row))
                elif chars[x] not in ('0', '1'):
                    gost.append((col, row))
                col += 1

        if (len(chars) > 0):
            if (row == 0): colMain = col
            if (chars[0]) != ' ':
                row += 1
                col = 0

    fp.close()
    path = []

    key = None
    result(map, colMain, row, spacing=1, path=path, start=start, goal=end)
    continuePath = start
    while (keys.qsize() != 0):
        key = keys.get()
        path1 = asearch(map, continuePath, key)
        print()
        if (path1 != None):
            if (map.get(key) == yk):
                for i in doors:
                    if (map.get(i) != yd):
                        map[i] = '0'
                        continuePath = key
            elif (map.get(key) == rk):
                for i in doors:
                    if (map.get(i) != rd):
                        map[i] = '0'
                        continuePath = key
            elif (map.get(key) == gk):
                for i in doors:
                    if (map.get(i) != gd):
                        map[i] = '0'
                        continuePath = key
            elif (map.get(key) == bk):
                for i in doors:
                    if (map.get(i) != bd):
                        map[i] = '0'
                        continuePath = key
            path += path1
        else:
            keys.put(key)
        if (keys.qsize() == 0):
            path1 = asearch(map, continuePath, end)
            path += path1

    print(path)

    result(map, colMain, row, spacing=1, path=path, start=start, goal=end)


main()