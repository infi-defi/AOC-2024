with open('day9.txt') as file:
    file = file.read().strip()

disk = []
index = 0

for i, item in enumerate(file):
    num = int(item)
    if i % 2 == 0:
        disk.extend([index] * num)
        index += 1
    else:
        disk.extend(['.'] * num)

def get_sum(disk):
    s = 0
    for i, x in enumerate(disk):
        if x != ".":
            s += i * x
    return s

def solve1(disk):
    front = 0
    back = len(disk) - 1

    while True:
        while disk[front] != '.':
            front += 1
        while disk[back] == '.':
            back -= 1
        if front > back:
            break

        disk[front], disk[back] = disk[back], disk[front]

    return get_sum(disk)

def solve2(disk):
    back = len(disk) - 1

    while True:
        index = None
        takeFrom = []
        putTo = []

        while back >= 0:
            item = disk[back]
            if item != '.' and (index == None or index == item):
                index = item
                takeFrom.append(back)
                back -= 1
            elif item == '.' and len(takeFrom) == 0:
                back -= 1
            else:
                break

        front = 0

        while front <= back:
            item = disk[front]
            if item == '.':
                putTo.append(front)
                if len(putTo) == len(takeFrom):
                    for a, b in zip(takeFrom, putTo):
                        disk[a], disk[b] = disk[b], disk[a]

                    break
            else:
                putTo = []
            front += 1

        if back < 0:
            break

    return get_sum(disk)


part1 = solve1(disk.copy())
part2 = solve2(disk.copy())

print(part1)
print(part2)