from functools import cache

with open('day11.txt', 'r') as f:
    file = f.read().split()

stones = list(map(int, file))

@cache
def countStones(val, blinks):
    if blinks == 0:
        return 1

    if val == 0:
        return countStones(1, blinks -1)

    num_str = str(val)
    if len(num_str) % 2 == 0:

        mid = len(num_str) // 2
        part1 = num_str[:mid]
        part2 = num_str[mid:] 
        
        return countStones(int(part1), blinks -1) + countStones(int(part2), blinks -1)

    else:
        return countStones(val*2024, blinks -1)

part1 = sum(countStones(stone, 25) for stone in stones)
part2 = sum(countStones(stone, 75) for stone in stones)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

# blinks = 25
# count = 0

# def split_number(num):
#     num_str = str(num)
#     mid = len(num_str) // 2
#     part1 = num_str[:mid]
#     part2 = num_str[mid:]
    
#     part1 = int(part1) if int(part1) != 0 else 0
#     part2 = int(part2) if int(part2) != 0 else 0
    
#     result = [part1, part2]
#     return result

# while count < blinks:
#     print(split_cache)
#     new = []
#     for i in lst:
#         if i == 0:
#             result = [1]
#         elif len(str(i)) % 2 == 0:
#             result = split_number(i)
#         else:
#             result = [i * 2024]
#         new.extend(result)
#     lst = new
#     count += 1

# print(len(lst))
