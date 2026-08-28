import time
def listeDiviseurs(n):
    diviseurs = []
    for i in range (1, n+1):
        if(n%i==0):
            diviseurs.append(i)
    return diviseurs

startTime= time.time()

print(listeDiviseurs(100))
endTime= time.time()
executionTime = endTime - startTime
print(f"Temps d execution : {executionTime}")