def vardai(listas):
    raides=[]
    for i in listas:
        raides.append(i[0])
    return  raides
sarasas=['Jonas','Petras','Antanas']

print('Vardų sąrašas: ',sarasas)
print('Pirmosios vardų raidės: ',vardai(sarasas))