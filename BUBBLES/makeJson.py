# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 17:40:33 2016

@author: smita.mohanty
"""
import sys
import json
import pandas as pd
dct={}
dct['name']='Targets'
dct['children']=[]

df=pd.read_excel('SNPs_auto_mod.xlsx',sheetname='immunome')
tmp={}
for i in df.index:
    if df.loc[i]['Gene'] not in tmp.keys():
       tmp[df.loc[i]['Gene']]={}
    if df.loc[i]['Disease'] not in tmp[df.loc[i]['Gene']].keys():
       tmp[df.loc[i]['Gene']][df.loc[i]['Disease']]={}
    if df.loc[i]['Type'] not in tmp[df.loc[i]['Gene']][df.loc[i]['Disease']]:
       tmp[df.loc[i]['Gene']][df.loc[i]['Disease']][df.loc[i]['Type']]=0 
    tmp[df.loc[i]['Gene']][df.loc[i]['Disease']][df.loc[i]['Type']]+=1   
       


for k in tmp.keys():
    #print (k,tmp[k])  
    lst=[]
    for j in tmp[k].keys():
        Nlst=[]
        for l in tmp[k][j].keys():
            Nlst.append({'name':l,'size':tmp[k][j][l]})
        lst.append({'name':j,'children':Nlst})    
    dct['children'].append({'name':k,'children':lst})

for k in dct.keys():
    print (k,dct[k])       
fil=open('gene-disease-type.json','w')
fil.write(json.dumps(dct))
fil.close()       
       