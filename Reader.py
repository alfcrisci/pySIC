############################################################
import pytesseract
import cv2
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont

#############################################################
R_percentage = 0

def real(t):
    return "".join([c for c in t if c.isalnum()])

def read(abs_folder_in, abs_folder_out, abs_folder_out_txt, lang, debug):
    global  R_percentage
    app_folder = os.path.dirname(__file__)
    s = sorted([int(i[:-4]) for i in os.listdir(abs_folder_in) if i.endswith(".jpg")])
    images_list = [os.path.join(abs_folder_in, str(i) + ".jpg") for i in s]
    pdfmetrics.registerFont(TTFont('Hebrew', './fonts/test_sans.ttf'))
    w, h = 595.28, 841.89
    pdf = canvas.Canvas(abs_folder_out, pagesize = (w, h))
    for c, img_name in enumerate(images_list, 1):
        im = cv2.imread(img_name, 0)
        text = pytesseract.image_to_data(im, lang = lang, output_type = "dict")
        hx, wx = im.shape
        Kx, Ky = w / wx, h / hx
        pdf.setFont('Hebrew', 10)
        for l, to, te in zip(text["left"], text["top"], text["text"]):
            te = pdf.drawString(l * Kx, h - to * Ky - 5, real(te))
        pdf.showPage()
        if debug: print("Done ", c, " of ", len(images_list))
        R_percentage += 1 / len(images_list)
        txt = " ".join(text["text"]) + "\n"
    with open(abs_folder_out_txt, "w", encoding = "utf-8") as file:
        file.write(txt)
    if debug: print("Saving...")
    pdf.save()
    R_percentage = 0
    
def get_percentage():
    global R_percentage
    return R_percentage

