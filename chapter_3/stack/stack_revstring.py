from stack import Stack


def revstring(_string):
    s = Stack()
    alist = [i for i in _string]
    for i in alist[::-1]:
        s.push(i)
        print(s.peek())

def revstring2(_string):
    s2 = Stack()
    for i in _string:
        s2.push(i)
    revstr = ''
    while not s2.isEmpty():
        revstr = revstr + s2.pop()
    print(revstr)


revstring('python')
revstring2('apple')
