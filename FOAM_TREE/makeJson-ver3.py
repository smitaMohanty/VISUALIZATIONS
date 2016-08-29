# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:18:11 2016

@author: smita.mohanty
"""
import pandas as pd
import json
df=pd.read_excel('./foam_tree_excel.xlsx',sheetname='Sheet1')
path={}
targets={}
x=0
for i in df['Pathways ']:
    if i not in path.keys():
       path[i]=[]
    path[i].append(df.loc[x]['Targets '])
    x+=1
x=0
for i in df['Targets ']:
    if i not in targets.keys():
       targets[i]=[]    
    if {'label':df.loc[x]['Drugs'],'weight':1} not in targets[i]:
       targets[i].append({'label':df.loc[x]['Drugs'],'weight':1})
    x+=1
x=0
tree={}
tree['groups']=[]
    
for  i in path.keys():
    tree['groups'].append({'label':i,'weight':len(path[i]),'groups':[]})
    
    for j in path[i]:
        
        if j in targets.keys():
           print (targets[j]) 
           tree['groups'][x]['groups'].append({'label':j,'weight':len(targets[j]),'groups':targets[j]})
    x+=1    

fil=open('pathways-targets-drugs-foam-tree.js','w')
fil.write(json.dumps(tree))
fil.close()    