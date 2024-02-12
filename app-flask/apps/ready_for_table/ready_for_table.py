"""Ready of table page routes."""
from flask import Blueprint, request
from flask import current_app as app
from flask import Flask, render_template, redirect, url_for


# Blueprint Configuration
ready_for_table_bp = Blueprint("ready_for_table_bp", __name__, template_folder="templates", static_folder="static")

@ready_for_table_bp.route("/ready-question-<company>")
def ask_ready_question(company):
    """
    Route for the page asking if the user is ready for a table.
    :param company: Selected company from pick_company_bp
    :return: HTML template
    """
    return render_template("ready_for_table_page.html", company=company)

@ready_for_table_bp.route("/ready-question-<company>", methods=["POST"])
def process_ready_response(company):
    """
    Route to process the user's response to being ready for a table.
    If the user clicks 'yes', get an available table and redirect to the set table page.
    :param company: Selected company from pick_company_bp
    :return: Redirect to the set table page or stay on the ready question page
    """
    user_response = request.form.get("response", "").lower()

    if user_response == "yes":
        # Call a backend function to get available table number for the company
        table_number = get_available_table()
        return redirect(url_for("set_table_bp.set_table_page", company=company, table_number=table_number))
    else:
        return redirect(url_for("ready_for_table_bp.ask_ready_question", company=company))


def get_available_table():
    """
    Function to get an available table for the given company.
    """
    for index, value in enumerate(app.available_tables):
        if value:
            return index + 1
    
    return None

