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
    Class for weblinks containing Filetypes to be downloaded.
    """

    def __init__(self, weblink, LinkList=list()):
        """
        Class constructor
        """
        self.Weblink = weblink
        self.LinkList = LinkList

    def tweak_links(self):
        """
        Instance method to tweak relative links to absolute links
        """
        for tp in enumerate(self.LinkList):
            if not(tp[1].startswith('http:') or
                   tp[1].startswith('https:') or
                   tp[1].startswith('www.')):
                if self.LinkList[tp[0]][0] == '/':
                    first_part = self.Weblink.partition('www.')[0]
                    sec_part = self.Weblink.partition('www.')[2]
                    sec_part = sec_part.partition('/')[0]+tp[1]
                    self.LinkList[tp[0]] = str(first_part + sec_part)
                else:
                    first_part = self.Weblink.partition('www.')[0]
                    sec_part = self.Weblink.partition('www.')[2]
                    sec_part = sec_part.partition('/')[0]+'/'+tp[1]
                    self.LinkList[tp[0]] = str(first_part + sec_part)
        return(self.LinkList)

    def fetch_links(self, filetype='pdf'):
        """
        Instance method to fetch only links of the given filetype from weblink
        """
        html = urlopen(self.Weblink).read()
        pagesoup = BeautifulSoup(html, 'html.parser')
        tp_link = ''
        for tp in pagesoup.find_all('a'):
            tp_link = tp.get('href')
            try:
                if (tp_link.endswith(filetype) and tp_link is not None):
                    self.LinkList.append(tp_link)
            except AttributeError:
                pass
        # html.close()
        self.tweak_links()
        return(self.LinkList)

    def download_links(self, localpath):
        """
        Instance method to download Links
        """
        os.chdir(localpath)
        for tp in enumerate(self.LinkList):
            link_html = self.LinkList[tp[0]]
            link_name = self.LinkList[tp[0]].rpartition('/')[2]
            urlretrieve(link_html, link_name)
        print("Links are downloaed to: " + str(localpath))
