import csv

def csv_to_matrix(filename, delimiter):
   
    with open(filename, newline='') as csvfile:
        csv_import = csv.reader(csvfile, delimiter=delimiter)
        csv_list = []
        for row in csv_import:
            
            csv_list.append((list(map(int, row))))

    return csv_list

    
