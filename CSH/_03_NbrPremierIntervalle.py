from _02_NbrPremier import isPrime

primeList=[]

def isPrimeInterval(a,b):
    for i in range(a,b+1):
        if (isPrime(i)):
            primeList.append(i)
    return primeList

print(isPrimeInterval(2,9))
          
        
    