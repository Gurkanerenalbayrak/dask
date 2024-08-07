import dask.dataframe as dd


df = dd.read_csv("twitter_parsed_dataset.csv", dtype ={

    "oh_label": float,
    "id": str,
    "index": str,
    "Text": str,
    "Annotation": str    
})



#print(df.head())

df = df.repartition(npartitions=20)
print(f"{df.npartitions} partitions")



df.to_parquet("twitter_parsed_dataset.parquet")




