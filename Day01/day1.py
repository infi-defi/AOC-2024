#part 1

file = open("day1.txt", "r")
contents = file.read()
file.close()

splitted = contents.split("\n")

A = []
B = []

for i in splitted:
    x = i.split("   ")
    A.append(int(x[0]))
    B.append(int(x[1]))

difference = 0

A.sort()
B.sort()

for i in range(len(A)):
    difference += abs(A[i] - B[i])

print("Answer to Day 1 Part 1:",difference)

#part 2

similarity = 0

for i in range(len(A)):
    count = 0
    for j in range(len(B)):
        if A[i] == B[j]:
            count += 1
    similarity += A[i]*count

print("Answer to Day 1 Part 2: ", similarity)