with open('day10.txt', 'r') as f:
    file = f.read().splitlines()

gridSize = 47

directions=[
    (-1,0),
    (1,0),
    (0,1),
    (0,-1)
]

starts = []

for i, line in enumerate(file):
    for j, char in enumerate(line):
        if char == '0':
            starts.append((i,j))

def check(startY, startX, count):

    y, x = startY, startX
    locations = []

    for direction in directions:
        dy, dx = y + direction[0], x + direction[1]
        if 0 <= dx < gridSize and 0 <= dy < gridSize:
            #print(f"start at {y,x} : {file[y][x]} check if {dy,dx} : {file[dy][dx]} = {str(count)}")
            if file[dy][dx] == str(count):
                locations.append((dy, dx))
    return locations

alls = []

for start in starts:
    y, x = start
    count = 1
    locations = check(y, x, count)
    
    while True:
        count += 1
        nextLoc = []

        if count > 9 or locations == []:
            break

        for location in locations:
            y, x = location
            nextLoc.extend(check(y, x, count))

        locations = set(nextLoc) # for part 1
        #locations = nextLoc # for part 2
    for i in locations:
        alls.append(i)

print(len(alls))

