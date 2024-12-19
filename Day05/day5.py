file = open("day5.txt", "r")
contents = file.read()
file.close()

rules = []
update = []

contents = contents.split("\n")
for i in contents:
    if "|" in i:
        rules.append(i)
    else:
        update.append(i)

rulesX = []
rulesY = []

for i in rules:
    x = i.split("|")
    rulesX.append(int(x[0]))
    rulesY.append(int(x[1]))


update = [item for item in update if item != '']

count = 0
count2 = 0


def create_adjacency_matrix(list1, list2):
    # Get all unique elements from both lists
    unique_nodes = sorted(set(list1 + list2))
    
    # Create a mapping from node to index
    node_to_index = {node: idx for idx, node in enumerate(unique_nodes)}
    
    # Initialize adjacency matrix
    n = len(unique_nodes)
    adjacency_matrix = [[0] * n for _ in range(n)]
    
    # Fill the adjacency matrix based on list1 and list2
    for parent, child in zip(list1, list2):
        i = node_to_index[parent]
        j = node_to_index[child]
        adjacency_matrix[i][j] = 1
    
    return adjacency_matrix, unique_nodes

adj_matrix, nodes = create_adjacency_matrix(rulesX, rulesY)

def fixThis(adj_matrix,lst):
    for v in range(len(lst)*len(lst)):
        for index, element in enumerate(lst):
            for i in lst[index:]:
                if adj_matrix[nodes.index(i)][nodes.index(element)] == 1:
                    lst[lst.index(i)], lst[lst.index(element)] = lst[lst.index(element)], lst[lst.index(i)]
    return  lst[len(lst) // 2]




for i in update:
    lst = i.split(",")
    lst = list(map(int, lst))
    skip = False  # Flag to track if we need to skip to the next `i`
    
    for j, element in enumerate(lst):
        if element in rulesY:
            positions = [k for k, y in enumerate(rulesY) if y == element]
            
            # Check if the corresponding `rulesX` is in the rest of `lst`
            for l in positions:
                if rulesX[l] in lst[j + 1:]:
                    skip = True
                    count2 += fixThis(adj_matrix,lst)
                    break  # Exit `positions` loop
            
            if skip:
                break  # Exit `j` loop
    
    if not skip:
        count += lst[len(lst) // 2]




print(count)
print(count2)