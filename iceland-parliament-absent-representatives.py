import scraperwiki,re
from BeautifulSoup import BeautifulSoup

starturl = 'http://www.althingi.is/vefur/altutg.html'

def scrape_meeting(url):
    html = scraperwiki.scrape(url)
    soup = BeautifulSoup(html)
    soup.prettify()
    #fjarvistir = soup.find(text=re.compile("Fjarvistarleyfi:").findParent)
    if not "Fjarvistarleyfi" in html:
        print soup.h1.text + " - Ekkert leyfi a thessum fundi - forum i naesta"
        return
    else:
        absent = {}
        print soup.h1.text + " - Ja! - Fjarvistarleyfi a thessum fundi - vinnum ur thvi"
        absent['meeting'] = soup.h1.text
        absent_link = soup.find(text=re.compile("Fjarvistarleyfi")).findParent('a')['href']
        #print absent_link['href']
        html = scraperwiki.scrape(absent_link)
        soup = BeautifulSoup(html)
        absent['assembly_number'] = re.split(" ",soup.title.text)[1][:3]
        p = soup.findAll('p')
        for p in p:
            absent['representative'] = re.sub(", \w.*","",p.text)
            scraperwiki.datastore.save(["meeting", "assembly_number", "representative"], absent)

def scrape_meeting_list(url):

    html = scraperwiki.scrape(url)
    soup = BeautifulSoup(html)
    soup.prettify()
    td = soup.findAll('td', {'align' : 'RIGHT' })
    for td in td:
        meeting_url = "http://www.althingi.is" + td.a['href']
        scrape_meeting(meeting_url)
    scraperwiki.metadata.save(url, '1')

def scrape_assembly_list(url):
    html = scraperwiki.scrape(url)
    soup = BeautifulSoup(html)
    soup.prettify()
    a = soup.findAll('a')
    for a in a:
        url = a['href']
        if re.search('fulist',url):
            url = "http://althingi.is" + url
            assembly_list_seen = scraperwiki.metadata.get(url)
            if assembly_list_seen is not None:
                print "Sed adur - sleppum: " + url
            else:
                scrape_meeting_list(url)
        

scrape_assembly_list(starturl)
