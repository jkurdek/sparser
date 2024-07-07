import pandas as pd


filenames = ['a.parquet', 'b.parquet', 'c.parquet', 'd.parquet']

combined_df = pd.DataFrame()

for filename in filenames:
    df = pd.read_parquet(filename)
    
    combined_df = pd.concat([combined_df, df], ignore_index=True)

combined_df.to_json('output_file.json', orient='records', lines=True)

print("Conversion to JSON completed successfully!")
