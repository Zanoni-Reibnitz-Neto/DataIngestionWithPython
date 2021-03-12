from pyarrow import parquet

table = parquet.read_table('taxi.parquet')

df = table.to_pandas()

print(df.dtypes)
print(df.head)
