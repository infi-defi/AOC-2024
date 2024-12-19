file = open("day6.txt", "r")
contents = file.read()
file.close()

array = []
row_length = 130

contents = contents.replace('\n', '')
array = [list(contents[i:i+row_length]) for i in range(0, len(contents), row_length)]

player = "^"
startx, starty = 72, 43
PosX, PosY = startx, starty
size = row_length
deadEnd = False
count = 0
visited = set()

# for i in array:
#     for j in i:
#         if j == "^":
#             print(i.index(j),array.index(i))


#      PosY  PosX
move_directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

def checkNext(player, posX, posY):
    directions = {
        "^": (-1, 0, ">"),
        ">": (0, 1, "v"),
        "v": (1, 0, "<"),
        "<": (0, -1, "^")
    }
    dy, dx, new_player = directions[player]
    nextX, nextY = posX + dx, posY + dy
    #print(posY,posX)
    if 0 <= nextX < size and 0 <= nextY < size:
        if array[nextY][nextX] == "#":
            return new_player
        else:
            return player
    else:
        return 0

while not deadEnd:

    i = 0
    while player != 0 and i<5:
        player = checkNext(player, PosX, PosY)
        i += 1

    if player == 0:
        break

    dy, dx = move_directions[player]
    nextX, nextY = PosX + dx, PosY + dy
    

    visited.add((PosY, PosX))
    visited.add((nextY, nextX))


    PosX, PosY = nextX, nextY


# for i in array:
#     for j in i:
#         if j == "X":
#             count += 1

print(f"Part 1: {len(visited)}")
player = "^"
traps = 0
PosX, PosY = startx, starty
repeat = []

#print(visited)

for i in visited:
    y,x = i
    array[y][x] = "#"
    repeat.append((startx, starty))
    while not deadEnd:
        i = 0
        while player != 0 and i<5:
            player = checkNext(player, PosX, PosY)
            i += 1

        if player == 0:
            break

        dy, dx = move_directions[player]
        nextX, nextY = PosX + dx, PosY + dy

        PosX, PosY = nextX, nextY    
        repeat.append((PosY, PosX))

        if repeat.count((PosY, PosX)) > 5:
            deadEnd = True
            #print(repeat.count((PosY, PosX)),PosY, PosX)
    
    if deadEnd == True:
        traps += 1
        #print(f"im not stuck, if {len(visited)} > {traps} you good")
    
    array[y][x] = "."
    deadEnd = False
    player = "^"
    PosX, PosY = startx, starty
    repeat = []

print(f"Part 2: {traps}")