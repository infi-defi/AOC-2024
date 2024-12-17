file = open("day8.txt", "r")
contents = file.read()
file.close()

array = []
row_length = 50

contents = contents.replace('\n', '')
array = [list(contents[i:i + row_length]) for i in range(0, len(contents), row_length)]

types = set()

for y, i in enumerate(array):
    for x, j in enumerate(array[y]):
        types.add(array[y][x])

types.discard(".")

types = sorted(types)

antinodes = set()
count = set()

for antena in types:
    antennas = []
    for y, i in enumerate(array):
        for x, j in enumerate(array[y]):
            if array[y][x] == antena:
                antennas.append([y, x])

    # Compute antinode locations
    for idx1, coord1 in enumerate(antennas):
        for idx2, coord2 in enumerate(antennas):
            if idx1 != idx2:  # Exclude itself
                diff_y = abs(coord1[0] - coord2[0])
                diff_x = abs(coord1[1] - coord2[1])
                
                # Calculate new coordinates
                new_y = coord1[0] + diff_y if coord1[0] > coord2[0] else coord1[0] - diff_y
                new_x = coord1[1] + diff_x if coord1[1] > coord2[1] else coord1[1] - diff_x
                 
                count.add((coord1[0], coord1[1]))
                count.add((coord2[0], coord2[1]))
                
                while 0 <= new_y < row_length and 0 <= new_x < row_length:
                    antinodes.add((new_y, new_x))  # Add as a tuple
                    new_y = new_y + diff_y if coord1[0] > coord2[0] else new_y - diff_y
                    new_x = new_x + diff_x if coord1[1] > coord2[1] else new_x - diff_x
                    

merged = antinodes | count
print(len(merged))
