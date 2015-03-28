import handle_nulls
import pandas as pd

filename="slaves_dataset.csv"
dataset=pd.read_csv(filename,sep='\t',dtype=str,keep_default_na=False)
handle_nulls.handle(dataset)

