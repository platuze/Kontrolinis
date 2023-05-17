def tuplas(*args):
    sar1=[]
    for elementas in args:
        sum=0
        kiekis=0
        for skaicius in elementas[1]:       # ieškomas tuple antras(iš dviejų)elementas ir tikrinama, ar jis skaičius
            if type(skaicius)==int:
                sum+=skaicius
                kiekis+=1
        vid=f'{(sum/kiekis):1.2f}'            # du skaičiai po kablelio
        pakeista_tuple=(elementas[0],vid)       # nauja tuple, kur nulinis elementas string, pirmas - vidurkis
        sar1.append(pakeista_tuple)
    return sar1

sarasas=[('jonas',[12,7,9]),('petras',[7,96]), ('kriaušė',[4,6,9,7]),('namas',[14,8,-9])]

print(tuplas(*sarasas))