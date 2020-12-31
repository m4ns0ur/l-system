import turtle


def next(s):
    r = ''
    for c in s:
        if c == 'F':
            r += 'F+F-F-F+F'
        else:
            r += c
    return r


def draw(s, n):
    for c in s:
        if c == 'F':
            t.fd(n)
        elif c == '+':
            t.lt(90)
        elif c == '-':
            t.rt(90)


scr = turtle.getscreen()
t = turtle.Turtle()

s = 'F'
for i in range(4):
    s = next(s)

draw(s, 10)
t.ht()
input('Press enter to continue ...')
