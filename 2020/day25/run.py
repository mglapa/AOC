
def parse():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    door_pub = int(lines[0])
    key_pub = int(lines[1])
    return door_pub, key_pub

def transform(inp, subj):
    return (inp * subj) % 20201227

def transform_n(subj, N):
    inp = 1
    for i in range(N):
        inp = transform(inp, subj)
    return inp

def part1(door_pub, key_pub):
    
    print(door_pub, key_pub)
    
    # find loop number for door and key
    door_n = -1
    key_n = -1
    loopn = 1
    n = 1
    while (door_n == -1) or (key_n == -1):
        n = transform(n, 7)

        #if loopn % 100 == 0:
        #    print('{}  {}'.format(loopn, n))
        
        if n == door_pub:
            door_n = loopn
            print('door_pub loop num = {}'.format(loopn))
        if n == key_pub:
            key_n = loopn
            print('key_pub loop num = {}'.format(loopn))
        
        loopn += 1

    # Get encryption key
    key1 = transform_n(key_pub, door_n)
    key2 = transform_n(door_pub, key_n)

    print('Part 1: ', key1, key2)















door_pub, key_pub = parse()
part1(door_pub, key_pub)

















