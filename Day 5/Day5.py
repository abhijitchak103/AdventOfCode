# Gathering the data

with open("Day 5_crates.txt") as f:
    lines = f.read().split("\n")

lines.remove(lines[-1])
lines.remove(lines[-1])

# Creating the list of list for the stack of crates
stack = list()

for i in range(1, len(lines[0]), 4):
    new = list()
    for row in lines:
        if row[i] not in ['[', ']', ' ']:
            new.append(row[i])

    stack.append(new)

# Gathering the moves and storing in a list

with open("Day 5_moves.txt") as f:
    data = f.read().split("\n") 

moves = list()
for line in data:
    line = line.split(" ")
    moves.append(line)

# Keeping the numbers in the moves list

for move in moves:
    del move[0]
    del move[1]
    del move[2]

    # for i in range(int(move[0])):
    num = int(move[0])
    src = int(move[1])
    trg = int(move[2])

    
    crate = stack[src-1][:num][::-1]
    del stack[src-1][:num]
    
    # Moving the crates in the same order as they were
    for ele in crate:
        stack[trg-1].insert(0, ele)

for row in stack:
    print(row[0], end = '')
