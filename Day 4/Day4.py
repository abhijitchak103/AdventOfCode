# Gathering the data

with open("Day 4\Day4.txt") as f:
    data = f.read().split("\n")

# print(data)

# Part 1

count = 0
for entry in data:
    entry_list = [i for i in entry.split(',')]
    
    e1_min, e1_max = entry_list[0].split('-')
    e2_min, e2_max = entry_list[1].split('-')

    e1_min, e1_max, e2_min, e2_max = [int(x) for x in [e1_min, e1_max, e2_min, e2_max]]

    # 4-6, 6-6
    # 2-8, 3-7
    # 14-16, 15-68
    # if elf1_min >= elf2_min and elf1_max <= elf2_min, add 1
    # or 
    # if elf2_min >= elf1_min and elf2_max <= elf1_min, add 1

    if (e1_min <= e2_min and e1_max >= e2_max) or (e1_min >= e2_min and e1_max <= e2_max):
        count += 1

print(f"Answer to Part 1: {count}")

# Part 2


# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, 
# while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

# 5-7,7-9 overlaps in a single section, 7.
# 2-8,3-7 overlaps all of the sections 3 through 7.
# 6-6,4-6 overlaps in a single section, 6.
# 2-6,4-8 overlaps in sections 4, 5, and 6

# Possible cases

# 1. One e1 min or e2 max = one of e2 min or e2 max
# 2. Fully enclosed
# 3. Either (e1 max is between e2 min and e2 max) or (e2 min is between e1 min and e1 max) 

count = 0
for entry in data:
    entry_list = [i for i in entry.split(',')]
    
    e1_min, e1_max = entry_list[0].split('-')
    e2_min, e2_max = entry_list[1].split('-')

    e1_min, e1_max, e2_min, e2_max = [int(x) for x in [e1_min, e1_max, e2_min, e2_max]]

    # Case 1
    if (e1_min in [e2_min, e2_max]) or (e1_max in [e2_min, e2_max]):
        count += 1 
    # Fully Overlap Case: case 2
    elif (e1_min <= e2_min and e1_max >= e2_max) or (e1_min >= e2_min and e1_max <= e2_max):
        count += 1
    # Case 3
    elif (e2_min <= e1_max <= e2_max) or (e1_min <= e2_min <= e1_max) or (e1_min <= e2_max <= e1_max) or (e2_min <= e1_min <= e2_max):
        count += 1

print(f"Answer to Part 2: {count}")