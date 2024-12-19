file = open("day4.txt", "r")
contents = file.read()
file.close()

array = []
row_length = 140

contents = contents.replace('\n', '')
array = [list(contents[i:i+row_length]) for i in range(0, len(contents), row_length)]

xmasCount = 0

def diag_tl_br(line, space):
    if line + 2 < len(array) and space + 2 < len(array[line]):
        if [array[line + i][space + i] for i in range(3)] == ['M', 'A', 'S'] or [array[line + i][space + i] for i in range(3)] == ['S', 'A', 'M']:
            return True

def diag_tr_bl(line, space):
    space += 2
    if line + 2 < len(array) and space - 2 >= 0:
        if [array[line + i][space - i] for i in range(3)] == ['M', 'A', 'S'] or [array[line + i][space - i] for i in range(3)] == ['S', 'A', 'M']:
            return True

for line in range(len(array)):
    for space in range(len(array[line])):

        if diag_tl_br(line, space) and diag_tr_bl(line, space):
            xmasCount += 1

print(xmasCount)