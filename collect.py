from urllib2 import urlopen
import re
import pyodbc
from BeautifulSoup import BeautifulSoup

def clean_var (var):
    return var.strip().lower()


url = 'http://examene.calificativ.ro/examene/rezultate-bacalaureat/2012/'
page = urlopen(url).read()
areas = []

# Read district names
for val in re.sub('<(.*?)>','',page).split('\n'):
    if len(val.split('/')[0].strip()) < 3 and len(val.split('/')[0].strip()) > 0:
        areas.append(val.split('/')[0])

for area in areas:
    # Read html filenames
    html = []
    url = 'http://examene.calificativ.ro/examene/rezultate-bacalaureat/2012/'+area+'/'
    page = urlopen(url).read()

    for val in re.sub('<(.*?)>',' ',page).split('\n'):
        if re.match('.*html', val.strip().split(' ')[0]):
            html.append(val.strip().split(' ')[0])
    
    for file in html:

        url = 'http://examene.calificativ.ro/examene/rezultate-bacalaureat/2012/'+area+'/'+file
        page = urlopen(url).read()

        soup = BeautifulSoup(page)
        table = soup.find('table')
         
        rows = table.findAll('tr')
        i = -1
        list = []
        for tr in rows:
            i += 1
            if i == 2:
                i = 0
                print '|'.join(list)
                list = []
            cols = tr.findAll('td')
            for td in cols:
                if len(td.contents) > 0:
                    if len(td.contents) > 2:
                        list.append(clean_var(td.contents[0] + td.contents[2]))
                    else:
                        list.append(clean_var(td.contents[0]))
                else:
                    list.append('None')
