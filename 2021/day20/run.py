
import numpy as np

#fn = 'sample.txt'
fn = 'input.txt'

def load():
    with open(fn, 'r') as f:
        lines = f.read()

    lines = lines.split('\n\n')

    # Parse code
    code = lines[0]
    code = code.replace('.', '0')
    code = code.replace('#', '1')
    code = np.array(list(code), np.int)

    # Parse img
    img = lines[1]
    img = img.replace('.', '0')
    img = img.replace('#', '1')
    img = img.split('\n')[:-1]
    
    for i in range(len(img)):
        img[i] = list(img[i])

    img = np.array(img)

    return img, code

def conv(img, code):
    h, w = img.shape
    out = np.zeros_like(img, int).astype(str)

    
    for y in range(1, h-1):
        for x in range(1, w-1):
            bits = ''
            for ky in range(-1, 2):
                for kx in range(-1, 2):
                    bits += str(img[y+ky, x+kx])
            bits = int(bits, 2)
            val = code[bits]
            out[y, x] = val

    return out


def part1():
    img, code = load()

    pad = 4

    img = np.pad(img, pad)

    img = conv(img, code)
    img = conv(img, code)

    p = pad//2
    img = img[p:-p, p:-p]


    total = img.astype(int).sum()

    print(total)






def part2():
    img, code = load()

    pad = 100

    img = np.pad(img, pad)

    for i in range(50):
        img = conv(img, code)

    p = pad//2
    img = img[p:-p, p:-p]


    total = img.astype(int).sum()

    print(total)



def main():
    
    part1()

    part2()


if __name__ == '__main__':
    main()    























