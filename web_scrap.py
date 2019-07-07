import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

name = []
runs= []
inn=[]
avg=[]



URL = "https://en.wikipedia.org/wiki/List_of_Afghanistan_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)

URL="https://en.wikipedia.org/wiki/List_of_Australia_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[1:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[6].text)
    inn.append(data[4].text)
    avg.append(data[8].text)


URL="https://en.wikipedia.org/wiki/List_of_Bangladesh_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[6].text)
    inn.append(data[4].text)
    avg.append(data[8].text)

URL="https://en.wikipedia.org/wiki/List_of_Bermuda_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[7].text)
    inn.append(data[4].text)
    avg.append(data[11].text)

URL="https://en.wikipedia.org/wiki/List_of_Canada_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)

URL="https://en.wikipedia.org/wiki/List_of_East_Africa_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[7].text)
    inn.append(data[4].text)
    avg.append(data[11].text)

URL="https://en.wikipedia.org/wiki/List_of_England_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)

URL="https://en.wikipedia.org/wiki/List_of_Hong_Kong_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)

URL="https://en.wikipedia.org/wiki/List_of_India_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[7].text)
    inn.append(data[4].text)
    avg.append(data[9].text)

URL="https://en.wikipedia.org/wiki/List_of_Ireland_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)

URL="https://en.wikipedia.org/wiki/List_of_Kenya_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)

URL="https://en.wikipedia.org/wiki/List_of_Namibia_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)

URL="https://en.wikipedia.org/wiki/List_of_Nepal_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)

URL="https://en.wikipedia.org/wiki/List_of_Netherlands_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)

URL="https://en.wikipedia.org/wiki/List_of_New_Zealand_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[6].text)
    inn.append(data[4].text)
    avg.append(data[8].text)


URL="https://en.wikipedia.org/wiki/List_of_Oman_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)

URL="https://en.wikipedia.org/wiki/List_of_Pakistan_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[6].text)
    inn.append(data[4].text)
    avg.append(data[8].text)


URL="https://en.wikipedia.org/wiki/List_of_Papua_New_Guinea_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)


URL="https://en.wikipedia.org/wiki/List_of_Scotland_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)


URL="https://en.wikipedia.org/wiki/List_of_South_Africa_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[6].text)
    inn.append(data[4].text)
    avg.append(data[8].text)

URL="https://en.wikipedia.org/wiki/List_of_Sri_Lanka_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[6].text)
    inn.append(data[4].text)
    avg.append(data[8].text)


URL="https://en.wikipedia.org/wiki/List_of_United_Arab_Emirates_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)


URL="https://en.wikipedia.org/wiki/List_of_United_States_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[5].text)
    inn.append(data[4].text)
    avg.append(data[7].text)


URL="https://en.wikipedia.org/wiki/List_of_West_Indies_ODI_cricketers"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[2:]:
    data=(items.find_all(['th','td']))
    name.append(data[1].text)
    runs.append(data[6].text)
    inn.append(data[4].text)
    avg.append(data[8].text)

import pandas
df = pandas.DataFrame(data={"Names": name, "Runs": runs, "Innings": inn, "Average": avg})
df.to_csv("runs.csv", sep=',',index=False)

