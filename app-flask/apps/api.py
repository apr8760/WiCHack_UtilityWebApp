"""Read placeholder data for demo purposes."""

import csv
from flask import Flask



"""Read in table data (i.e., table numbers and which tables associate to each other)"""
def init_tables(app: Flask) -> list:
    # Initialize an empty list to store neighbors for each table
    table_neighbors_list = []

    # Read CSV file and populate the list
    with open(app.config["TABLE_PLACEMENTS_DATA_FILEPATH"], newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            neighbors_str = row[1].split(',')
            neighbors = [int(neighbor) for neighbor in neighbors_str]
            table_neighbors_list.append(neighbors)

    print(table_neighbors_list)
    return table_neighbors_list


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


"""Initialize categories to table mapping"""
def init_categories_to_table(app: Flask) -> list:
    # Initialize an empty list to store the list of possible categories
    categories_to_table_list = []

    # Read CSV file and populate the list
    with open(app.config["CATEGORIES_TO_TABLE_FILEPATH"], newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            categories = row[1].split(',')
            categories_to_table_list.append(categories)

    print(categories_to_table_list)
    return categories_to_table_list


def init_availability(app: Flask) -> dict:
    number_tables = len(app.tables)                     # find number of tables
    return [True] * number_tables                      # return all false array 



