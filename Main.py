###########################################################
import Cropper
import Maker
import Reader
import Merger
import os
###########################################################
phase = 0
nameDoc = ""
###########################################################
def Elaborate(name, ocr = False, lang = "", debug = False):
    global phase
    global nameDoc
    nameDoc = name
    app_folder = os.path.dirname(__file__)
    fi = os.path.join(app_folder, "data")
    fo = os.path.join(app_folder, "output", "out_cropper")
    phase = 1
    Cropper.Crop(fi, fo, debug)
    fi, fo = fo, os.path.join(app_folder, "output", "out_maker")
    phase = 2
    Maker.Make(fi, fo, name + ".pdf", debug)
    if ocr:
        fo = os.path.join(app_folder, "output", "out_reader")
        fo_txt = os.path.join(app_folder,"output","out_txt")
        phase = 3
        Reader.Read(fi, os.path.join(fo, name+".pdf"), os.path.join(fo_txt, name+".txt"), lang, debug)
        fi = [os.path.join(app_folder, "output", "out_reader", name+".pdf"), os.path.join(app_folder, "output", "out_maker", name+".pdf")]
        fo = os.path.join(app_folder, "output",  name)
        phase = 4
        Merger.Merge(fi, fo, debug)
    phase = 0
def Reset(delData = False, delPdf = {"general": False, "reader": False, "maker": False}):
    if delPdf["general"]:
        dr = os.path.dirname(__file__)
        for d in os.listdir("."):
            if d.endswith(".pdf"):
                os.remove(os.path.join(dr, d))
    if delData:
        dr = os.path.join(os.path.dirname(__file__), "data")
        for d in os.listdir(dr):
            try:
                os.remove(os.path.join(dr, d))
            except:
                pass
    if delPdf["reader"]:
        dr = os.path.join(os.path.dirname(__file__), "output", "out_reader")
        for d in os.listdir(dr):
            os.remove(os.path.join(dr, d))
    if delPdf["maker"]:
        dr = os.path.join(os.path.dirname(__file__), "output", "out_maker")
        for d in os.listdir(dr):
            os.remove(os.path.join(dr, d))
    dr = os.path.join(os.path.dirname(__file__), "output", "out_cropper")
    for d in os.listdir(dr):
        os.remove(os.path.join(dr, d))
def getPhase():
    global phase
    if phase == 1: return (phase, Cropper.get_percentage())
    elif phase == 2: return (phase, Maker.get_percentage())
    elif phase == 3: return (phase, Reader.get_percentage())
    elif phase == 4: return (phase, Merger.get_percentage())
    else: return None
def getName():
    global nameDoc
    return nameDoc
###########################################################
