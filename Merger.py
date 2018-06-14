###############################################################
import os
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
###############################################################
ME_percentage = 0
###############################################################
def Merge(abs_folder_in, name_out, debug):
    global ME_percentage
    app_folder = os.path.dirname(__file__)
    pdf1, pdf2 = PdfFileReader(open(abs_folder_in[0], "rb")), PdfFileReader(open(abs_folder_in[1], "rb"))
    out = PdfFileWriter()
    for page in range(min(pdf1.getNumPages(), pdf2.getNumPages())):
        pag = pdf1.getPage(page)
        if debug: print("pag1: ", pag.mediaBox)
        pag.mergePage(pdf2.getPage(page))
        if debug: print("pag2: ", pdf2.getPage(page).mediaBox)
        out.addPage(pag)
        if debug: print("pag3: ", out.getPage(page).mediaBox)
        if debug: print("Done ", page+1, " of ", min(pdf1.getNumPages(), pdf2.getNumPages()))
        ME_percentage += 1 / min(pdf1.getNumPages(), pdf2.getNumPages())
    out.write(open(name_out+".pdf", "wb"))
    ME_percentage = 0
def get_percentage():
    global ME_percentage
    return ME_percentage
###############################################################
