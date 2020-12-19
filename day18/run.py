
def parse():
    with open('input_ex.txt', 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip().replace(' ', '')
            print(lines[i])

    return lines

def eval(line):
    eq = []
    val = ''

    for x in line:
        if x.isnumeric():
            print(x)
            val += x
    



def part1(lines):
    for line in lines:
        eval(line)






lines = parse()

part1(lines)




