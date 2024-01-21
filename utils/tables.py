#
# Class to hold tables data from csv
#
import csv


class Tables:
    def __init__(self):
        self.__num_tables = 16  # Private variable
        # Initialize an empty adjacency list for nodes 1-# of tables
        self.__adj_list = {node: [] for node in range(1, self.__num_tables+1)}

    def create_adjacency_list_from_csv(self, file_path):
        # Read the CSV file
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                node = int(row['Node'])
                neighbors = list(map(int, row['Neighbors'].split(',')))
                self.__adj_list[node] = neighbors

    def initialize_tables(self):
        self.create_adjacency_list_from_csv("flask-api/tables_adj_list.csv")
        # Printing the adjacency list created from the CSV
        print("Adjacency List from CSV:")
        for node, neighbors in self.__adj_list.items():
            print(f"Node {node}: {neighbors}")