#
# Hold singleton class for local data instantiation 
# Instantiated only once, used for all devices
#
import csv


NUM_TABLES = 16

class SingletonLocalData:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonLocalData, cls).__new__(cls, *args, **kwargs)
            # Create boolean array for all tables, default to false
            cls._instance.boolean_array = [False for _ in range(NUM_TABLES)]
            # Create adjacency list of tables and their neighbors from CSV
            cls._instance.adjacency_list = {}
            file_path = r'C:\Users\ainsl\Google Drive\RIT\WiC\WiC_Projects\WiCHack_UtilityWebApp\app\utils\table_placements.csv'
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    node = int(row['Table'])
                    neighbors = list(map(int, row['Neighbors'].split(',')))
                    cls._instance.adjacency_list[node] = neighbors
            
            ### TO Delete debug print adjacency list
            for node, neighbors in cls._instance.adjacency_list.items():
                print(f"Node {node}: {neighbors}")

        return cls._instance

    def set_boolean_array(self, new_array):
        self.boolean_array = new_array

    def get_boolean_array(self):
        return self.boolean_array

    def set_adjacency_list(self, new_adjacency_list):
        self.adjacency_list = new_adjacency_list

    def get_adjacency_list(self):
        return self.adjacency_list
    
        
   
