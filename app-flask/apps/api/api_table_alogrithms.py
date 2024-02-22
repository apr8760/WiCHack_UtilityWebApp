"""Holds all backend functions used to get the right table"""

import html
import random
from flask import Flask

def get_random_qualifying_table(app: Flask, category):
    """
    Function to get a random available table for the given category.
    """
    qualifying_tables = []

    for table in app.category_done_dicts[category]:
            if(app.available_tables[int(table)] & (app.category_done_dicts[category][table] == False)):
                qualifying_tables.append(int(table))

    # if qualifying tables list is not empty return random, else return None
    if(qualifying_tables):
        random_table = random.choice(qualifying_tables)
        return random_table
    else:
        return -1
    

# TODO: Big todo, this is just a copy of random for now
def get_nearby_qualifying_table(app: Flask, category, blocked_list):
    """
    Function to get a random available table for the given category.
    """
    qualifying_tables = []

    for table in app.category_done_dicts[category]:
            if(app.available_tables[int(table)] & (app.category_done_dicts[category][table] == False)):
                qualifying_tables.append(int(table))

    # if qualifying tables list is not empty return random, else return None
    if(qualifying_tables):
        random_table = random.choice(qualifying_tables)
        return random_table
    else:
        return -1
     

def get_free_table(app: Flask, category, blocked_list):
    """
    Function to get an available table for the given category.
    """
    category = html.unescape(category)

    if(any(x == False for x in app.category_done_dicts[category].values())):
        for table in app.category_done_dicts[category]:
                if(app.available_tables[int(table)] & (app.category_done_dicts[category][table] == False) & (table not in blocked_list)):
                    return int(table)
        return None
    else:
        return -1
    

def get_todo_tables(app: Flask, category):
    """Return list of all possible tables for this category that are NOT done"""

    list_all_possible_tables = []
    for table in app.category_done_dicts[category]:
                # False means the table is NOT done and should be added to list
                if(app.category_done_dicts[category][table] == False):
                    list_all_possible_tables.append(table)
    
    return list_all_possible_tables

def no_more_tables(app:Flask, category):
    """Return true if there are no more tables for this category to judge
        And false if there are still tables.
    """
    return (len(get_todo_tables(app, category)) == 0)


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


def make_done(app:Flask, category, table_number):
    """Set table to done for this category"""

    assert(0 <= table_number < len(app.available_tables))
    # set this table to done (ie true in done dictionary for this category):
    (app.category_done_dicts[category])[table_number] = True
