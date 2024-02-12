#
# Class to hold tables data from csv in local data structures
#
import csv


class Tables:
    def __init__(self):
        self.__num_tables = 16  
        # Initialize an empty adjacency list for nodes 1-# of tables
        self.__adj_list = {node: [] for node in range(1, self.__num_tables+1)}
        self.__boolean_array = []

    # Create adjacency list of tables and their neighbors from CSV
    def create_neighbor_list(self):
        # Read the CSV file
        file_path = "utils\table_placements.csv"
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                node = int(row['Table'])
                neighbors = list(map(int, row['Neighbors'].split(',')))
                self.__adj_list[node] = neighbors


    # probs won't use 
    # create array list of tables and whether they are occupied or not from csv
    def create_occupied_array(self):
        file_path = "utils/table_occupied_booleans.csv"
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                node = int(row['Table'])
                self.__boolean_array[node] = row['Occupied_Boolean']