import PyPDF2
#import wget
import requests
import os
from bs4 import BeautifulSoup
import re

def extract(raw_string, start_marker, end_marker):
    start = raw_string.index(start_marker) + len(start_marker)
    end = raw_string.index(end_marker, start)
    return raw_string[start:end]

PDFFile = open('/home/ashish/Zedblox/resources/Springer Ebooks.pdf','rb')
#outFile = open('C:/Users/viru_/Documents/Resources/Springer_Ebooks_urls.txt','a+')

PDF = PyPDF2.PdfFileReader(PDFFile)
pages = PDF.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'

for page in range(pages):
    #print("Current Page: {}".format(page))
    pageSliced = PDF.getPage(page)
    pageObject = pageSliced.getObject()
    if key in pageObject.keys():
        ann = pageObject[key]
        for a in ann:
            u = a.getObject()
            if uri in u[ank].keys():
                #print(u[ank][uri])
                #outFile.write(u[ank][uri])
                #outFile.write('\n')
                url = u[ank][uri]
                r = requests.get(url)
                url = r.url

                soup = BeautifulSoup(r.content, 'html.parser')
                s = soup.find_all("div", {"class" : "page-title"})[0].text
                d_filename = extract(s, '\n', '\n')

                url = url.replace("book", "content/pdf")
                url = url + ".pdf"
                print(url)

                if not(os.path.isfile('/home/ashish/Zedblox/resources/downloaded_books/' + d_filename + '.pdf')):
                    r = requests.get(url)
                    d = r.headers['content-disposition']
                    fname = re.findall("filename=(.+)", d)[0]
                    #open('C:/Users/viru_/Documents/Resources/downloaded_books/' + d_filename + '.pdf', 'wb').write(r.content)
                    if not (os.path.isfile('/home/ashish/Zedblox/resources/downloaded_books/' + fname)):
                        open('/home/ashish/Zedblox/resources/downloaded_books/' + fname, 'wb').write(r.content)
