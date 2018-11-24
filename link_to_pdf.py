# -*- coding: utf-8 -*-
"""
Created Nov 2018

@author: henss
"""

# import built in libarys
import os
from urllib.request import urlretrieve, urlopen

# import 3rd party libarys
from bs4 import BeautifulSoup

# import local libarys


# define classes and functions
class Weblink():
    """
    Class for weblinks containing PDFs to be downloaded.
    """

    def __init__(self, weblink, pdflist=list()):
        """
        Class constructor
        """
        self.Weblink = weblink
        self.PDFlist = pdflist

    def tweak_pdflinks(self):
        """
        Instance method to tweak relative links to absolute links
        """
        for tp in enumerate(self.PDFlist):
            if not(tp[1].startswith('http:') or
                   tp[1].startswith('https:') or
                   tp[1].startswith('www.')):
                if self.PDFlist[tp[0]][0] == '/':
                    first_part = self.Weblink.partition('www.')[0]
                    sec_part = self.Weblink.partition('www.')[2]
                    sec_part = sec_part.partition('/')[0]+tp[1]
                    self.PDFlist[tp[0]] = str(first_part + 'www.' + sec_part)
                else:
                    first_part = self.Weblink.partition('www.')[0]
                    sec_part = self.Weblink.partition('www.')[2]
                    sec_part = sec_part.partition('/')[0]+'/'+tp[1]
                    self.PDFlist[tp[0]] = str(first_part + 'www.' + sec_part)
        return(self.PDFlist)

    def fetch_pdflinks(self):
        """
        Instance method to fetch only pdf's from weblink
        """
        html = urlopen(self.Weblink).read()
        pagesoup = BeautifulSoup(html, 'html.parser')
        tp_pdflink = ''
        for tp in pagesoup.find_all('a'):
            tp_pdflink = tp.get('href')
            try:
                if (tp_pdflink.endswith('pdf') and tp_pdflink is not None):
                    self.PDFlist.append(tp_pdflink)
            except AttributeError:
                pass
        # html.close()
        self.tweak_pdflinks()
        return(self.PDFlist)

    def download_pdfs(self, localpath):
        """
        Instance method to download PDFs
        """
        os.chdir(localpath)
        for tp in enumerate(self.PDFlist):
            pdf_html = self.PDFlist[tp[0]]
            pdf_name = self.PDFlist[tp[0]].rpartition('/')[2]
            urlretrieve(pdf_html, pdf_name)
        print("PDFs are downloaed to: " + str(localpath))
