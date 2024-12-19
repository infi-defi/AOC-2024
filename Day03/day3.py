file = open("day3.txt", "r")
contents = file.read()
file.close()

contents = list(contents)

enabled = True
alls = 0

for i in range(len(contents)):
    ends = False
    commas = False
    
    if contents[i] == "d" and contents[i+1] == "o" and contents[i+2] == "n":
        enabled = False
        #print("died")
    elif contents[i] == "d" and contents[i+1] == "o":
        #print("lived")
        enabled = True


    if enabled and contents[i] == "m" and contents[i+1] == "u" and contents[i+2] == "l" and contents[i+3] == "(":
        for index in range(i+3,i+12):
            if contents[index] == ")":
                end = index
                break
        start = i+4
        for index in range(i+3,i+8):
            if contents[index] == ",":
                comma = index
                break
                
        first = ""
        second = ""

        for j in range(start,comma):
            first += contents[j]
        for k in range(comma+1,end):
            second += contents[k]
        if first != "" and second != "":
            alls += int(first)*int(second)
            #print(int(first)*int(second))
        
print(alls)

