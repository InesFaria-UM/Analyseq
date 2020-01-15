#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:38:20 2020

@author: fernandavieira
"""

from Bio import ExPASy
from Bio import SeqIO
import requests

class PropriedadesProt:
    
    def swissprot(self,accnumber, op):
        
        handle = ExPASy.get_sprot_raw(str(accnumber))
        url=handle.url
        url=url.replace('txt','xml')
        response = requests.get(url)
        with open('ficheiro.xml','wb') as file:
            file.write(response.content)
        ficheiro=SeqIO.read('ficheiro.xml','uniprot-xml')
        #print(ficheiro.seq)
        # print(ficheiro.annotations)
        if op==1:
            print(ficheiro.annotations['taxonomy'])
        if op==2:
            print(ficheiro.annotations['references'])
        if op==3:
            print(ficheiro.annotations['comment_catalyticactivity'])
        if op==4:
            print(ficheiro.annotations['comment_pathway'])
        if op==5:
            if ficheiro.annotations['comment_subcellularlocation_location']== None:
                print('Não tem localização')
            else:
                print(ficheiro.annotations['comment_subcellularlocation_location'])
        if op==6:
            print(ficheiro.annotations['comment_function'])
        if op==7:
            if ficheiro.annotations['comment_subunit'] is None:
                print('Não tem coment_subunit')    
            else:
                print(ficheiro.annotations['comment_subunit'])
        if op==8:
            if ficheiro.annotations['comment_disease'] is None:
                print('Não tem comment_disease')
            else:
                print(ficheiro.annotations['comment_disease'])
        if op==9:
            print(ficheiro.annotations['comment_similarity'])
        if op==10:
            print(ficheiro.annotations['keywords'])    

