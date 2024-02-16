"""Ready of table page routes."""
import html
from flask import Blueprint, request
from flask import current_app as app
from apps.api.api_table_alogrithms import *
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
    return render_template("ready_for_table_page.html", company=html.unescape(company))

##### TODO find a better way to rest tables when done with table than calling a seperate "again" function
#### but for now this is just how it needs to be
@ready_for_table_bp.route("/ready-question-<company>-<int:table_number>")
def ask_ready_question_again(company, table_number):
    """
    Route for the page asking if the user is ready for a table.
    :param company: Selected company from pick_company_bp
    :return: HTML template
    """

    # TODO: Delete debug print
    print("BEFORE RESET------------------------------------------------")
    print("Dictionary for all tables availability:")
    print(app.available_tables)
    print("Done list for this company now:")
    print("done lists:")
    print(app.company_done_lists)
    print("company:")
    print(company)
    print(app.company_done_lists[company])

    free_table(app, table_number=table_number)
    make_done(app, company=company, table_number=table_number)
    print("-------------------------------------------------------------")

    print("AFTER RESET------------------------------------------------")
    # TODO: Delete debug print
    print("Dictionary for all tables availability:")
    print(app.available_tables)
    print("Done list for this company now:")
    print("done lists:")
    print(app.company_done_lists)
    print("company:")
    print(company)
    print(app.company_done_lists[company])
    print("-----------------------------------------------------------")
    
    return render_template("ready_for_table_page.html", company=html.unescape(company))

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
        return redirect(url_for("set_table_bp.set_table_page", company=html.unescape(company), old_table_number=0))
    else:
        return redirect(url_for("ready_for_table_bp.ask_ready_question", company=html.unescape(company)))




