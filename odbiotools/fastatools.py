# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 19:12:44 2022

@author: Oguhan DUYAR (oguzhan.duyar.ogresyus@gmail.com)
"""

def fastostr(myfileloc):
    with open(myfileloc, "r", encoding="utf-8" ) as myfile:
        mylist= myfile.readlines()
        
    genstr=""
    for x in mylist[1:]:
        genstr += x.strip("\n")
    genstr=genstr.upper()
    return genstr

        
def fastotag(myfileloc):
    with open(myfileloc, "r", encoding="utf-8" ) as myfile:
        mylist= myfile.readline()
    gentag=mylist.strip("\n")
    return gentag