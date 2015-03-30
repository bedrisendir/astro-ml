import handle_nulls
import scientific_to_float
import remove_constant
import pandas as pd

filename="slaves_dataset.csv"
dataset=pd.read_csv(filename,sep='\t',dtype=str,keep_default_na=False)

#scientific format
dataset=scientific_to_float(dataset)

#collect nodes columns to delete
dataset=handle_nulls.handle(dataset)

#remove constant
dataset=remove_constant(dataset)
