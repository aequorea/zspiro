#!/usr/bin/python3
#
# zspiro.py -- primordial eyecandy based on spirograph algorithm
#              inspired by a version I wrote in the 1970s which
#              ran on a PDP-10 and a Tektronix 4010 graphics display
#
#              if you let it run for a while you'll see patterns that
#              don't really look like something that came out of a
#              spirograph
#
# 2015-09-07 -- first release
# 2019-01-15 -- pensize 2, make default window fit 1024x768 display

from turtle import Screen, Turtle
from math import sin, cos, pi
from time import sleep

steps = 360     # level of detail or number of patterns in space

s = Screen()
s.setup(width=900, height=700, startx=0, starty=2) # TEK 4010 = 1024 x 780
l = s.window_height()/4-10
s.bgcolor("black")
s.delay(0)

t = Turtle()
t.hideturtle()
t.pencolor("green")
t.pensize(2)
t.speed(0)

j = 1
while True:
    t.goto(2*l,0)
    t.clear()

    i = 0
    while i <= steps:
        angle = 2*i*pi/steps
        x=cos(angle) + cos(j*angle)
        y=sin(angle) + sin(j*angle)
        t.goto(l*x,l*y)
        i += 1
    sleep(2)
    j += 1

