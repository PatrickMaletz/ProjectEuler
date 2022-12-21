import csv

def csv_to_matrix(filename, delimiter):
   
    with open(filename, newline='') as csvfile:
        csv_import = csv.reader(csvfile, delimiter=delimiter)
        csv_list = []
        for row in csv_import:
            
            csv_list.append((list(map(int, row))))

    return csv_list

    
class node():

    def __init__(self, left = None, right = None, data = None) -> None:
        super().__init__()
        self.left = left
        self.right = right
        self.data = data
    
    def add(self,node, left):
        if left:
            self.left = node
        else:
            self.right = node
        return



     