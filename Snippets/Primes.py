n=int(input(">>> Enter Number: "))

def CheckPrime(n):
    if n==0 or n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
            break
    else:
        return True       
print(CheckPrime(n))

def GenPrimes(n):
    Primes=[]
    for i in range(n):
        if CheckPrime(i):
            Primes.append(i)
    return Primes
print(f"All Primes till {n} are:")
for i in GenPrimes(n):
    print(i,end=",")
print()

def FirstNPrimes(n):
    Pr=2
    Primes=[]
    while True:
        if CheckPrime(Pr):
            Primes.append(Pr)
            if len(Primes)>=n:
                break
        Pr+=1
    return Primes

print(f"First {n} Prime Numbers are:")
for i in FirstNPrimes(n):
    print(i,end=",")
print()
