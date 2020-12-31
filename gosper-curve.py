import turtle


def next(s):
    r = ''
    for c in s:
        if c == 'A':
            r += 'A-B--B+A++AA+B-'
        elif c == 'B':
            r += '+A-BB--B-A++A+B'
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
a = 60
t.lt(a)

s = 'A'
for i in range(4):
    s = next(s)

draw(s, 10, a)
t.ht()
input('Press enter to continue ...')
