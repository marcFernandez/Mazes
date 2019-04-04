import random
import PriorityQueue


class Entity:

    moves = ['UP', 'DOWN', 'RIGHT', 'LEFT']

    def __init__(self, maze):
        self.position = (1, 1)
        self.maze = maze

    @staticmethod
    def to_string():
        return " C "

    def available_movements(self):
        movements = []
        for move in self.moves:
            i, j = self.move(move, True)
            if self.maze[i][j] == 0:
                movements.append(move)
        return movements

    def move(self, movement, check=False):
        if not check:
            if movement == 'UP':
                self.position = (self.position[0], self.position[1] + 1)
            elif movement == 'DOWN':
                self.position = (self.position[0], self.position[1] - 1)
            elif movement == 'RIGHT':
                self.position = (self.position[0] + 1, self.position[1])
            else:
                self.position = (self.position[0] - 1, self.position[1])
        else:
            if movement == 'UP':
                return self.position[0], self.position[1] + 1
            elif movement == 'DOWN':
                return self.position[0], self.position[1] - 1
            elif movement == 'RIGHT':
                return self.position[0] + 1, self.position[1]
            else:
                return self.position[0] - 1, self.position[1]
