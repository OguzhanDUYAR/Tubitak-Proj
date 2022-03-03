from odbiotools import fastatools as ft
from odbiotools import gento as gt



mygen=ft.fastostr("FASTA/sequence.fasta")

#print(mygen)

mygentag=ft.fastotag("FASTA/sequence.fasta")

#print(mygentag)

mycodon=gt.gentocod(mygen)

#print(mycodon)

gt.genratio(mygen)
