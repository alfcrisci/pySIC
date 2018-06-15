######################################################
from fpdf import FPDF
import os

######################################################
M_percentage = 0


def make(abs_folder_in, abs_folder_out, name_out, debug):
    global M_percentage
    s = [int(i[:-4]) for i in os.listdir(abs_folder_in) if i.endswith(".jpg")]
    s.sort()
    images_list = [os.path.join(abs_folder_in, str(i) + ".jpg") for i in s]
    if debug: print("\n".join(images_list))
    pdf = FPDF()
    for c, image_name in enumerate(images_list, 1):
        pdf.add_page()
        pdf.image(image_name, 0, 0, 210, 297)
        if debug: print("Done", c, " of ", len(images_list))
        M_percentage += (1 / len(images_list))
    if debug: print("Saving...")
    pdf.output(os.path.join(abs_folder_out, name_out), "F")
    M_percentage = 0
    
def get_percentage():
    global M_percentage
    return M_percentage
######################################################
