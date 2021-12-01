
with open('input.txt', 'r') as f:
    lines = f.readlines()


tot = 0
for line in lines:
    n = int(line)//3 -2
    print(n)

    m = n
    while True:
        m = m//3 - 2
        if m <= 0:
            break
        n += m
    print(n)

    tot += n

print('total: ', tot)

'''
new = tot
while True:
    new = new//3 - 2
    print(new)
    if new <= 0:
        break
    tot += new
print(tot)
'''
