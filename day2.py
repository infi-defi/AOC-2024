#part 1
file = open("day2.txt", "r")
contents = file.read()
file.close()

splitted = contents.split("\n")


safe = 0

for i in splitted:
    lst = i.split(" ")
    #lst = ['7','10','11','14']
    lst = list(map(int,lst))
    sort = False
    nums = False
    #print(sorted(lst))

    if sorted(lst, reverse=True) == lst or sorted(lst) == lst:
        sort = True

    for j in range(len(lst) -1):
        if 0 < abs(lst[j] - lst[j+1]) < 4:
            nums = True
        else:
            nums = False
            break

    if sort and nums:
        safe += 1

print("The answer to the 1st part is: ",safe)

#part 2

def CheckList(data):
    inc, dec = False, False
    for i in range(len(data) - 1):
        diff = data[i] - data[i+1]
        if not (0 < abs(diff) < 4):
            return False
        if diff > 0:
            inc = True
        if diff < 0:
            dec = True  
        if inc and dec:
            return False
    return True


result = 0
for i in splitted:
    lst = i.split(" ")
    lst = list(map(int,lst))
    if CheckList(lst):
        result += 1

print("Part 1: ", result)

result = 0
for i in splitted:
    lst = i.split(" ")
    lst = list(map(int,lst))
    check = CheckList(lst)
    if not check:        
        for i in range(len(lst)):
            removed = lst[i]
            lst.pop(i)
            check = CheckList(lst)
            if check:
                break
            lst.insert(i, removed)
    if check:
        result += 1

print("Part 2: ", result)