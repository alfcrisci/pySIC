###########################################################
import cropper
import reader
import os
import sys
import shutil
###########################################################
phase = 0
###########################################################

if sys.version_info[0] != 3:
   raise Exception("This module works only with Python 3!")

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def initdirs():
     create_dir('raw_data')
     create_dir('images')
     create_dir('hocr')
     create_dir('pdf_complete')

def removedirs():
     shutil.rmtree('images')
     shutil.rmtree('hocr')
     shutil.rmtree('pdf_complete')


def elaborate(name, ocr = False, lang = "eng", debug = False):
    global phase
    nameDoc = name
    app_folder = os.getcwd()
    fi = os.path.join(app_folder, "raw_data")
    fo = os.path.join(app_folder, "images")
    phase = 1
    cropper.crop(fi, fo, debug)
    if ocr:
        fi, fo,focr,foPDF = fo, os.path.join(app_folder,"images"), os.path.join(app_folder,"hocr"), os.path.join(app_folder,"pdf_complete")
        phase = 2
        reader.read(fi, fo,focr, foPDF, lang, debug, name)
    phase = 0

def getPhase():
    global phase
    if phase == 1: return (phase, cropper.get_percentage())
    elif phase == 2: return (phase, reader.get_percentage())
    else: return None
###########################################################
