

class thing(object):

    def __init__(self, x=None):
        self.x = x


y = thing(x='huh')

def wut(x):
    x.x = 'wut'


wut(y)

print(y.x)
