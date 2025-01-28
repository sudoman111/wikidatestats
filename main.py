import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

days = range(1,32)
# days = range(1,5)
months = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre']
# months = ['janvier']

wikipediaApiUrl = 'https://api.wikimedia.org/core/v1/wikipedia/'
language_code = 'fr'
headers = {
  # 'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
  'User-Agent': 'MOSTBIRTHTDATES (mail@mail.com)'
}

# make data:
x = []
y = []

# x = ['1_janvier', '2_janvier', '3_janvier', '4_janvier'] 
# y = [0, 160, 200, 184]

for month in months:
    for day in days:
        date = str(day) + '_' + month
        page = '/page/' + date + '/html'
        x.append(date)
        url = wikipediaApiUrl + language_code + page 
        response = requests.get(url, headers=headers)
        html_doc = response.text
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
        soup = BeautifulSoup(html_doc, 'html.parser')
        naissances = soup.find(id="Naissances")
        if naissances:
          nbDeNaissance = len(naissances.previous_element.find_all('li'))
          y.append(nbDeNaissance)
        else:
          y.append(0)

# plot
fig, ax = plt.subplots()

bars = ax.bar(x, y)

ax.bar_label(bars)

plt.ylabel('nombre de naissances')
plt.show()