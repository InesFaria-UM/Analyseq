#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:55:31 2020

@author: fernandavieira
"""

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO

class My_Blast:
    def __init__(self,file_fasta,file_xml,db="nr"):
        """Recebe como parâmetros a proteína em ficheiro fasta, um ficheiro de output xml e a base de dados a utilizar """
        self.__file_fasta = file_fasta     #("__" antes, fica privado)
        self.__file_xml = file_xml
        self.__db = db
        
    def blast(self,TRESH):
        """faz o blast"""
        try:
            blast_records = SeqIO.parse(self.__file_fasta, "fasta")  
            save_file = open(self.__file_xml, "w")      #abre um ficheiro para posteriormente guardar os resultados em xml
            for blast_record in blast_records:
                result_handle = NCBIWWW.qblast("blastp", self.__db, blast_record.format("fasta"))
                save_file.write(result_handle.read())
            save_file.close()
            blast_records.close()
            
            
            file=open("Resultados_Blast.txt", "w")
            result_handle=open(str(self.file_xml))
            blast_records=NCBIXML.parse(result_handle)
            E_VALUE_TRESH = TRESH
            for blast_record in blast_records:
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        if hsp.expect < E_VALUE_TRESH:
#                            print('****Alignment****')
                            file.writelines('\n ****Alignment**** \n')
#                            print('sequence:',alignment.title)
                            file.writelines('\n sequence:'+ alignment.title)
#                            print('length:',alignment.length)
                            file.writelines('\n length:'+ str(alignment.length))
#                            print('e value:', hsp.expect)
                            file.writelines('\n e value:'+ str(hsp.expect) + '\n')
#                            print(hsp.query[0:75] + '...')
                            file.writelines(hsp.query[0:75] + '...' + '\n')
#                            print(hsp.match[0:75] + '...')
                            file.writelines(hsp.match[0:75] + '...' + '\n')
#                            print(hsp.sbjct[0:75] + '...')
                            file.writelines(hsp.sbjct[0:75] + '...' + '\n')
            file.close()
                                        
        except:
            print("Erro na configuração do Blast")
        

        

                    
        

