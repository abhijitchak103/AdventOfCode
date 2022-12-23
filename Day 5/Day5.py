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

stack_f = list()
for row in stack:
    row = row[::-1]
    stack_f.append(row)

# print(stack)

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

    for i in range(int(move[0])):
        src = int(move[1])
        trg = int(move[2])
        crate = stack_f[src-1].pop(-1)
        stack_f[trg-1].append(crate)
        
for row in stack_f:
    print(row[-1], end = '')








