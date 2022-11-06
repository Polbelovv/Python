
def prosto():
    n = int(input())
    b=[]
    i = 2
    while n > 1:
        while n % i == 0:
            b.append(i)
            n //= i
        i += 1
    print(b)
        


prosto()
