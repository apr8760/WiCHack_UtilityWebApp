"""Holds all backend functions used to get the right table"""

import html
import random
from flask import Flask

def get_random_qualifying_table(app: Flask, company):
    """
    Function to get a random available table for the given company.
    """
    qualifying_tables = []

    for table in app.company_done_lists[company]:
            if(app.available_tables[int(table)] & (app.company_done_lists[company][table] == False)):
                qualifying_tables.append(int(table))

    # if qualifying tables list is not empty return random, else return None
    if(qualifying_tables):
        random_table = random.choice(qualifying_tables)
        return random_table
    else:
        return -1
    

# TODO: Big todo, this is just a copy of random for now
def get_nearby_qualifying_table(app: Flask, company, blocked_list):
    """
    Function to get a random available table for the given company.
    """
    qualifying_tables = []

    for table in app.company_done_lists[company]:
            if(app.available_tables[int(table)] & (app.company_done_lists[company][table] == False)):
                qualifying_tables.append(int(table))

    # if qualifying tables list is not empty return random, else return None
    if(qualifying_tables):
        random_table = random.choice(qualifying_tables)
        return random_table
    else:
        return -1
     

def get_free_table(app: Flask, company, blocked_list):
    """
    Function to get an available table for the given company.
    """
    company = html.unescape(company)
    # get list of categories associated with this company
    # categories_for_this_company = app.categories_to_company[company]

    # all_tables_for_this_company = list(set([table for category in categories_for_this_company 
                                  #  for table in app.tables_to_category[category]]))

    if(any(x == False for x in app.company_done_lists[company].values())):
        for table in app.company_done_lists[company]:
                if(app.available_tables[int(table)] & (app.company_done_lists[company][table] == False) & (table not in blocked_list)):
                    return int(table)
        return None
    else:
        return -1
    

def get_todo_tables(app: Flask, company):
    """Return list of all possible tables for this company that are NOT done"""

    list_all_possible_tables = []
    for table in app.company_done_lists[company]:
                # False means the table is NOT done and should be added to list
                if(app.company_done_lists[company][table] == False):
                    list_all_possible_tables.append(table)
    
    return list_all_possible_tables

def no_more_tables(app:Flask, company):
    """Return true if there are no more tables for this company to judge
        And false if there are still tables.
    """
    return (len(get_todo_tables(app, company)) == 0)


def take_table(app: Flask, table_number):
    """Set that table to false in available list"""

    assert(0 <= table_number < len(app.available_tables))
    app.available_tables[table_number] = False

    
def free_table(app:Flask, table_number):
    """Reset a table to available so that another judge can judge it"""

    print("Table number:")
    print(table_number)
    assert(0 <= table_number < len(app.available_tables))
    app.available_tables[table_number] = True


def make_done(app:Flask, company, table_number):
    """Set table to done for this company"""

    assert(0 <= table_number < len(app.available_tables))
    # set this table to done (ie true in done dictionary for this company):
    (app.company_done_lists[company])[table_number] = True
