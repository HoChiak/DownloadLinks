from module_pdf_link import PDFweblink

link = r'http://www.ima.uni-stuttgart.de/studium/stud_arbeiten/bereich_zuv/index.html'
path = r'C:\Users\%USERNAME%\Desktop'

StudArbeiten = PDFweblink(link, path)
StudArbeiten.fetch_pdflinks()
StudArbeiten.download_pdfs()
