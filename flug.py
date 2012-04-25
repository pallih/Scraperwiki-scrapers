import scraperwiki
import lxml.html

html = scraperwiki.scrape('http://www.isavia.is')

#print html
root = lxml.html.fromstring(html)
content = root.xpath ("//div [@class='content']/div[@class='item']")

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


for x in content:
    record = {}
    to = str(x.attrib['rel'])
    for case in switch(to):
        if case('RKV'):
            to=' í Reykjavík (' + to + ')'
            break
        if case('AEY'):
            to = ' á Akureyri (' + to  + ')'
            break
        if case('KEF'):
            to = ' í Keflavík (' + to  + ')'
            break
        if case('EGS'):
            to = ' á Egilsstöðum (' + to  + ')'
            break
        if case('IFJ'):
            to = ' á Ísafirði (' + to  + ')'
            break
        if case('VEY'):
            to = ' í Vestmannaeyjum (' + to  + ')'
            break
        if case('HFN'):
            to = ' á Hornafirði (' + to  + ')'
            break
        if case('GRY'):
            to = ' í Grímsey (' + to  + ')'
            break
        if case('BIU'):
            to = ' á Bíldudal (' + to  + ')'
            break
        if case('VPN'):
            to = ' á Vopnafirði (' + to  + ')'
            break
        if case('THO'):
            to = ' á Þórshöfn (' + to  + ')'
            break
        if case('TEY'):
            to = ' á Þingeyri (' + to  + ')'
            break
        if case('GJR'):
            to = ' á Gjögri (' + to  + ')'
            break
        if case(): # default, could also just omit condition or 'if True'
            to = to
    
    
    record['to'] = to
    #print x.text_content().encode('iso-8859-1') + ' --- ' + str(x.attrib)
    record['from'] = x[0].text.encode('iso-8859-1')
    record['flightcode'] = x[0][0].text.encode('iso-8859-1')
    record['time'] = x[1].text.encode('iso-8859-1')
    record['date'] = x[1][0].text.encode('iso-8859-1')
    try:
        record['comment'] = x[2].text#.encode('utf-8')
    except AttributeError:
        pass 
    try:
        if 'Lent' in record['comment']:
            print 'Klukkan ' + record['time'] + ' lenti vél ('+record['flightcode']+') frá ' + record['from'] + record['to'] + ' - http://info.flightmapper.net/flight/'+record['flightcode'][:2]+'_'+record['flightcode'][2:]
    except TypeError:
        pass
    #print record
