import scraperwiki
emaillibrary = scraperwiki.utils.swimport("general-emails-on-scrapers")
subjectline, headerlines, bodylines, footerlines = emaillibrary.EmailMessageParts("onlyexceptions")
if bodylines:
    print "\n".join([subjectline] + headerlines + bodylines + footerlines)