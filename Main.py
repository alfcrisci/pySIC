###########################################################
import Cropper
import Maker
import Reader
import Merger
import os
###########################################################
phase = 0
###########################################################
def Elaborate(name, ocr = False, debug = False):
    global phase
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
        phase = 3
        Reader.Read(fi, fo + "\\"+name+".pdf", debug)
        fi = [os.path.join(app_folder, "output", "out_reader", name+".pdf"), os.path.join(app_folder, "output", "out_maker", name+".pdf")]
        fo = name
        phase = 4
        Merger.Merge(fi, fo, debug)
    phase = 0
def Reset(delData = False, delPdf = {"general": False, "reader": False, "maker": False}):
    if delPdf["general"]:
        dr = os.path.dirname(__file__)
        for d in os.listdir("."):
            if d.endswith(".pdf"):
                os.remove(dr+"\\"+d)
    if delData:
        dr = os.path.join(os.path.dirname(__file__), "data")
        for d in os.listdir(dr):
            os.remove(dr+"\\"+d)
    if delPdf["reader"]:
        dr = os.path.join(os.path.dirname(__file__), "output", "out_reader")
        for d in os.listdir(dr):
            os.remove(dr+"\\"+d)
    if delPdf["maker"]:
        dr = os.path.join(os.path.dirname(__file__), "output", "out_maker")
        for d in os.listdir(dr):
            os.remove(dr+"\\"+d)
    dr = os.path.join(os.path.dirname(__file__), "output", "out_cropper")
    for d in os.listdir(dr):
        os.remove(dr+"\\"+d)
def getPhase():
    global phase
    if phase == 1: return (phase, Cropper.getPercentage())
    elif phase == 2: return (phase, Maker.getPercentage())
    elif phase == 3: return (phase, Reader.getPercentage())
    elif phase == 4: return (phase, Merger.getPercentage())
    else: return None
###########################################################
