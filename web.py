import pandas as pd
import matplotlib.pyplot as plt

plik = "C://scieżka do pliku"
from bs4 import BeautifulSoup
with open(plik, "r", encoding='utf-8') as f:
    soup = BeautifulSoup(f) 
    lista = soup.findAll('div', attrs={'class':'_2lek'})
    print(len(lista))

import csv

lista[0].string
d = lista[0].string[12:]
d = d.replace(' i ', ', ')
d = d.split(',')

myData = [d]
myFile = open('csvexample3.csv', 'w', encoding="utf-8")
with myFile:
   writer = csv.writer(myFile)
   writer.writerows(myData)
   

df = pd.read_csv('csvexample3.csv',header=None, sep=',')
df = df.transpose()
df = df.rename(columns={0:"Imie Nazwisko"})
df["Imie Nazwisko"] = df["Imie Nazwisko"].str.strip()
df["Liczba Wiadomości"] = 0

lista = soup.findAll('div', attrs={'class':'_3-96 _2pio _2lek _2lel'})

for i in range(len(df)):
    result = []
    for th in lista:
        result.extend(th.find_all(text=df.iloc[i][0].strip()))
    
    df.at[i,"Liczba Wiadomości"] = result.count(df.iloc[i][0].strip())  

lista = soup.findAll('div', attrs={'class':'pam _3-95 _2pi0 _2lej uiBoxWhite noborder'})
lista = lista[1:]

df["Długość wszystkich wiadomości"] = 0
df["Plik/Zdj"] = 0
df["Link"] = 0


for i,th in enumerate(lista):
    try:
        index = df[df["Imie Nazwisko"] == lista[i].contents[0].contents[0]].index[0]
        lista[16].contents[1].contents[0].contents[1].contents[0].name == 'a'
        if 'https' in str(lista[i]) or 'http' in str(lista[i]):
            df.at[index,"Link"] += 1
        elif lista[i].find_all("a") != []:
            df.at[index,"Plik/Zdj"] += 1
            temp.append(i)
        else:
            df.at[index,"Długość wszystkich wiadomości"] += len(lista[i].contents[1].contents[0].contents[1].contents[0])
    except:
        print(i, end=' ')

df['Znaki/Wiadomosc'] = df['Długość wszystkich wiadomości']/df['Liczba Wiadomości']


plt.figure(figsize=(40,40))
df.nlargest(10,"Liczba Wiadomości")[["Imie Nazwisko","Liczba Wiadomości"]].set_index('Imie Nazwisko').plot.pie(subplots=True, autopct="%.2f",legend=None,ylabel='')
plt.title('Liczba wysłanych wiadomości')
plt.savefig("Liczba_wiadomosc.png")
plt.show()


plt.figure(figsize=(40,40))
df.nlargest(10,'Długość wszystkich wiadomości')[["Imie Nazwisko","Długość wszystkich wiadomości"]].set_index('Imie Nazwisko').plot.pie(subplots=True, autopct="%.2f",legend=None,ylabel='')
plt.title('Łączna liczba wysłanych znaków')
plt.savefig('Łącznie_znaki.png')
plt.show()

plt.figure(figsize=(40,40))
df.nlargest(10,'Znaki/Wiadomosc')[["Imie Nazwisko",'Znaki/Wiadomosc']].sort_values('Znaki/Wiadomosc',ascending=False).set_index('Imie Nazwisko').plot.bar()
plt.title('Średnia znaków/wiadomość ')
plt.savefig('Srednie_znaki.png')
plt.show()

#____
#
#plt.figure(figsize=(40,40))
#df.nlargest(10,'Znaki/Wiadomosc')[["Imie Nazwisko",'Znaki/Wiadomosc']].sort_values('Znaki/Wiadomosc',ascending=False).set_index('Imie Nazwisko').plot.bar()
#plt.title('Średnia znaków/wiadomość')
#plt.savefig('Srednia.png')
#plt.show()

dft = pd.DataFrame({
    "Dni Tygodnia":["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"]
})
import datetime
slownik = {"cze":6,"maj":5,"kwi":4,"mar":3,"lut":2,"sty":1,"gru":12,"lis":11,"paź":10}
dft['Liczba wiadomości'] = 0
for i in range(len(lista)):
    try:
        l1 = []
        l1 = lista[i].contents[2].string.split(None, 3)
        l1[2]=l1[2].replace(',','')
        l1 = l1[:-1]
        l1[1] = slownik[l1[1]]
        day, month, year = (int(x) for x in l1)    
        ans = datetime.date(year, month, day)
        idx = int(ans.strftime("%w"))
        dft.at[idx, 'Liczba wiadomości'] += 1
    except:
        print(i, end=' ')

dft.set_index('Dni Tygodnia').plot.pie(subplots=True,autopct="%.f%%",legend=None,ylabel='')
plt.savefig('Kolo_tyg.png')

dfg = pd.DataFrame({
    "Godziny":pd.date_range("00:00", "23:59", freq="60min").strftime('%H:%M')
})
dfg['Liczba Wiadomości'] = 0
for i in range(len(lista)):
    indx = int(lista[i].contents[2].string.split(None, 3)[3].split(":")[0])
    dfg.at[indx, "Liczba Wiadomości"] += 1


for i in range(len(lista3)):
    for el in lista3[i]:
        try:
            index = df[df["Imie Nazwisko"] == el.string[1:]].index[0]
            df.at[index,"Reakcje"] += 1
        except:
            try:
                index = df[df["Imie Nazwisko"] == el.string[2:]].index[0]
                df.at[index,"Reakcje"] += 1
            except:
                print(el, "i: ",i)
				

df.set_index('Imie Nazwisko').nlargest(10,'Reakcje').plot.barh(color='brown')
plt.ylabel('')
plt.xlabel('Liczba reakcji')
plt.title("Liczba reakcji na osobe")
plt.savefig('Reakcje.png')
plt.show()

dfi = pd.DataFrame({
    "Ikonki" : baza_ikonek
})
dfi = dfi.drop_duplicates('Ikonki')
dfi['Liczba wystąpień'] = 0
dfi


dfi[dfi["Ikonki"] == "👨"].index[0]


el=lista3[493]
t = el.string[:1]
baza_ikonek = []
for i in range(len(lista3)):
    for el in lista3[i]:
        try:
            indx = dfi[dfi["Ikonki"] == el.string[:1]].index[0]
            dfi.at[indx, "Liczba wystąpień"] +=1
        except:
            print(i, end=' ')
