with open('Randoms/input.txt') as f:
    commands = f.read().split('\n')

path = '/home'
dirs = {'/home':0}

for command in commands:
    if command[0] == '$':
        if command[2:4] == 'ls':
            pass
        elif command[2:4] == 'cd':
            if command[5:] == '/':
                path = '/home'
            elif command[5:] == '..':
                path = path[:path.rfind('/')]
            else: 
                path = path + '/' + command[5:]
                dirs[path] = 0
    elif command[:3] == 'dir':
        pass
    else:
        size = int(command[:command.find(' ')])
        # dirs[path] += size

        dir = path
        for i in range(path.count('/')):
            dirs[dir] += size
            dir = dir[:dir.rfind('/')]

# print(dirs)
total = 0

for key, value in dirs.items():
    if value <= 100000:
        total += value

print(total)




        


