file = open("day4.txt", "r")
contents = file.read()
file.close()

array = []
row_length = 140

contents = contents.replace('\n', '')
array = [list(contents[i:i+row_length]) for i in range(0, len(contents), row_length)]

xmasCount = 0

def hor(line, space):
    if space + 3 < len(array[line]):
        if array[line][space:space+4] == ['X', 'M', 'A', 'S'] or array[line][space:space+4] == ['S', 'A', 'M', 'X']:
            global xmasCount
            xmasCount += 1

def ver(line, space):
    if line + 3 < len(array):
        if [array[line + i][space] for i in range(4)] == ['X', 'M', 'A', 'S'] or [array[line + i][space] for i in range(4)] == ['S', 'A', 'M', 'X']:
            global xmasCount
            xmasCount += 1

def diag_tl_br(line, space):
    if line + 3 < len(array) and space + 3 < len(array[line]):
        if [array[line + i][space + i] for i in range(4)] == ['X', 'M', 'A', 'S'] or [array[line + i][space + i] for i in range(4)] == ['S', 'A', 'M', 'X']:
            global xmasCount
            xmasCount += 1

def diag_tr_bl(line, space):
    if line + 3 < len(array) and space - 3 >= 0:
        if [array[line + i][space - i] for i in range(4)] == ['X', 'M', 'A', 'S'] or [array[line + i][space - i] for i in range(4)] == ['S', 'A', 'M', 'X']:
            global xmasCount
            xmasCount += 1

for line in range(len(array)):
    for space in range(len(array[line])):
        hor(line, space)
        ver(line, space)
        diag_tl_br(line, space)
        diag_tr_bl(line, space)

print(xmasCount)