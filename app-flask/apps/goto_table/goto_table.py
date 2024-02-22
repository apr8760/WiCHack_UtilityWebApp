import html
from flask import Blueprint, redirect, render_template, request, url_for
from flask import current_app as app
from apps.api.api_table_alogrithms import *

# Blueprint Configuration
goto_table_bp = Blueprint("goto_table_bp", __name__, template_folder="templates", static_folder="static")

@goto_table_bp.route("/goto-table/<category>/<int:table_number>")
def goto_table_page(category, table_number):
    """
    Route for showing "goto table" page. They will X number of seconds to 
    get to the selected table before they lose that table.
    Then the user can report when they are AT THE TABLE

    :param category: Selected category from ready_for_table_bp
    :param table_number: Assigned table number
    :return: HTML template for setting the table
    """
    return render_template("goto_table_page.html", category=category, table_number=table_number)


# call set table to 
# - free table if necessary
# - get nearby table if requested
# - get random table if requested
# - get random table if method initially "None"
@goto_table_bp.route("/set-table/<category>/<int:old_table_number>", methods=["GET"])
def set_table(category, old_table_number):
    """
    Route for setting a specific table.
    :param category: Selected category from ready_for_table_bp
    :param table_number: Assigned table number
    :return: HTML template for setting the table
    """
    # put method into variable
    method = request.args.get('method', 'random')  # default to 'new' if method is not provided


    # First: if all tables have been judged return done page
    if(no_more_tables(app, category=category)):
        return render_template("category_done_page.html", category=html.unescape(category))
    
    # Second: Free the old table if this is not the first call to set-table
    # if we are not calling set-table for the first time, old_table_number should have a value
    # and we need to free the old table so that someone else can use it
    if(old_table_number != 0):
        free_table(app, table_number=old_table_number)
    
    # Third: Get the new table
    # You need to account for
    # - The complete table list and every table's availability, only "True" (available) tables valid
    # - Cross referenced with the specific category's table list
    # - Cross reference to not include whatever is in the blocked list (The blocked list is just there in case 
    #   someone really doesn't want a table and we want to include that in our decision for whatever reason)
    # You will also get a table in different ways, specified by method
        # method = nearby --> find the table that qualifies and is the closest to the old_table
        # method = random --> find the table that qualifies and is randomized from the qualifying list

    table_number = old_table_number
    if (method == "random"):
        table_number = get_random_qualifying_table(app, category=category)
    if (method == "nearby"):
        table_number = get_nearby_qualifying_table(app, category=category, blocked_list=[])

    if (table_number == -1):
        return render_template("tables_full_page.html", category=html.unescape(category), table_number=table_number)
    
    return render_template("goto_table_page.html", category=html.unescape(category), table_number=table_number)