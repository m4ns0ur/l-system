import turtle


def next(s):
    r = ''
    for c in s:
        if c == 'F':
            r += 'F+F--F+F'
        else:
            r += c
    return r


def draw(s, n, a):
    for c in s:
        if c == 'F':
            t.fd(n)
        elif c == '+':
            t.lt(a)
        elif c == '-':
            t.rt(a)


scr = turtle.getscreen()
t = turtle.Turtle()

s = 'F--F--F'
a = 60
for i in range(4):
    s = next(s)

draw(s, 10, a)
t.ht()
input('Press enter to continue ...')
