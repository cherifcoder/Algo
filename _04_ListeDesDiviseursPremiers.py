from _01_ListeDesDiviseurs import listeDiviseurs
from _03_NbrPremierIntervalle import isPrimeInterval
from _02_NbrPremier import isPrime




def isPrimeDivider(n):
    maliste = []
    tableau = listeDiviseurs(n)
    for i in tableau:
        if isPrime(i):
            maliste.append(i)
    return (maliste)

if __name__=="__main__":
    print(isPrimeDivider(56320))