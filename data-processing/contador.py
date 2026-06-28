# Adapted script to analyze all columns starting from the third column and save the results in a .txt file

import pandas as pd
from collections import Counter

def count_elements_in_all_columns(csv_file):
    df = pd.read_csv(csv_file)
    column_names = df.columns[2:]
    result = []
    
    for column_name in column_names:
        column_data = df[column_name]
        element_counts = Counter(column_data)
        result.append(f"Coluna: {column_name}\n")
        for element, count in element_counts.items():
            result.append(f"'{element}': {count} vezes\n")
        result.append("\n")
    
    return result

csv_file = 'dataset.csv'
output_file = 'column_counts_result.txt'

counts_result = count_elements_in_all_columns(csv_file)

with open(output_file, 'w') as f:
    f.writelines(counts_result)

output_file
