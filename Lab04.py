#  Wzorowane na przyk³adzie Rona Zacharskiego

from math import sqrt
import numpy as np


users = {
        "Ania": 
            {"Blues Traveler": 1.8,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": 2.5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

#Funkcja obliczajaca wspolczynnik korelacji (z zastosowaniem wzoru przyblizajacego)

def pearson(rating1, rating2):
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    nn=users["Ania"].values()
    udaloSiePorownac = False
    

    a=[]
    b=[]
    c=[]
    d=[]
    e=[]

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            a.append(rating1[klucz]*rating2[klucz])
            b.append(rating1[klucz])
            c.append(rating2[klucz])
            d.append(rating1[klucz]**2)
            e.append(rating2[klucz]**2)
        n=len(nn)

        l1=sum(a)
        l2=(sum(b)*sum(c))/n
             
        m1=sqrt(sum(d)-((sum(b)**2)/n))
        m2=sqrt(sum(e)-((sum(c)**2)/n))
               
        
    korelacja=(l1-l2)/(m1*m2)   

    return korelacja


print "Wspó³czynnik korelacji (obliczony na podstawie wzoru przybli¿aj¹cego) wynosi: "
print pearson(users["Ania"],users["Bonia"])



#Korelacja - biblioteka numpy

def pearsonNumpy(rating1,rating2):
    klucze10 = rating1.keys()
    klucze20 = rating2.keys()
    udaloSiePorownac = False

        for klucz in klucze10:
            if klucz in rating20.keys():
                korelacjaNumpy=np.corrcoef([klucze10,klucze20])[0][1]
                
    return korelacjaNumpy

print "Wspó³czynnik korelacji (obliczony za pomoc¹ biblioteki Numpy) wynosi: "
print pearsonNumpy(users["Ania"],users["Bonia"])

    
















