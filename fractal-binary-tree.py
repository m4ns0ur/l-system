import turtle


def next(s):
    r = ''
    for c in s:
        if c == '1':
            r += '11'
        elif c == '0':
            r += '1[0]0'
        else:
            r += c
    return r


def draw(s, n):
    for c in s:
        if c == '0':
            t.fd(n)
            t.bk(n)
        elif c == '1':
            t.fd(n)
        elif c == '[':
            stack.append((t.pos(), t.heading()))
            t.lt(45)
        elif c == ']':
            (p, h) = stack.pop()
            t.seth(h)
            t.penup()
            t.setpos(p)
            t.pendown()
            t.rt(45)


scr = turtle.getscreen()
t = turtle.Turtle()
t.lt(90)
stack = []

s = '0'
for i in range(7):
    s = next(s)

draw(s, 4)
t.ht()
input('Press enter to continue ...')
