from flask import Blueprint, redirect, render_template, request, url_for
from flask import current_app as app

# Blueprint Configuration
set_table_bp = Blueprint("set_table_bp", __name__, template_folder="templates", static_folder="static")

@set_table_bp.route("/set-table/<company>/<int:table_number>")
def set_table_page(company, table_number):
    """
    Route for setting a specific table.
    :param company: Selected company from ready_for_table_bp
    :param table_number: Assigned table number
    :return: HTML template for setting the table
    """
    return render_template("set_table_page.html", company=company, table_number=table_number)

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
        if set_chosen_table(table_number) == 0:
            result = f"Table {table_number} has been set for {company}."

        else:
            result = f"Table {table_number} cannot be set for {company}."
    else:
        result = f"You chose not to set table {table_number} for {company}."

    # TODO uncomment line bellow once done debugging with loop back to ready for table page
    # return render_template("set_table_page.html", company=company, table_number=table_number, result=result)
    return redirect(url_for("ready_for_table_bp.ask_ready_question", company=company))

def set_chosen_table(table_number):
    """Set that table to false in available list"""

    if 0 <= table_number < len(app.available_tables):
        app.available_tables[table_number - 1] = False
        return 0
    else:
        print("Invalid index.")
        return 1


