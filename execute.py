# -*- coding: utf-8 -*-
"""
Created Nov 2018

@author: henss
"""

# import built in libarys

# import 3rd party libarys

# import local libarys
import link_to_pdf as ltp

#%%
# set paramters
link = r'http://www.ima.uni-stuttgart.de/studium/stud_arbeiten/bereich_zuv/index.html'
path = r'C:\User\%Username%\Downloads'

# execute tool
pdflink = ltp.Weblink(link)  # create instance
pdflink.fetch_links(filetype='pdf')  # fetch all available PDFs links from weblinks
pdflink.download_links(path)  # download the fetched PDFs
