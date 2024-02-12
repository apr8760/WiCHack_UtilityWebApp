"""Read placeholder data for demo purposes."""

import json
import csv
from flask import Flask



"""Read in table data (ie. table numbers and which tables associate to each other)"""
def init_tables(app: Flask) -> dict:

    # Initialize an empty dictionary to store neighbors for each table
    table_neighbors_dict = {}

    # Read CSV file and populate the dictionary
    with open(app.config["TABLE_PLACEMENTS_DATA_FILEPATH"], newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            table = int(row[0])
            neighbors_str = row[1].split(',')
            neighbors = [int(neighbor) for neighbor in neighbors_str]
            table_neighbors_dict[table] = neighbors

    print(table_neighbors_dict)
    return table_neighbors_dict


def init_categories_to_company(app: Flask) -> dict:

    # Initialize an empty list to store the list of possible categories
    categories_to_company = {}

    # Read CSV file and populate list
    with open(app.config["CATEGORIES_TO_COMPANY_FILEPATH"], newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            company = row[0]
            categories = row[1].split(',')
            categories_to_company[company] = categories

    print(categories_to_company)
    return categories_to_company


def init_categories_to_table(app: Flask) -> dict:

    # Initialize an empty list to store the list of possible categories
    categories_to_table_dict = {}

    # Read CSV file and populate list
    with open(app.config["CATEGORIES_TO_TABLE_FILEPATH"], newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            table = row[0]
            categories = row[1].split(',')
            categories_to_table_dict[table] = categories

    print(categories_to_table_dict)
    return categories_to_table_dict


## TODO: intialize the occupied_booleans to all false (bascially return dict (key: table, value: T/F) with all false for tables)

