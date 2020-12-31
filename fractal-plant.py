import turtle


def next(s):
    r = ''
    for c in s:
        if c == 'X':
            r += 'F+[[X]-X]-F[-FX]+X'
        elif c == 'F':
            r += 'FF'
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
        elif c == '[':
            stack.append((t.pos(), t.heading()))
        elif c == ']':
            (p, h) = stack.pop()
            t.seth(h)
            t.penup()
            t.setpos(p)
            t.pendown()


scr = turtle.getscreen()
t = turtle.Turtle()
t.lt(65)
stack = []

s = 'X'
a = 25
for i in range(6):
    s = next(s)

draw(s, 4, a)
t.ht()
input('Press enter to continue ...')
