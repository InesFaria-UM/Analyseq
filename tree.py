# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:20:08 2020

@author: migue
"""

from Bio import Phylo
tree = Phylo.read("align.dnd", "newick")
text = Phylo.draw_ascii(tree)

'''
Alinhamento múltiplo e árvore filogenética criada através do docker clustalw 
usado nas aulas de Laboratótios de bioinformática. Print da árvore criado com o
auxílio da biblioteca Phylo.
'''