import sys
import pySIC

#build.py, output_name, ocr, language, debug

l = ["", "", False, "", False]

for i, ar in enumerate(sys.argv, 0):
    if ar.upper() == "F": ar = False
    elif ar.upper() == "T": ar = True
    l[i] = ar

pySIC.elaborate(l[1], ocr = l[2], lang = l[3], debug = l[4])
