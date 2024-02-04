from zipper import Zipper, ZipperError

example = {'name': '+', 'body': [{'name':'*', 'body': [1, 2]}, {'name':'*', 'body':[3, 4]}]}

z = Zipper(example)


z.down().right().edit(lambda d: {'name': '/', 'body': d['body']}).top()
print(z.get())

def match(l):
    print(f"matching {l}")
    z = Zipper(l)
    try:
        if z.get()['name'] != '+':
            return False
        z.down()
        if z.get()['name'] != '*':
            return False
        z.right()
        if z.get()['name'] != '*':
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
        n = z.get()
        if isinstance(n, dict):
            print(n['name'])
        else:
            print(n)
    elif k == 'l':
        z.leftmost()
    elif k == 'r':
        z.rightmost()
    n = z.get()
    print(n)
    if isinstance(n, dict):
        print(n['name'])
    else:
        print(n)
    #print(z)
