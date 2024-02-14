"""Backend functionality for initializing all csv data specific to our hackathon."""

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
def init_categories_to_table(app: Flask) -> dict:
    # Initialize an empty list to store the list of possible categories
    tables_to_category = {}

    # Read CSV file and populate list
    with open(app.config["TABLES_TO_CATEGORY_FILEPATH"], newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            category = row[0]
            tables = row[1].split(',')
            tables_to_category[category] = tables

    print(tables_to_category)
    return tables_to_category


def init_availability(app: Flask) -> dict:
    number_tables = len(app.tables)                     # find number of tables
    return [True] * number_tables                      # return all false array 


