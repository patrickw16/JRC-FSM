import os
import pandas as pd

# Specify the folder containing the .csv files
folder_path = 'results'

# Initialize an empty list to store DataFrames
dataframes = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Read the .csv file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Append the DataFrame to the list
        dataframes.append(df)

# Combine all DataFrames into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined DataFrame to a new .csv file
output_path = os.path.join(folder_path, 'CC_human_driver_cut_in.csv')
combined_df.to_csv(output_path, index=False)

print(f"Combined .csv files saved to {output_path}")