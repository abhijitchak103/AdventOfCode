# Gathering the data

with open("Day2.txt") as f:
    data = f.read().split("\n")

# print(data)

# elf = [i[0] for i in data]
# user = [i[-1] for i in data]

# print(elf)
# print(user)
score = 0
for item in data:
    if item[-1] == 'X':
        score += 1
        if item[0] == 'A':
            score += 3
        elif item[0] == 'B':
            score += 0
        elif item[0] == 'C':
            score += 6
    elif item[-1] == 'Y':
        score += 2
        if item[0] == 'A':
            score += 6
        elif item[0] == 'B':
            score += 3
        elif item[0] == 'C':
            score += 0
    elif item[-1] == 'Z':
        score += 3
        if item[0] == 'A':
            score += 0
        elif item[0] == 'B':
            score += 6
        elif item[0] == 'C':
            score += 3

print(f"Score for Part 1: {score}")

# A: Rock, B: Paper, C: Scissor
# X: Lose, Y: Draw, Z: Win
score = 0
for item in data:
    if item[0] == 'A':      # Elf Chose Rock  
        if item[-1] == 'X':
        # Need to Lose, this means score will be +0
            score += 0
        # Since elf chose Rock, I need to choose Scissor
            score += 3
        elif item[-1] == 'Y':
        # Need to Draw, this means score will be +3
            score += 3
        # Since elf chose Rock, I need to choose Rock
            score += 1
        elif item[-1] == 'Z':
         # Need to Win, this means score will be +6
            score += 6
        # Since elf chose Rock, I need to choose Paper
            score += 2
    elif item[0] == 'B':      # Elf Chose Paper  
        if item[-1] == 'X':
        # Need to Lose, this means score will be +0
            score += 0
        # Since elf chose Paper, I need to choose Rock
            score += 1
        elif item[-1] == 'Y':
        # Need to Draw, this means score will be +3
            score += 3
        # Since elf chose Paper, I need to choose Paper
            score += 2
        elif item[-1] == 'Z':
         # Need to Win, this means score will be +6
            score += 6
        # Since elf chose Paper, I need to choose Scissor
            score += 3
    elif item[0] == 'C':      # Elf Chose Scissor  
        if item[-1] == 'X':
        # Need to Lose, this means score will be +0
            score += 0
        # Since elf chose Scissor, I need to choose Paper
            score += 2
        elif item[-1] == 'Y':
        # Need to Draw, this means score will be +3
            score += 3
        # Since elf chose Scissor, I need to choose Scissor
            score += 3
        elif item[-1] == 'Z':
         # Need to Win, this means score will be +6
            score += 6
        # Since elf chose Scissor, I need to choose Rock
            score += 1

print(f"Score for Part 2: {score}")
