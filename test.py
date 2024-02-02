from zipper import Zipper, ZipperError

example = ['+', ['*', 1, 2], ['*', 3, 4]]

z = Zipper(example)


z.down().right().right().down().set('/').topmost()
print(z.get())

def match(l):
    print(f"matching {l}")
    z = Zipper(l)
    try:
        z.down()
        if z.get() != '+':
            return False
        z.right()
        z.down()
        if z.get() != '*':
            return False
        z.up().right().down()
        if z.get() != '*':
            print('expected *')
            return False
    except ZipperError:
        return False
    return True

print(match(example))


while True:
    k = input('> ')
    if k == 'z':
        z.up()
    elif k == 's':
        z.down()
    elif k == 'q':
        z.left()
    elif k == 'd':
        z.right()
    elif k == 'g':
        print(z.get())
    elif k == 'l':
        z.leftmost()
    elif k == 'r':
        z.rightmost()
    print(z)
