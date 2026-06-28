import os
import csv

def remove_column_from_csv_in_directory(directory, column_name):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            
            temp_output_file = file_path + ".tmp"
            
            with open(file_path, mode='r', newline='', encoding='utf-8') as infile:
                reader = csv.DictReader(infile)
                
                if column_name in reader.fieldnames:
                    fieldnames = [field for field in reader.fieldnames if field != column_name]
                    
                    with open(temp_output_file, mode='w', newline='', encoding='utf-8') as outfile:
                        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                        writer.writeheader()
                        for row in reader:
                            del row[column_name]
                            writer.writerow(row)
                    
                    os.replace(temp_output_file, file_path)
                    print(f"Coluna '{column_name}' removida do arquivo: {filename}")
                else:
                    print(f"A coluna '{column_name}' não existe no arquivo: {filename}. Nenhuma alteração feita.")

directory_path = 'Dados/'
coluna_para_remover = 'Endereço de e-mail'

remove_column_from_csv_in_directory(directory_path, coluna_para_remover)
