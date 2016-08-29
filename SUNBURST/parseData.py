# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:59:02 2016

@author: smita.mohanty
"""

import pandas as pd
import glob
import re
import numpy as np
import json
import math
def read_fil(dirpath):
    newdf=pd.DataFrame()
    for i in glob.glob(dirpath+'/*'):
        #print (i)
        nam=i.split('_') 
        nam[-3]=re.sub('.*ENRICH.','',nam[-3])
        print(nam[-3])
        df=pd.read_csv(i,index_col=0,header=0)
        newdf=pd.merge(newdf,df['p-value'].to_frame(name=nam[-3]),right_index=True,left_index=True,how='outer')
    return newdf    
def get_curated (filnam,lst):
    df=pd.read_excel(filnam,index_col=0,header=0)
    dct={}
    dct['name']='All Pathways ('+str(len(lst))+')'
    dct['children']=[]
    tst={}
    for i in df.index:
         #print ((str(i)+'|'+df.loc[i][0]).replace('| ','|'))
         if (str(i)+'|'+df.loc[i][0]).replace('| ','|') in lst.keys():
            if df.loc[i][1] not in tst.keys():
                tst[df.loc[i][1]]=[]
            tst[df.loc[i][1]].append({"name":df.loc[i][0],"size":-math.log(lst[(str(i)+'|'+df.loc[i][0]).replace('| ','|')])})    
    print(tst)
    for i in tst.keys():
        dct['children'].append({'name':i,'children':tst[i]})
    return dct    
    
    
def comapre(df,lst):
    dct={}
    dct['name']="All Pathways ()"
    dct['children']=[]
    nodes=[]
    for i in df.index.values:
        pathids=i.split('|')
        k=','.join(np.sort(list(df.loc[i].dropna().to_dict().keys())))   
        v=np.max(-np.log10((np.array(list(df.loc[i].dropna().to_dict().values()))).astype(float)))
        if v>=2.0 and pathids[0] in lst:
           if k not in nodes:
              nodes.append(k)
              dct['children'].append({'name':k,'children':[]})
           for l in dct['children']:
              if l['name']==k:
                 l['children'].append({"name":pathids[1],"size":v})
    return dct, nodes            