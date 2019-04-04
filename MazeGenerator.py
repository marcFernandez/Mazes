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
        for i in range(1, self.width-2):
            self.maze[i][self.height/2] = self.EMPTY
        for j in range(1, self.height-2):
            self.maze[6][j] = self.EMPTY
            self.maze[17][j] = self.EMPTY
            self.maze[25][j] = self.EMPTY
        # ct = 0
        # while(ct<100):
        #     x = random.randint(2, self.width-2)
        #     y = random.randint(2, self.height-2)
        #     if self.maze[x][y] == self.WALL:
        #         if self.maze[x+1][y] == self.EMPTY and self.maze[x-1][y] == self.EMPTY or self.maze[x][y+1] == self.EMPTY and self.maze[x][y-1] == self.EMPTY:
        #             self.maze[x][y] == self.EMPTY
        #             coord = (x, y)
        #             print "Deleting",coord,"wall"
        #             ct += 1

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
    def print_maze(self, origen=None, destination=None, solution=None, pacman=None):
        if solution is None:
            solution = [(-1, -1)]

        for j in range(self.height):
            for i in range(self.width):
                if (i, j) == origen:
                    sys.stdout.write(" O ")
                elif (i, j) == destination:
                    sys.stdout.write(" X ")
                elif (i, j) in solution[0]:
                    sys.stdout.write(" 1 ")
                elif pacman and (i, j) == pacman:
                    sys.stdout.write(" C ")
                elif self.maze[i][j] == self.EMPTY:
                    sys.stdout.write("   ")
                else:
                    sys.stdout.write("|||")
            sys.stdout.write("\n")

    # Manhattan distance
    def manhattan_distance(self, s1, s2=None):
        if s2 is None:
            return self.out[0] - s1[0] + self.out[1] - s1[1]
        else:
            return abs(s1[0]-s2[0]) + abs(s1[1]-s2[1])

    # Our Heuristic function
    def heuristic(self, state):
        return self.manhattan_distance(state)

    # Successors of 'state'
    def successors(self, state):
        successors = []
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
    def solver(self, origen, destination=None, num_paths=1, dist=None):

        solutions = []

        if destination is None:
            destination = self.out

        statePQueue = PriorityQueue.PriorityQueue()
        explored = []

        current_state = origen
        h = self.heuristic(current_state)

        statePQueue.push([origen, [], 0], h)

        while not statePQueue.is_empty():

            current = statePQueue.pop()

            if dist is None:
                if current[0] == destination or current[2] == dist:
                    solutions.append(current[1])
            elif current[0] == destination or current[2] == dist:
                if len(solutions) == 0:
                    print current[1]
                    solutions.append(current[1])
                elif self.manhattan_distance(current[0], solutions[0][dist-1]) > 20:
                    print "la dist entre", current[0],"i",solutions[0][dist-1],"> 8"
                    print current[1]
                    solutions.append(current[1])
            if len(solutions) == num_paths:
                return solutions

            # if current[2] == dist:
            #     return current[1]

            if current[0] not in explored:
                for successor in self.successors(current[0]):
                    h = self.heuristic(successor)
                    g = current[2]+1
                    statePQueue.push([successor, current[1]+[successor], g], h+g)
            explored.append(current[0])
