#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:27:07 2020

@author: fernandavieira
"""

from cmd import *
import json
from Blast import My_Blast
from Literatura import Literatura
from AnaliseNCBI import AnaliseNCBI
from PropriedadesProt import PropriedadesProt

class Shell(Cmd):
    intro= """Comandos úteis:
        
===================Laboratórios de Bioinformática==================

    1. analiseliteratura - Análise de literatura
    2. analiseNCBI - Análise da sequência e das features     
    3. blast - (insira: Ficheiro_fasta.txt Ficheiro.xml Base_de_dados)
    4. swissprot - Análise das propriedades proteícas              
    5. sair 
        
======================================================================

"""  
    prompt="Escolha dos comandos> "
    
    
    def do_analiseliteratura(self,arg):
        """Comando que faz a análise da literatura através do PubMed"""
        try:
            results=l.search(str(input("O que deseja procurar? ")))
            l.id_list=results['IdList']
            papers=l.fetch_details(l.id_list)
            for i, paper in enumerate(papers['PubmedArticle']):
                print('%d) %s' % (i+1, paper['MedlineCitation']['Article']['ArticleTitle']))
            dic={1:0,2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8,10:9,11:10,12:11,13:12,14:13,15:14,16:15,17:16,18:17,19:18,20:19}
            li=int(input('Escolha o artigo: ')) 
            pos=dic[li]
            print (json.dumps(papers['PubmedArticle'][pos],indent=2,separators=(',' , ':')))    

        except:
            print("Erro na análise da literatura!")
            
    def do_analiseNCBI(self,arg):
        try:
            gene=str(input("O que deseja procurar? "))
            results=a.search(gene)
            a.id_list=results['IdList']
            record=a.fetch_details(a.id_list)
    #        print(record)
            for i, rec in enumerate(range(len(a.id_list))):
                n_id = record['DocumentSummarySet']['DocumentSummary'][i].attributes['uid']
                sc_name = record['DocumentSummarySet']['DocumentSummary'][i]['Organism']['ScientificName']
                # ChrAccVer=record['DocumentSummarySet']['DocumentSummary'][0]['GenomicInfo'][0]['ChrAccVer']
                '''Fazer com que a posição escolhida 1 seja o humano'''
                # StartPosition=record['DocumentSummarySet']['DocumentSummary'][i]['GenomicInfo'[2]]
                # EndPosition=record['DocumentSummarySet']['DocumentSummary'][i]['GenomicInfo'[3]]
                print( '%d) %s - %s ' % (i+1, n_id, sc_name))
            dic={1:0,2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8,10:9,11:10,12:11,13:12,14:13,15:14,16:15,17:16,18:17,19:18,20:19}
            a.li=int(input('Em que posição se encontra da lista? '))
            pos=dic[a.li]
            file_name=a.get_Chr(record,gene,pos)
            proteins=a.get_annotations(file_name)
            protein_id=str(input('Protein_id: '))
            a.get_fasta(proteins,gene,protein_id)
            
        except:
            print("Erro na análise do NCBI!")
    

    def do_blast(self,arg):
        """Comando que faz o Blast e coloca o seu resultado num ficheiro"""
        try:
            argumentos=arg.strip("\n").split(" ")
            if len(argumentos)==3:
                Blast=My_Blast(argumentos[0], argumentos[1], argumentos[2])
                TRESH=input('Qual é o valor do e-value Tresh: ')
                Blast.blast(TRESH)
                
            else:
                print("Número de argumentos errados!")
        except:
            print("Erro a executar o blast!")
        
        
    def do_swissprot(self,arg):
        try:
            accnumber=str(input('Qual é o accnumber? '))
            print(accnumber)
            print('''
            ****  OPTIONS: ****
            1) Taxonomy
            2) References
            3) Catalytic Activity
            4) Pathways
            5) Subcellular activity
            6) Function
            7) Subunit
            8) Diseases
            9) Similarity
            10) Keywords
    ''')
            op= int(input('Escolha a opção: '))
            s.swissprot(accnumber, op)
        
        except:
            print('Erro a executar o swiss_prot')
    
    def do_sair(self, arg):
        """sair do programa"""
        global janela       #atribuir um valor a um identificador global
        if janela is not None:
            del janela
        return True


if __name__ == "__main__":
    janela=None
    l=Literatura()
    a=AnaliseNCBI()
    s=PropriedadesProt()
    Shell().cmdloop()
    