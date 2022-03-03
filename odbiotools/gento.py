# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 19:12:44 2022

@author: Oguhan DUYAR (oguzhan.duyar.ogresyus@gmail.com)
"""
# Protein Dictionary
proteincode = {  'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M','ACA':'T', 'ACC':'T', 'ACG':'T',
             'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S',
             'AGA':'R', 'AGG':'R','CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P',
             'CCC':'P', 'CCG':'P', 'CCT':'P','CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
             'CGA':'R', 'CGC':'R','CGG':'R', 'CGT':'R','GTA':'V', 'GTC':'V', 'GTG':'V',
             'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A','GAC':'D', 'GAT':'D',
             'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G','TCA':'S',
             'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
             'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*','TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}


def gentocod(genstr):
    codon=[]
    for x in range(0, len(genstr), 3):
        y=genstr[x:x+3]
        codon.append(y)
    return codon

def genratio(genstr):
    print("-Guanine count = ", genstr.count('G'))
    print("-Cytosine count = ", genstr.count('C'))
    print("-Adenine count = ", genstr.count('A'))
    if genstr.count("U")==0:
        print("-Thymine count = ", genstr.count('T'))
        print("-- Ratios of Bases  -- \n-A {:2.2%} \n-T {:2.2%}  \n-G {:2.2%} \n-C {:2.2%}  " .format((genstr.count("A")/len(genstr)),(genstr.count("T")/len(genstr)),(genstr.count("G")/len(genstr)),(genstr.count("C")/len(genstr))))
        print("-- Ratios of Base Pairs  -- \n-AT {:2.2%} \n-GS {:2.2%} " .format(((genstr.count("A")+genstr.count("T"))/len(genstr)),((genstr.count("G")+genstr.count("C"))/len(genstr))))
    else:
        print("-Uracil count = ", genstr.count('U'))
        print("-- Ratios of Bases  -- \n-A {:2.2%} \n-U {:2.2%}  \n-G {:2.2%} \n-C {:2.2%}  " .format((genstr.count("A")/len(genstr)),(genstr.count("U")/len(genstr)),(genstr.count("G")/len(genstr)),(genstr.count("C")/len(genstr))))
        print("-- Ratios of Base Pairs  -- \n-AU {:2.2%} \n-GC {:2.2%} " .format(((genstr.count("A")+genstr.count("U"))/len(genstr)),((genstr.count("G")+genstr.count("C"))/len(genstr))))

        


# def codtopro(codstr):