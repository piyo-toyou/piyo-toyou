# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:30:09 2021

@author: mgkog
"""

import zipfile
import os, glob

BasicPATH = os.getcwd()
file_list = glob.glob(BasicPATH + "/*.zip")

for i in file_list:
    with zipfile.ZipFile(i) as zf:
            zf.extractall("C:/Users/mgkog/Desktop/Jack")
