# Gathering the data

with open("day1.txt") as f:
    calorie = [i for i in f.read().strip().split("\n")]

# print(calorie)
# elfs = list()

most = 0
most2 = 0
most3 = 0
count = 0

elves = list()

for data in calorie:
    if data == "":
        count = 0
    else:
        count += int(data)
    
    if count > most:
        most = count
    elif count > most2:
        most2 = count
    elif count > most3:
        most3 = count

    elves.append(count)
    elves.sort(reverse=True)

print(f"Day 1 result: {most}")
# # print(f"Day 2 result: {most}, {most2}, {most3}")
# # print(elves[0]+elves[1]+elves[2])
# print(elves)

print(sum(elves[:3]))