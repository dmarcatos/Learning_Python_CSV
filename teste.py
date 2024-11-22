import csv

print("CSV module imported successfully!")

# Abre o arquivo CSV
with open ('exemple.csv', mode='r') as file:
    # Cria um objeto CSV reader
    csv_reader = csv.reader(file)
    
    # Pula a linha do cabeçalho se tiver um
    next(csv_reader, None)
    
    # Itera cada linha do arquivo CSV
    for row in csv_reader:
        print(row)
    
