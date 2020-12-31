import turtle


def next(s):
    r = ''
    for c in s:
        if c == 'A':
            r += '+BF-AFA-FB+'
        elif c == 'B':
            r += '-AF+BFB+FA-'
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
a = 90
t.lt(a)

s = 'A'
for i in range(6):
    s = next(s)

draw(s, 10, a)
t.ht()
input('Press enter to continue ...')
