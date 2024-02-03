class ZipperError(Exception):
    pass

class Zipper:
    def __init__(self, tree):
        self.focus = tree
        self.path = []

    def up(self):
        if len(self.path) == 0:
            raise ZipperError('Already at the top')
        lr, self.path = self.path[0], self.path[1:]
        self.focus = lr['l'] + [self.focus] + lr['r']
        return self

    def down(self):
        if (not isinstance(self.focus, list)) or len(self.focus) == 0 :
            raise ZipperError('Already at the bottom')
        self.path = [ {'l': [], 'r': self.focus[1:]}] + self.path
        self.focus = self.focus[0]
        return self

    def left(self):
        if len(self.path) == 0:
            raise ZipperError('Left of root')
        if len(self.path[0]['l']) == 0:
            raise ZipperError('Already at leftmost node')
        lr, self.path = self.path[0], self.path[1:]
        new_focus = lr['l'][-1]
        self.path = [{'l': lr['l'][:-1], 'r': [self.focus] + lr['r']}] + self.path
        self.focus = new_focus
        return self
        

    def right(self):
        if len(self.path) == 0:
            raise ZipperError('Right of root')
        if len(self.path[0]['r']) == 0:
            raise ZipperError('Already at rightmost node')
        lr, self.path = self.path[0], self.path[1:]
        new_focus = lr['r'][0]
        self.path = [{'l': lr['l'] + [self.focus], 'r': lr['r'][1:]}] + self.path
        self.focus = new_focus
        return self

    def topmost(self):
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
    
    def set(self, val):
        self.focus = val
        return self
    
    def __repr__(self):
        return f"({self.focus}, {self.path})"
