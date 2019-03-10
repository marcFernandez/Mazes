import sys
import random
import PriorityQueue


class Maze:

    WALL = 1
    EMPTY = 0

    def __init__(self, width, heigth):
        self.maze = dict()
        self.width = width if width % 2 == 1 else width + 1
        self.height = heigth if heigth % 2 == 1 else heigth + 1
        self.out = (self.width - 2, self.height - 2)
        for i in range(self.width):
            self.maze[i] = dict()
            for j in range(self.height):
                self.maze[i][j] = 1

    # Generate the maze
    def generate_maze(self):
        random.seed()
        self.maze[1][1] = self.EMPTY
        self.carve_maze(1, 1)

    # Carve the maze starting at (i,j)
    def carve_maze(self, i, j):
        dir = random.randint(0, 3)
        count = 0
        while count < 4:
            di, dj = 0, 0
            if dir == 0:  # right
                di = 1
            elif dir == 1:  # up
                dj = 1
            elif dir == 2:  # left
                di = -1
            else:  # down
                dj = -1
            i1 = i + di
            j1 = j + dj
            i2 = i1 + di
            j2 = j1 + dj
            if 0 < i2 < self.width and 0 < j2 < self.height:
                if self.maze[i1][j1] == self.WALL and self.maze[i2][j2] == self.WALL:
                    self.maze[i1][j1] = self.EMPTY
                    self.maze[i2][j2] = self.EMPTY
                    self.carve_maze(i2, j2)
            count += 1
            dir = (dir + 1) % 4

    # Display the maze
    def print_maze(self, origen=None, destination=None, solution=None):
        if solution is None:
            solution = [(-1, -1)]

        for j in range(self.height):
            for i in range(self.width):
                if (i, j) == origen:
                    sys.stdout.write(" O ")
                elif (i, j) == destination:
                    sys.stdout.write(" X ")
                elif (i, j) in solution:
                    sys.stdout.write(" . ")
                elif self.maze[i][j] == self.EMPTY:
                    sys.stdout.write("   ")
                else:
                    sys.stdout.write("|||")
            sys.stdout.write("\n")

    # Manhattan distance
    def manhattan_distance(self, s1):
        print s1
        return self.out[0] - s1[0] + self.out[1] - s1[1]

    # Our Heuristic function
    def heuristic(self, state):
        return self.manhattan_distance(state)

    # Successors of 'state'
    def successors(self, state):
        successors = []
        print "Estat:", state
        if self.maze[state[0]+1][state[1]] == self.EMPTY:
            successors.append((state[0]+1, state[1]))
        if self.maze[state[0]-1][state[1]] == self.EMPTY:
            successors.append((state[0]-1, state[1]))
        if self.maze[state[0]][state[1]+1] == self.EMPTY:
            successors.append((state[0], state[1]+1))
        if self.maze[state[0]][state[1]-1] == self.EMPTY:
            successors.append((state[0], state[1]-1))
        return successors

    # Resolve the maze
    def solver(self, origen, destination=None):

        dist = 65

        if destination is None:
            destination = self.out

        statePQueue = PriorityQueue.PriorityQueue()
        explored = []

        current_state = origen
        h = self.heuristic(current_state)

        statePQueue.push([origen, [], 0], h)

        while not statePQueue.is_empty():

            current = statePQueue.pop()

            if current[0] == destination:
                return current[1]
            # if current[2] == dist:
            #     return current[1]

            if current[0] not in explored:
                for successor in self.successors(current[0]):
                    print "Successor de", current, "es:", successor
                    h = self.heuristic(successor)
                    g = current[2]+1
                    statePQueue.push([successor, current[1]+[successor], g], h+g)
            explored.append(current[0])
