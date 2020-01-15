# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 10:53:00 2019

@author: mines
"""
from Bio import Entrez 

'''
Análise da Literatura

'''

#retirado de https://marcobonzanini.wordpress.com/2015/01/12/searching-pubmed-with-python/

    
class Literatura:
    def search(self,query):
        Entrez.email='marinapt88@gmail.com'
        handle=Entrez.esearch(db='pubmed',sort='relevance',retmax='20',retmode='xml',term=query)
        results=Entrez.read(handle)
        return results
    
    def fetch_details(self,id_list):
        ids=','.join(id_list)
        Entrez.email='marinapt88@gmail.com'
        handle=Entrez.efetch(db='pubmed',retmode='xml',id=ids)
        results=Entrez.read(handle)
        return results
    
    
    
    
 