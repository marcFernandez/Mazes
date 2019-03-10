import MazeGenerator as mg

if __name__ == "__main__":

    w, h = 39, 27
    origen = (1, 1)
    destination = (w - 2, h - 2)
    maze = mg.Maze(w, h)
    maze.generate_maze()
    maze.maze[1][2] = maze.EMPTY
    maze.maze[2][1] = maze.EMPTY
    maze.print_maze(origen, destination)

    path = maze.solver(origen)
    maze.print_maze(origen, destination, path)
