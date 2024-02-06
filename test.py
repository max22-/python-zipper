from zipper import Zipper, ZipperError

example = {'name': '+', 'body': [{'name':'*', 'body': [1, 2]}, {'name':'*', 'body':[3, 4]}]}

def make_node(n, c):
    n_copy = dict(n)
    n_copy['body'] = c
    return n_copy

z = Zipper(
    lambda n: isinstance(n, dict),
    lambda n: n['body'],
    make_node,
    example)


z.down().right().edit(lambda d: {'name': '/', 'body': d['body']}).up().append_child({'name': '+', 'body': [5, 6]}).top()
print(z.node())

def match(l):
    print(f"matching {l}")
    z = Zipper(
        lambda n: isinstance(n, dict),
        lambda n: n['body'],
        make_node,
        l)
    try:
        if z.node()['name'] != '+':
            return False
        z.down()
        if z.node()['name'] != '*':
            return False
        z.right()
        if z.node()['name'] != '*':
            print(f"expected *, got {z.node()['name']}")
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
        n = z.node()
        if isinstance(n, dict):
            print(n['name'])
        else:
            print(n)
    elif k == 'l':
        z.leftmost()
    elif k == 'r':
        z.rightmost()
    n = z.node()
    print(n)
    if isinstance(n, dict):
        print(n['name'])
    else:
        print(n)
    #print(z)
