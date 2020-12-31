import turtle


def next(s):
    r = ''
    for c in s:
        if c == 'L':
            r += '-RF+LFL+FR-'
        elif c == 'R':
            r += '+LF-RFR-FL+'
        else:
            r += c
    return r


def draw(s, n, a):
    for c in s:
        if c == 'F':
            t.fd(n)
        elif c == '+':
            t.rt(a)
        elif c == '-':
            t.lt(a)


scr = turtle.getscreen()
t = turtle.Turtle()
a = 90
t.lt(a)

s = 'LFL+F+LFL'
for i in range(4):
    s = next(s)

draw(s, 10, a)
t.ht()
input('Press enter to continue ...')
