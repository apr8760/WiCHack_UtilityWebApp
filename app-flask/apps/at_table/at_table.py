from flask import Blueprint, redirect, render_template, request, url_for
from flask import current_app as app

# Blueprint Configuration
at_table_bp = Blueprint("at_table_bp", __name__, template_folder="templates", static_folder="static")

@at_table_bp.route("/at-table/<company>/<int:table_number>")
def at_table_page(company, table_number):
    """
    Route for showing "at table" page.
    This is where the user can report when they are AT THE TABLE

    :param company: Selected company from ready_for_table_bp
    :param table_number: Assigned table number
    :return: HTML template for setting the table
    """
    return render_template("at_table_page.html", company=company, table_number=table_number)




