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
                    try:
                        d = r.headers['content-disposition']
                        fname = re.findall("filename=(.+)", d)[0]
                    except KeyError:
                        print("No download option? " + d_filename)
                        continue
                    except Exception:
                        print("fname something went wrong? " + d_filename)
                        continue
                    if not (os.path.isfile('/home/ashish/Zedblox/resources/downloaded_books/' + fname)):
                        try:
                            open('/home/ashish/Zedblox/resources/downloaded_books/' + fname, 'wb').write(r.content)
                        except Exception:
                            print("Unable to download: " + fname)
