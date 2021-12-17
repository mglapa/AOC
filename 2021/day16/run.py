
#fn = 'sample.txt'
fn = 'input.txt'

def load():
    with open(fn, 'r') as f:
        lines = f.readlines()

    line = lines[0].rstrip()

    binary = ''

    for c in line:
        c = int(c, 16)
        c = format(c, 'b').zfill(4)
        binary += c

    return binary

def parse_packet(bits, i):

    packet = {}
    
    i_start = i

    packet['version'] = int(bits[i:i+3], 2)
    packet['type_id'] = int(bits[i+3:i+6], 2)

    #print('Version: {}  |  Type_ID: {}'.format(packet['version'], packet['type_id']))

    # Literal value
    if packet['type_id'] == 4:
        i = i+6
        val = ''
        while True:
            chunk = bits[i:i+5]
            i += 5
            val += chunk[1:]
            if chunk[0] == '0':
                break
        
        packet['value']  = int(val, 2)


    else:
        packet['subpackets'] = []

        length_type_id = bits[i+6]
        if length_type_id == '0':
            length = bits[i+7:i+22]
            length = int(length, 2)

            i += 22

            read_len = 0
            while True:
                subp, size = parse_packet(bits, i)
                i += size
                read_len += size

                packet['subpackets'].append(subp)

                if read_len == length:
                    break

        else:
            num = bits[i+7:i+18]
            i += 18
            num = int(num, 2)
            for j in range(num):
                subp, size = parse_packet(bits, i)
                i += size
                packet['subpackets'].append(subp)

    return packet, (i - i_start)

def add_versions(packets):
    total = 0
    for p in packets:
        total += p['version']
        if 'subpackets' in p.keys():
            total += add_versions(p['subpackets'])
    return total

def evaluate(packet):
    if packet['type_id'] == '4':
        return

    if 'subpackets' in packet.keys():
        for p in packet['subpackets']:
            evaluate(p)
        
        if packet['type_id'] == 0:
            packet['value'] = 0
            for sub in packet['subpackets']:
                packet['value'] += sub['value']

        if packet['type_id'] == 1:
            packet['value'] = 1
            for sub in packet['subpackets']:
                packet['value'] *= sub['value']
           
        if packet['type_id'] == 2:
            packet['value'] = 1e10
            for sub in packet['subpackets']:
                packet['value'] = min(sub['value'], packet['value'])
            
        if packet['type_id'] == 3:
            packet['value'] = -1e10
            for sub in packet['subpackets']:
                packet['value'] = max(sub['value'], packet['value'])
        
        if packet['type_id'] == 5:
            sub1, sub2 = packet['subpackets']
            packet['value'] = 1 if sub1['value'] > sub2['value'] else 0
        if packet['type_id'] == 6:
            sub1, sub2 = packet['subpackets']
            packet['value'] = 1 if sub1['value'] < sub2['value'] else 0

        if packet['type_id'] == 7:
            sub1, sub2 = packet['subpackets']
            packet['value'] = 1 if sub1['value'] == sub2['value'] else 0

def part1():
    bits = load()

    packets = []

    i = 0

    while True:
        packet, size = parse_packet(bits, i)
        packets.append(packet)
        i += size

        remaining = len(bits) - i
        if remaining < 6:
            break
    
    total = add_versions(packets)
    print('Part 1: ', total)





def part2():
    bits = load()

    packets = []

    i = 0

    while True:
        packet, size = parse_packet(bits, i)
        packets.append(packet)
        i += size

        remaining = len(bits) - i
        if remaining < 6:
            break
    
    evaluate(packets[0])

    print('Part 2: ', packets[0]['value'])



def main():
    
    part1()

    part2()


if __name__ == '__main__':
    main()    























