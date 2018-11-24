# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 14:17:54 2018

@author: henss
"""

# import built in libarys
import os
from urllib.request import urlretrieve, urlopen

# import 3rd party libarys
from bs4 import BeautifulSoup

# import local libarys


# define classes and functions
class PDFweblink(object):
    """
    Class for weblinks containing PDFs to be downloaded.
    """

    def __init__(self, weblink, localpath, pdflinks=list()):
        """
        Class constructor
        """
        self.Weblink = weblink
        self.Localpath = localpath
        self.PDFlinks = pdflinks

    def tweak_pdflinks(self):
        """
        Instance method to tweak relative links to absolute links
        """
        for tp in enumerate(self.PDFlinks):
            if not(tp[1].startswith('http:') or
                   tp[1].startswith('https:') or
                   tp[1].startswith('www.')):
                if self.PDFlinks[tp[0]][0] == '/':
                    first_part = self.Weblink.partition('www.')[0]
                    sec_part = self.Weblink.partition('www.')[2]
                    sec_part = sec_part.partition('/')[0]+tp[1]
                    self.PDFlinks[tp[0]] = str(first_part + 'www.' + sec_part)
                else:
                    first_part = self.Weblink.partition('www.')[0]
                    sec_part = self.Weblink.partition('www.')[2]
                    sec_part = sec_part.partition('/')[0]+'/'+tp[1]
                    self.PDFlinks[tp[0]] = str(first_part + 'www.' + sec_part)
        return(self.PDFlinks)

    def fetch_pdflinks(self):
        """
        Instance method to fetch only pdf from weblink
        """
        html = urlopen(self.Weblink).read()
        pagesoup = BeautifulSoup(html, 'html.parser')
        tp_pdflink = ''
        for tp in pagesoup.find_all('a'):
            tp_pdflink = tp.get('href')
            try:
                if (tp_pdflink.endswith('pdf') and tp_pdflink is not None):
                    self.PDFlinks.append(tp_pdflink)
            except AttributeError:
                pass
        # html.close()
        self.tweak_pdflinks()
        return(self.PDFlinks)

    def download_pdfs(self):
        """
        Instance method to download PDFs
        """
        os.chdir(self.Localpath)
        for tp in enumerate(self.PDFlinks):
            pdf_html = self.PDFlinks[tp[0]]
            pdf_name = self.PDFlinks[tp[0]].rpartition('/')[2]
            urlretrieve(pdf_html, pdf_name)
        print("PDFs are downloaed to: " + str(self.Localpath))


# execute tool
link = r'http://www.ima.uni-stuttgart.de/studium/stud_arbeiten/bereich_zuv/index.html'
path = r'\\imapc\benutzer\Mitarbeiterdaten\henss'

StudArbeiten = PDFweblink(link, path)
StudArbeiten.fetch_pdflinks()
StudArbeiten.download_pdfs()
