file = open("day7.txt", "r")
contents = file.read()
file.close()

# Split based on \n
contents = contents.split("\n")

result = []
numbers = []

# Split into results and numbers
for i in contents:
    x = i.split(":")
    result.append(int(x[0]))
    numbers.append(x[1])

count = 0
operators = ['+', '*','|']

def generate_combinations(operators, num_gaps):
    combinations = [[]]
    for _ in range(num_gaps):
        # Expand each combination with all possible operators
        new_combinations = []
        for combination in combinations:
            for operator in operators:
                new_combinations.append(combination + [operator])
        combinations = new_combinations
    return combinations

def eval_left_to_right(expression):
    # Initialize variables
    tokens = []
    num = ""
    
    # Split the expression into numbers and operators
    for char in expression:
        if char in "0123456789":  # If the character is a digit, add it to the number
            num += char
        else:  # If the character is an operator, save the current number and the operator
            if num:
                tokens.append(num)
                num = ""
            tokens.append(char)
    
    if num:  # Append the last number if there's any
        tokens.append(num)
    
    # Start evaluating the expression from left to right
    result = int(tokens[0])
    index = 1
    
    while index < len(tokens):
        operator = tokens[index]
        next_num = int(tokens[index + 1])
        
        if operator == "+":
            result += next_num
        elif operator == "*":
            result *= next_num
        elif operator == "|":
            result = int(str(result)+str(next_num))
        
        index += 2  # Move to the next operator and number
    
    return result

for index,i in enumerate(numbers):
    # Turn i into a list of int.
    lst = i.split(" ")
    lst = [ele for ele in lst if ele.strip()]
    lst = list(map(int,lst))
    num_gaps = len(lst)-1

    # Generate the operator combinations for said list
    operator_combinations = generate_combinations(operators, num_gaps)    

    for combo in operator_combinations:

        # Add the first element of the lst as a string
        expression = str(lst[0])
        for i in range(num_gaps):
            # Add the operator plus the next element of the lst to the string
            expression += combo[i] + str(lst[i+1]) 

        # Calculate the output
        output = eval_left_to_right(expression)

        # If the output matches the original output then add said output to the count
        if output == result[index]:
            count += result[index]
            break
    
print(count)


# k^(n-1) where k the amount of operators and n the amount of numbers. For + and * it would be 2^(n-1).