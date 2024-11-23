from time import sleep

maze1 = [['#','#','#','#','#','#','#','#'],
         ['#',' ','#',' ','E','#',' ','#'],
         ['#',' ','#',' ','#','#',' ','#'],
         ['#',' ',' ',' ','#',' ',' ','#'],
         ['#','#',' ','#','#',' ','#','#'],
         ['#',' ',' ','#',' ',' ',' ','#'],
         ['#','S',' ',' ',' ','#',' ','#'],
         ['#','#','#','#','#','#','#','#']]

##########################

dirs = ((0,1),(1,0),(0,-1),(-1,0))

path = []
seen = []

def walk(maze,pos):
    if (pos in seen): 
        return False 
    else: 
        seen.append(pos)

    path.append(pos)

    if (pos[1] < 0 or pos[1] >= len(maze[0]) or pos[0] < 0 or pos[0] >= len(maze)): 
        path.pop()
        return False
    if (maze[pos[0]][pos[1]] == "#"): 
        path.pop()
        return False

    if (maze[pos[0]][pos[1]] == "E"): 
        return True

    for d in dirs:
        if walk(maze,[pos[0]+d[1],pos[1]+d[0]]):
            return True
    
    path.pop()
    return False

def display_maze_path(maze,speed=0.5):
    for step in range(1,len(path)):
        for row in maze: print("".join(row))
        print("\n")
        sleep(speed)
        pos = path[step]
        maze[pos[0]][pos[1]] = "@"

def solve(maze):
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == "S":
                walk(maze,[r,c])
                break
    display_maze_path(maze)

solve(maze1)