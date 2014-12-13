#  Wzorowane na przyk³adzie Rona Zacharskiego

from math import sqrt
import numpy as np

# Mamy s³ownik users - zawiera on klucze i wartoœci (keys() i values())

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

#Funkcja obliczaj¹ca estymator wspó³czynnika korelacji

def pearson(rating1,rating2):
    x=rating1.values()
    y=rating2.values()
      
    xsr=sum(x)/len(x)
    ysr=sum(y)/len(y)

    x2=[]
    x3=[]

    y2=[]
    y3=[]
    z=[]

    for i in x:
        x2.append(i-xsr)
        x3.append((i-xsr)**2)

    for i in y:
        y2.append(i-ysr)
        y3.append((i-ysr)**2)

    for i in range(0,len(x)):
        z.append(x2[i]*y2[i])

    z1=sum(z)
    x4=sqrt(sum(x3))
    y4=sqrt(sum(y3))
            
    korelacja=z1/(x4*y4)
    return korelacja

print "Wspó³czynnik korelacji wynosi:"
print pearson(users["Ania"],users["Bonia"])
#Estymator wyniós³ oko³o 0,8 co wskazuje na siln¹ zale¿noœæ (korelacjê)
#gdy¿ jego wartoœæ jest mocno zbli¿ona do 1.

#Funckja manhattan do obliczania odleg³oœci manhattan
def manhattan(rating1, rating2):
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1

print "Odleg³oœæ manhattan od Ani do Boni wynosi:"
print manhattan(users["Ania"],users["Bonia"])

#Wspó³czynnik korelacji obliczony na podstawie biblioteki numpy

def pearsonNumpy(rating1,rating2):
    x=rating1.values()
    y=rating2.values()

    a=array(x)
    b=array(y)
    korelacjaNumpy=np.corrcoef([x,y])[0][1]
    return korelacjaNumpy

print pearsonNumpy(users["Ania"],users["Bonia"])

    
















