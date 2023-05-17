import pickle

def duomenu_kurimas():
    duomenys=[]
    kiek=int(input('Kiek duomenų vesite? '))
    for i in range(kiek):

        vardas=input('Įveskite vardą: ')
        amzius=int(input('Įveskite amžių: '))
        pareigos=input(('Įveskite pareigas: '))
        tuplas=(vardas,amzius,pareigos)
        duomenys.append(tuplas)
    return duomenys

def saugojimas(duomenys):
    with open('duomen.pkl','wb') as failas:
      return  pickle.dump(duomenys,failas)

def nuskaitymas():
    with open('duomen.pkl', 'rb') as failas:
        print(pickle.load(failas))

duomenys=duomenu_kurimas()
saugojimas(duomenys)
nuskaitymas()