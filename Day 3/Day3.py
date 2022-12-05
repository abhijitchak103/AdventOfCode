# Gathering the data

with open("Day3.txt") as f:
    data = f.read().split("\n")

# print(data)

weights = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
           'k': 11, 'l': 12,'m': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 
           'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
           'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
           'K': 37, 'L': 38,'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 
           'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

score = 0

# Part 1
# for element in data:
#     n = len(element)
#     first = element[:n//2]
#     last = element[n//2:]

#     for char in first:
#         if char in last:
#             score += weights[char]
#             break

# print(f"First part score: {score}")

# Part 2
x = len(data)

# print(data[1])
# print(data[2])
score = 0
i = 0
while i < x:
    group1 = {j for j in data[i]}
    group2 = {j for j in data[i+1]}
    group3 = {j for j in data[i+2]}
    i += 3
    common = group1.intersection(group2).intersection(group3)
    common = list(common)[0]
    # print(f"{i=} and common character is {common}")
    score += weights[common]

print(f"Second part score: {score}")