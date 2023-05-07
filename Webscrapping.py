# Before we start I will import necessary packages before proceeding to the code
from unicodedata import name
from bs4 import BeautifulSoup
import requests
from csv import writer
import os
import wget
# Web link which I will start to parse this information.This site is probably a site which every Mongolian knows
url = 'https://www.unegui.mn/l-hdlh/l-hdlh-zarna/oron-suuts-zarna/'
# For convince I used a mongolian website which everybody knows also the code below is to specify what I want
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('li', class_='announcement-container')
# Since I made a list with engiin zaruud.I am going to collect necessary
# info from my list however this will not contain pictures as i will
# write a different code in order to make things more clean and efficient.
with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['title', 'Zartavisanudur', 'Talibar', 'price']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('a', class_='announcement-block__title').text.replace('\n', '')
        Zartavisanudur = list.find('div', class_='announcement-block__date').text.replace('\n', '')
        Talibar = list.find('div', class_='announcement-block__breadcrumbs').text.replace('\n', '')
        price = list.find('meta', itemprop='price')
        info = [title, Zartavisanudur, Talibar, price]
        thewriter.writerow(info)


# Once you run the code above you will get csv file with the name housing.csv
# Which I will attach with this code here
# What we did is only extract texts inside the url and store it as csv file
# Now I am going to attach pictures following question 2
def imagedown(some,folder):
    try:
        os.mkdir(os.path.join(os.getcwd(),folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(),folder))
    r=requests.get(url)
    soup1 = BeautifulSoup(r.text,'html.parser')
    images = soup1.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace('','_').replace('/','')+'.jpg','wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing',name)

#The function above will parse any url and if it contains files with img
#This will store all pictures it scraped into a single folder
#imagedown()
#But create the folder before declaring the function
# Once we run the code will get all pictures with includes something with favicon and so on
# We can however make our search more specific

imagedown('https://www.unegui.mn/l-hdlh/l-hdlh-zarna/oron-suuts-zarna/','unegui')
