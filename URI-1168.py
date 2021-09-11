# -*- coding: utf-8 -*-
n = int(input())

leds = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6, 0:6}

for i in range(n):
    tLeds = 0
    led = input()
    for i in range(len(led)):
        tLeds+= leds[int(led[i])]
    print(tLeds, "leds")