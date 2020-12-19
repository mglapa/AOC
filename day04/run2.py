
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

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
valid_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

invalid = 0
valid = 0

for p in passports:

    # Check if fields are there
    keys = p.keys()
    fields = 0
    val = True
    for r in required:
        if r not in keys:
            val = False
            break
    if val == False:
        invalid += 1
        continue




    # Check birth year
    if int(p['byr']) < 1920 or int(p['byr']) > 2002:
        invalid += 1
        continue

    # Check issue year
    if int(p['iyr']) < 2010 or int(p['iyr']) > 2020:
        invalid += 1
        continue

    # Check expiration year
    if int(p['eyr']) < 2020 or int(p['eyr']) > 2030:
        invalid += 1
        continue
    
    # Check height
    if 'cm' in p['hgt']:
        if len(p['hgt']) != 5:
            invalid += 1
            continue
        
        n = int(p['hgt'][:3])
        if n < 150 or n > 193:
            invalid += 1
            continue

    elif 'in' in p['hgt']:
        if len(p['hgt']) != 4:
            invalid += 1
            continue
        
        n = int(p['hgt'][:2])
        if n < 59 or n > 76:
            invalid += 1
            continue

    else:
        invalid += 1
        continue

    # Check hair color
    if len(p['hcl']) != 7:
        invalid += 1
        continue

    if p['hcl'][0] != '#':
        invalid += 1
        continue

    for c in p['hcl'][1:]:
        if c not in valid_char:
            val = False
            break
    
    if val == False:    
        invalid += 1
        continue

    # Check eye color
    if p['ecl'] not in eyes:
        invalid += 1
        continue

    # Check passport id
    if len(p['pid']) != 9:
        invalid += 1
        continue
    for c in p['pid']:
        if c not in valid_num:
            val = False
    if val == False:
        invalid += 1
        continue
    
    

print('valid: ', len(passports) - invalid)


