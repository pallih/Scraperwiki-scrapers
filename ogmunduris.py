import scraperwiki
import lxml.html

start = scraperwiki.scrape('http://ogmundur.is/allar-greinar/eldra/')
year_xpath= '//div[1]/div/div/div/a'
root = lxml.html.fromstring(start)
years = root.xpath(year_xpath)

def scrape_year(url,year):
    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html)
    items = root.xpath('//div[@class="newslistdiv"]')
    for item in items:
        try:
            record = {}
            record['date'] = item[0].text
            record['headline'] = item[1].text_content()
            record['url'] = 'http://ogmundur.is' + item[1][0].get('href')
            record['intro'] = item[2].text_content()
            record['year'] = year
            scraperwiki.sqlite.save(['url'], data=record, table_name='ogmundur-articles', verbose=0)
        except Exception:
            pass

for year in years:
    url = 'http://ogmundur.is' + year.get('href')
    scrape_year(url,year.text)
    print 'Done with ', year.text

