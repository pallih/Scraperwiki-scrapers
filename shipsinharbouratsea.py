import scraperwiki
import requests
from lxml import etree
import lxml.html
import datetime

now = datetime.datetime.now()

print "Hour: %d" % now.hour

ships_in_port_url = 'http://www.112.is/Stat/StatsService.asmx/ShipInPortInSea'

post_data = {"Content-Length": 0}

r = requests.post(ships_in_port_url, post_data)

print r.status_code
print r.headers['content-type']
xml = r.content.encode('utf-8')
print xml

#root = etree.fromstring(xml)
root = lxml.html.fromstring(xml)
nodes = root.xpath('//arrayofshipinportinsea/shipinportinsea/.')
for m in nodes:
    for d in m:
        if d.tag == 'hourfrom' and d.text == str(now.hour):
            print d.tag, d.text
            for x in m:
                print x.tag, x.text
exit()
parser = etree.XMLParser()
tree = etree.XML(xml, parser)
for node in tree.iter('{http://tempuri.org/}ShipInPortInSea'):
#    print node
#        record = {}
    #for item in node.iter('{http://tempuri.org/}ShipInPortInSea'):
    for item in node.iter('{http://tempuri.org/}CurrDate'):
        print 'Date: ', item.text #, item.nsmap
    for item in node.iter('{http://tempuri.org/}HourFrom'):
        print 'Hour from: ', item.text
    for item in node.iter('{http://tempuri.org/}HourTo'):
        print 'Hour to ', item.text
    for item in node.iter('{http://tempuri.org/}Sea'):
        print 'At sea: ', item.text
    for item in node.iter('{http://tempuri.org/}Port'):
        print 'NOT at sea: ', item.text
           




