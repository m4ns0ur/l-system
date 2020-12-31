import turtle


def next(s):
    r = ''
    for c in s:
        if c == 'F':
            r += '+F--F+'
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

s = 'F'
a = 45
for i in range(8):
    s = next(s)

draw(s, 10, a)
t.ht()
input('Press enter to continue ...')
