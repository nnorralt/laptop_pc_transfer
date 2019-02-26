import pandas as pd #impordin pandas andmetöötluslibrary

def eestimees(andmed):
    eestifail = pd.read_csv(andmed.strip(""), delimiter=';')   
    eestifail = pd.DataFrame(eestifail) #muudame need andmed dataFrameks, et töödelda paremini Pandase käsklustega
    print(eestifail) #printisime lihtsalt et kontrollida andmeid
     
    
eestimees('eestlased.csv')
