import html
from flask import Blueprint, redirect, render_template, request, url_for
from apps.api.api_table_alogrithms import *
from flask import current_app as app

# Blueprint Configuration
set_table_bp = Blueprint("set_table_bp", __name__, template_folder="templates", static_folder="static")


# call set table to 
# - free table if necessary
# - get nearby table if requested
# - get random table if requested
# - get random table if method initially "None"
@set_table_bp.route("/set-table-again/<company>/<int:old_table_number>", methods=["GET"])
def set_table_page(company, old_table_number):
    """
    Route for setting a specific table.
    :param company: Selected company from ready_for_table_bp
    :param table_number: Assigned table number
    :return: HTML template for setting the table
    """
    # put method into variable
    method = request.args.get('method', 'random')  # default to 'new' if method is not provided


    # First: if all tables have been judged return done page
    if(no_more_tables(app, company=company)):
        return render_template("company_done_page.html", company=html.unescape(company))
    
    # Second: Free the old table if this is not the first call to set-table
    # if we are not calling set-table for the first time, old_table_number should have a value
    # and we need to free the old table so that someone else can use it
    if(old_table_number != 0):
        free_table(app, table_number=old_table_number)
    
    # Third: Get the new table
    # You need to account for
    # - The complete table list and every table's availability, only "True" (available) tables valid
    # - Cross referenced with the specific company's table list
    # - Cross reference to not include whatever is in the blocked list (The blocked list is just there in case 
    #   someone really doesn't want a table and we want to include that in our decision for whatever reason)
    # You will also get a table in different ways, specified by method
        # method = nearby --> find the table that qualifies and is the closest to the old_table
        # method = random --> find the table that qualifies and is randomized from the qualifying list

    table_number = old_table_number
    if (method == "random"):
        table_number = get_random_qualifying_table(app, company=company)
    if (method == "nearby"):
        table_number = get_nearby_qualifying_table(app, company=company, blocked_list=[])

    if (table_number == -1):
        return render_template("tables_full_page.html", company=html.unescape(company), table_number=table_number)
    
    return render_template("set_table_page.html", company=html.unescape(company), table_number=table_number)
    


@set_table_bp.route("/set-table/<company>/<int:table_number>", methods=["POST"])
def process_set_table(company, table_number):
    """
    Route to process setting the table.
    If the user clicks 'yes', redirect to the TODO page.
    :param company: Selected company from ready_for_table_bp
    :param table_number: Assigned table number
    :return: Redirect to the TODO page or stay on the set table page
    """
    user_response = request.form.get("response", "").lower()

    if user_response == "yes":
        return redirect(url_for("at_table_bp.at_table_page", company=html.unescape(company), table_number=table_number))
    else:
        return redirect(url_for("ready_for_table_bp.ask_ready_question", company=html.unescape(company)))
    


