import matplotlib.pyplot as plt
import pandas as pd #impordin pandas andmetöötluslibrary
from easygui import * #toon easygui sisse, et ei peaks konsooli jälgima

#kas sa tahad näha demograafilisi muutusi kogusummas või vanuste lõikes?
def eestimees(andmed): #def et lisada hiljem sisse teise valiklause funktsioone
    valik = ["Vanusegrupid, palun", "Koguarv, palun","Mõlemad korraga, palun"] #määran ära easyGUI kastid ning valikud
    msgbox("Tere. Tutvustan teile graafiliselt meessoost täisealiste Eestlaste arvu muutumist Ida-Viru maakonnas aastatel 1990-2017.\n(andmed Statistikaametist)")
    graafiku_valik = choicebox(" Kas soovite näha graafikus koguarvu muutumist, vanusegruppide lõikes või mõlemat korraga?:", choices = valik)
    f = open(andmed, encoding="UTF-8") #avame faili
    eestijrj = [] #järjendid kuhu harutada andmed lahti
    labels = []
    vanustesummad = []
    for rida in f: #hakkan andmeid järjenditesse ette valmistama et neist pandase DataFrame teha lihtsamalt
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
    labels = tuple(labels)
    f.close() #sulgeme
    eestifail = pd.DataFrame(eestijrj, index = labels) #teen neist dataframe
    eestifail = eestifail.astype(float) #määran et väärtused oleksid floatid, sest pandas vahel ei tuvasta arvudena kõiki väärtusi dataframes
    koguarv = pd.DataFrame(vanustesummad, index = labels)
    koguarv = koguarv.astype(float)
    if graafiku_valik == "Vanusegrupid, palun":
        plt.plot(eestifail[0], label='20-24.aastased') #plotime kõik muutused eraldi ja anname nimetused joontele
        plt.plot(eestifail[1], label='25-29.aastased')
        plt.plot(eestifail[2], label='30-34.aastased')
        plt.plot(eestifail[3], label='35-39.aastased')
        plt.plot(eestifail[4], label='40-44.aastased')
        plt.plot(eestifail[5], label='45-49.aastased')
        plt.plot(eestifail[6], label='50-54.aastased')
        plt.plot(eestifail[7], label='55-59.aastased')
        plt.plot(eestifail[8], label='60-64.aastased')       
        plt.legend(loc='upper right') #legendi asukoht
        plt.xlabel('Aasta') #nimetame x ja y teljed ära
        plt.ylabel('Tööealiste eesti meeste arvud vanuse gruppidena Ida-Virumaal')
        plt.show() #show-ga näitame kõiki plottinguid korraga
    if graafiku_valik == "Koguarv, palun":
        koguarv.plot(label = '20-64.aastased')
        plt.legend(loc='upper left')
        plt.xlabel('Aasta')
        plt.ylabel('Tööealiste eesti meeste koguarv, 20-64 a.')
        plt.show()
    if graafiku_valik == "Mõlemad korraga, palun":
        plt.plot(eestifail[0], label='20-24.aastased') 
        plt.plot(eestifail[1], label='25-29.aastased')
        plt.plot(eestifail[2], label='30-34.aastased')
        plt.plot(eestifail[3], label='35-39.aastased')
        plt.plot(eestifail[4], label='40-44.aastased')
        plt.plot(eestifail[5], label='45-49.aastased')
        plt.plot(eestifail[6], label='50-54.aastased')
        plt.plot(eestifail[7], label='55-59.aastased')
        plt.plot(eestifail[8], label='60-64.aastased')       
        plt.legend(loc='upper right')
        plt.xlabel('Aasta')
        plt.ylabel('Tööealiste eesti meeste arvud vanusegruppidena Ida-Virumaal')
        plt.show()
        koguarv.plot(label = '20-64.aastased') #ainult üksj oon ja seetõttu lihtsalt kasutame kogu dataframe plottingut
        plt.legend(loc='upper left')
        plt.xlabel('Aasta')
        plt.ylabel('Tööealiste eesti meeste koguarv, 20-64 a.')
        plt.show()
eestimees('eestlased.csv') #kutsume välja programmi