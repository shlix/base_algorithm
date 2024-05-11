import math

def computeN(n):
    res = 1
    dis = 0
    for i in range(1,n+1):
        res *= i
    st = str(res)
    print(len(st))
    for i in range(1,len(st)):
        if st[len(st)-i] != '0':
            break
        dis = i
    return dis, res
def predictN(n):
    e = math.floor(math.log(n, 5))
    res = 0
    for i in range(1,e+1):
        res += n//int((math.pow(5, i)))
    return res
n = 1000
print(computeN(n))
print(predictN(n))