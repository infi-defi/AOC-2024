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





def create_adjacency_matrix(list1, list2):
    # Get all unique elements from both lists
    unique_nodes = sorted(set(list1 + list2))
    
    # Create a mapping from node to index
    node_to_index = {node: idx for idx, node in enumerate(unique_nodes)}
    
    # Initialize an adjacency matrix with zeros
    n = len(unique_nodes)
    adjacency_matrix = [[0] * n for _ in range(n)]
    
    # Fill the adjacency matrix based on list1 and list2
    for parent, child in zip(list1, list2):
        i = node_to_index[parent]
        j = node_to_index[child]
        adjacency_matrix[i][j] = 1
    
    return adjacency_matrix, unique_nodes

# Example usage:
list1 = [1, 1, 1, 1, 2, 2, 2, 3]
list2 = [4, 5, 6, 7, 7, 6, 5, 2]

adj_matrix, nodes = create_adjacency_matrix(rulesX, rulesY)

# Print the adjacency matrix
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

# Print the mapping of indices to nodes
print("\nNode mapping:")
for idx, node in enumerate(nodes):
    print(f"{idx}: {node}")


print(nodes.index(36))



