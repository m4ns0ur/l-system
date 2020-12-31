import turtle


def next(s):
    r = ''
    for c in s:
        if c == 'A':
            r += 'ABA'
        elif c == 'B':
            r += 'BBB'
    return r


def draw(s, n):
    for c in s:
        if c == 'A':
            t.fd(n)
        elif c == 'B':
            t.penup()
            t.fd(n)
            t.pendown()


scr = turtle.getscreen()
t = turtle.Turtle()

s = 'A'
for i in range(5):
    s = next(s)

draw(s, 4)
t.ht()
input('Press enter to continue ...')
