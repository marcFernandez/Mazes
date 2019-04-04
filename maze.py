import MazeGenerator as mg

if __name__ == "__main__":

    w, h = 39, 27
    origen = (1, 1)
    destination = (w - 2, h - 2)
    maze = mg.Maze(w, h)
    maze.generate_maze()
    maze.maze[1][2] = maze.EMPTY
    maze.maze[2][1] = maze.EMPTY
    # maze.print_maze(origen, destination)

    # paths = maze.solver(destination, origen, 2, 50)
    path = maze.solver(origen, destination)
    # print len(paths)
    # maze.print_maze(origen, destination, path)

    while path[0]:
        current_coord = path[0][0]
        print current_coord
        path[0].pop(0)
        maze.print_maze(origen, destination, pacman=current_coord)

