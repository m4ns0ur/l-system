import turtle


def next(s):
    r = ''
    for c in s:
        if c == 'A':
            r += 'B-A-B'
        elif c == 'B':
            r += 'A+B+A'
        else:
            r += c
    return r


def draw(s, n, a):
    for c in s:
        if c in 'AB':
            t.fd(n)
        elif c == '+':
            t.lt(a)
        elif c == '-':
            t.rt(a)


scr = turtle.getscreen()
t = turtle.Turtle()

s = 'A'
a = 60
for i in range(6):
    s = next(s)

draw(s, 10, a)
t.ht()
input('Press enter to continue ...')
