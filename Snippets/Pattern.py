n=int(input("enter:"))
def StTri(n):
    for i in range(1,n+1):
        print(" "*(n+1-i)+"* "*(i))
def RevTri(n):
    for i in range(1,n+1):
        print(" "*(i-1)+" *"*(n+1-i))
StTri(n)        
RevTri(n)
