
with open('input.txt', 'r') as f:
    lines = f.readlines()

passports = []

tmp = ''
for i in range(len(lines)):
    if lines[i] != '\n':
        tmp += lines[i].rstrip() + ' '
    else:
        tmp = tmp.split(' ')
        tmp_dict = {}
        for t in tmp:
            try:
                key, val = t.split(':')
                tmp_dict[key] = val
            except:
                pass
        passports.append(tmp_dict)
        tmp = ''


for p in passports:
    print(p)

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

invalid = 0
valid = 0

for p in passports:
    keys = p.keys()
    fields = 0
    for r in required:
        if r not in keys:
            print(r, keys)
            invalid += 1
            break
        else:
            fields += 1
    if fields == 7:
        valid += 1


print('total:   ', len(passports))
print('valid:   ', valid)
print('invalid: ', invalid)


