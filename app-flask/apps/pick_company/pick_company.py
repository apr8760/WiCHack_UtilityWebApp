"""Category selection page routes."""
from flask import Blueprint, request, render_template, redirect, url_for
from flask import current_app as app


# Blueprint Configuration
pick_company_bp = Blueprint("pick_company_bp", __name__, template_folder="templates", static_folder="static")

@pick_company_bp.route("/")
def home_page():
    return render_template("pick_company_home.html")  # Update with your actual home template

@pick_company_bp.route("/", methods=["POST"])
def process_company_selection():
    """
    Route to process the user's company selection.
    If the user submits a selected company, redirect to the ready question page.
    :return: Redirect to the ready question page or stay on the home page
    """
    selected_company = request.form.get("selected_company")

    if selected_company:
        return redirect(url_for("ready_for_table_bp.ask_ready_question", company=selected_company))
    else:
        return redirect(url_for("pick_company_bp.home_page"))

# Assuming /ready-question-<company> is handled by ready_for_table_bp
# ...
