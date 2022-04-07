#recursion to print from 1 to n
def sa(x,n):
    if n<x:
        return
    print(x)
    sa(x+1,n)

n=int(input())
sa(1,n)



#recursion to print from n to 1

def sa(x):
    if x==0:
        return
    print(x)
    sa(x-1)

n=int(input())
sa(n)
