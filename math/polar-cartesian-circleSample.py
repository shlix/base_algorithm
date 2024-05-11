# http://note.youdao.com/s/JQThVzgs

import math,random
import numpy as np

def polar_coordinate(N = 1000, R = 1):
    x,y = [], []
    for i in range(N):
        r = random.random()
        theta = 2*np.pi*random.random()
        x.append(R*math.cos(theta)*(r)**0.5)
        y.append(R*math.sin(theta)*(r)**0.5)
    return x,y

def cartesian_coordinate(N = 1000, R = 1):
    x,y = [], []
    while(N > 0):
        s = random.random()
        t = random.random()
        # 此处0.5->2结果不变，因为x^2与x^0.5为反函数
        if math.pow(s*s + t*t, 0.5) <= 1:
            x.append(R*s)
            y.append(R*t)
            N -= 1
    return x,y

def calculate_expectation():
    xp, yp = polar_coordinate(100000, 10)
    xp, yp = np.array(xp), np.array(yp)
    p = np.power(xp*xp+yp*yp, 0.5)
    xc, yc = cartesian_coordinate(100000, 10)
    xc, yc = np.array(xc), np.array(yc)
    c = np.power(xc*xc+yc*yc, 0.5)
    print(np.mean(p),np.mean(c))

calculate_expectation()