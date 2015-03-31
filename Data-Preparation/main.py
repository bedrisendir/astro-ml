import handle_nulls
import scientific_to_float
import remove_constant
import pandas as pd
import writetoFile
import stdev_threshold

filename="node43.csv"
dataset=pd.read_csv(filename,dtype=str,keep_default_na=False)
dataset.drop(dataset.columns[0], axis=1)
print len(list(dataset.columns.values))

del dataset["Unnamed: 0"]
dataset=handle_nulls.handle(dataset)
print len(list(dataset.columns.values))
writetoFile.write(dataset,"1.csv")

#print dataset["Date"]
dataset=scientific_to_float.handle(dataset)
print len(list(dataset.columns.values))

#print dataset["Date"]
dataset=remove_constant.remove_constant(dataset)
print len(list(dataset.columns.values))



#print dataset["Date"]
dataset=stdev_threshold.stdev(dataset)
print len(list(dataset.columns.values)) 

writetoFile.write(dataset,"2.csv")
