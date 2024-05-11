
def returnFactorial(N):
    if N == 1:
        return "1"
    else:
        return "*".join([str(N),returnFactorial(N-1)])

print(returnFactorial(4))

def printFactorial(N):
    if N == 1:
        print("1")
    else:
        printFactorial(N-1)
        print("*".join([str(N),]))

printFactorial(5)


