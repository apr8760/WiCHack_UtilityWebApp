"""Holds all backend functions used to get the right table"""

from flask import Flask


def get_available_table(app: Flask):
    """
    Function to get an available table for the given company.
    """
    for index, value in enumerate(app.available_tables):
        if value:
            return index + 1
    
    return None


