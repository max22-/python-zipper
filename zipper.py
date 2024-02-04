class ZipperError(Exception):
    pass

class Zipper:
    def __init__(self, tree):
        self.focus = tree
        self.path = []

    def up(self):
        if len(self.path) == 0:
            raise ZipperError('Already at the top')
        crumb, self.path = self.path[0], self.path[1:]
        self.focus = {'name': crumb['name'], 'body': crumb['l'] + [self.focus] + crumb['r']}
        return self

    def down(self):
        if (not isinstance(self.focus, dict)) or len(self.focus) == 0 :
            raise ZipperError('Already at the bottom')
        self.path = [{'name': self.focus['name'], 'l': [], 'r': self.focus['body'][1:]}] + self.path
        self.focus = self.focus['body'][0]
        return self

    def left(self):
        if len(self.path) == 0:
            raise ZipperError('Left of root')
        if len(self.path[0]['l']) == 0:
            raise ZipperError('Already at leftmost node')
        l = self.path[0]['l']
        r = self.path[0]['r']
        r = [self.focus] + r
        self.focus = l.pop()
        self.path[0]['l'] = l
        self.path[0]['r'] = r
        return self
        

    def right(self):
        if len(self.path) == 0:
            raise ZipperError('Right of root')
        if len(self.path[0]['r']) == 0:
            raise ZipperError('Already at rightmost node')
        l = self.path[0]['l']
        r = self.path[0]['r']
        l.append(self.focus)
        self.focus = r[0]
        r = r[1:]
        self.path[0]['l'] = l
        self.path[0]['r'] = r
        return self

    def top(self):
        while len(self.path) > 0:
            self.up()

    def leftmost(self):
        if len(self.path) > 0:
            while len(self.path[0]['l']) > 0:
                self.left()

    def rightmost(self):
        if len(self.path) > 0:
            while len(self.path[0]['r']) > 0:
                self.right()

    def get(self):
        return self.focus
    
    def edit(self, f):
        self.focus = f(self.focus)
        return self
    
    def __repr__(self):
        return f"({self.focus}, {self.path})"
