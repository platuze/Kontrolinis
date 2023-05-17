import random
import pickle
from functools import reduce
from statistics import mean
with open('skaiciai.pkl','wb') as failas:
    kiekis=random.randint(5,10)
    for i in range(kiekis):
        skaicius=random.randint(-5,5)
        print(skaicius)
        pickle.dump(skaicius,failas)
sar=[]
with open('skaiciai.pkl','rb') as failas:
    while True:
        try:
            skaic=pickle.load(failas)
            sar.append(skaic)
        except EOFError:
            break

suma_skaiciai=reduce(lambda x,y: (x[0]+y,x[1]+1),sar,(0,0))
vidurkis=suma_skaiciai[0]/suma_skaiciai[1]
print('Vidurkis: ',vidurkis)
print('Vidurkis su mean funkcija: ',mean(sar))

