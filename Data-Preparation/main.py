import handle_nulls
import scientific_to_float
import remove_constant
import pandas as pd
import writetoFile

filename="node43.csv"
dataset=pd.read_csv(filename,dtype=str,keep_default_na=False)
print len(list(dataset.columns.values))


dataset=handle_nulls.handle(dataset)
print len(list(dataset.columns.values))


dataset=scientific_to_float.handle(dataset)
print len(list(dataset.columns.values))


dataset=remove_constant.remove_constant(dataset)
print len(list(dataset.columns.values))
writetoFile.write(dataset)
