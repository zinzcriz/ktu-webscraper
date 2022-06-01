#importing webscraping libraries

from bs4 import BeautifulSoup
import requests
import re
#assigning url of the targetted website
url="https://ktu.edu.in/home.htm;jsessionid=DBCCCE2AFFAD26F93141CD46A46346DF"

#requests the url and save the response to the response variable
response=requests.get(url)

#parses the fetched html document
soup=BeautifulSoup(response.text, 'html.parser')

#searches for a division named news block
data = soup.find('div', attrs={'class': 'news-blocks'})
#find all html elements with bold tag in the
c=data.find_all("b")
for i in c:
    if i.string is not None:
        print(i.string)