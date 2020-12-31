import turtle


def next(s):
    r = ''
    for c in s:
        if c == 'F':
            r += 'F-G+F+G-F'
        elif c == 'G':
            r += 'GG'
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

a = 120
s = 'F-G-G'
for i in range(6):
    s = next(s)

draw(s, 10, a)
t.ht()
input('Press enter to continue ...')
