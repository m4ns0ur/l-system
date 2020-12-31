import turtle


def next(s):
    r = ''
    for c in s:
        if c == 'X':
            r += 'XF-F+F-XF+F+XF-F+F-X'
        else:
            r += c
    return r


def draw(s, n, a):
    for c in s:
        if c in 'FG':
            t.fd(n)
        elif c == '+':
            t.lt(a)
        elif c == '-':
            t.rt(a)


scr = turtle.getscreen()
t = turtle.Turtle()
a = 90
t.lt(a)

s = 'F+XF+F+XF'
for i in range(4):
    s = next(s)

draw(s, 10, a)
t.ht()
input('Press enter to continue ...')
