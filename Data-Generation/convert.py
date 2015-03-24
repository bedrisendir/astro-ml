#!/usr/bin/env python
import sys
import os
from lxml import etree as et
import csv
import pandas as pd

out_folder = str(sys.argv[1])
in_folder = str(sys.argv[1])
extension = "rrd.xml"

def parse(file):
    print file
    time=[]
    data=[]
    date=[]
    parser = et.XMLParser(remove_comments=False)
    tree = et.parse(file,parser=parser)
    ctr=0
    val=tree.iter("database").next()
    for row in val:
        if isinstance(row, et._Comment):
            stamp=row.text.split('/')[0].strip().split(' ')
            time.append(stamp[1])
            date.append(stamp[0])
        else:            
            for elem in row.iter(tag="v"):
                data.append(elem.text)
    return file.split('/')[-1].split(".rrd.xml")[0],date,time,data        

###########
first = True
df= pd.DataFrame()
for file in os.listdir(in_folder):
    row=[]
    if file.endswith(extension):
        wfile = open("alldata",'w+')
        write = csv.writer(wfile)
        column,date,time,data=parse(in_folder+file)
        if(first):
            df["Date"] = date
            df["Time"] = time
            first=False
        df[column]=data
df.to_csv("test.csv")
print df
