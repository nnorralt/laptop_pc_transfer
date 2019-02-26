import matplotlib.pyplot as plt
import pandas as pd #impordin pandas andmetöötluslibrary
from easygui import * #toon easygui sisse, et ei peaks konsooli jälgima

#kas sa tahad näha demograafilisi muutusi kogusummas või vanuste lõikes?
def eestimees(andmed):
    valik = ["Vanusegrupid, palun" , "Koguarv, palun"]
    msgbox("Tere. Tutvustan teile graafiliselt meessoost täisealiste Eestlaste arvu muutumist Ida-Viru maakonnas aastatel 1990-2017.")
    valik = choicebox(" Kas soovite näha graafikut koguarvu või vanusegruppide lõikes?:", choices = valik)
    f = open(andmed, encoding="UTF-8") #avame faili
    eestijrj = []
    labels = []
    vanustesummad = []
    for rida in f: #
        osa = rida.split(";")
        eestijrj.append(osa)
    for rida in range(len(eestijrj)): #loeme faili sisse
        for el in range(len(eestijrj[rida])):
            eestijrj[rida][el] = eestijrj[rida][el].strip() #puhastame whitespacest
            eestijrj[rida][el] = eestijrj[rida][el].strip('"') #puhastame liigsetest jutumärkidest
    for rida in range(len(eestijrj)):
            eestijrj[rida].pop(0) #eemaldame ebavajaliku esimese elemendi
            eestijrj[rida].pop(0) #eemaldame ebavajaliku teise elemendi. nüüd 1. element on aastaarv
            labels.append(eestijrj[rida].pop(0))
            for el in range(len(eestijrj[rida])):
                eestijrj[rida][el] = int(eestijrj[rida][el])
            vanustesummad.append(sum(eestijrj[rida]))
    print("-----")
    print(vanustesummad)
    print("-----")
    #print(labels)
    labels = tuple(labels)
    print(eestijrj)
    f.close() #sulgeme
    eestifail = pd.DataFrame(eestijrj, index = labels)
    #eestifail.set_index(0)
    eestifail = eestifail.astype(float)
    print(eestifail)
    koguarv = pd.DataFrame(vanustesummad, index = labels)
    koguarv = koguarv.astype(float)
    
    
    #eestifail = pd.read_csv(eestijrj, delimiter=',',index_col=1 )   
    #eestifail = pd.DataFrame(eestifail) #muudame need andmed dataFrameks, et töödelda paremini Pandase käsklustega
    #eestifail.pop('Ida-Viru maakond')
    #print(eestifail.shape)
    #print(eestifail) #printisime lihtsalt et kontrollida andmeid
    #eestifail.plot()
    #koguarv.plot()
    plt.plot(eestifail[0], label='20-24.aastased')
    plt.plot(eestifail[1], label='25-29.aastased')
    plt.plot(eestifail[2], label='30-34.aastased')
    plt.plot(eestifail[3], label='35-39.aastased')
    plt.plot(eestifail[4], label='40-44.aastased')
    plt.plot(eestifail[5], label='45-49.aastased')
    plt.plot(eestifail[6], label='50-54.aastased')
    plt.plot(eestifail[7], label='55-59.aastased')
    plt.plot(eestifail[8], label='60-64.aastased')

                    
    plt.legend(loc='upper left')
    plt.xlabel('Aasta')
    plt.ylabel('Tööealiste eesti meeste arv')
    plt.show() 
    
eestimees('eestlased.csv')