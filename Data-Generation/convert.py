#!/usr/bin/env python
import sys
import os
from lxml import etree as et
import csv
import pandas as pd

out_folder = str(sys.argv[1])
in_folder = str(sys.argv[1])
extension = "rrd.xml"
nodeName = str(sys.argv[2])

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
icount=0
for file in os.listdir(in_folder):
    row=[]
    if file.endswith(extension):
        column,date,time,data=parse(in_folder+file)
        if(first):
            df["Date"] = date
            df["Time"] = time
            first=False
        df[column]=data
	icount = df[column].count()

mylist=[]
for x in range(0,icount):
	mylist.append(nodeName)

df["node"] = mylist
df.to_csv(nodeName+".csv")
print df


