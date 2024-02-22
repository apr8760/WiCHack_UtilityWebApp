"""Ready of table page routes."""
import html
from flask import Blueprint, request
from flask import current_app as app
from apps.api.api_table_alogrithms import *
from flask import Flask, render_template, redirect, url_for


# Blueprint Configuration
ready_bp = Blueprint("ready_bp", __name__, template_folder="templates", static_folder="static")

@ready_bp.route("/ready-question-<category>")
def ask_ready_question(category):
    """
    Route for the page asking if the user is ready for a table.
    :param category: Selected category from pick_category_bp
    :return: HTML template
    """
    return render_template("ready_page.html", category=(category))


@ready_bp.route("/ready-question-<category>-<int:table_number>")
def ask_ready_question_again(category, table_number):
    """
    Route for the page asking if the user is ready for a table.
    :param category: Selected category from pick_category_bp
    :return: HTML template
    """

    free_table(app, table_number=table_number)
    make_done(app, category=category, table_number=table_number)
    
    return render_template("ready_page.html", category=(category))

@ready_bp.route("/ready-question-<category>", methods=["POST"])
def process_ready_response(category):
    """
    Route to process the user's response to being ready for a table.
    If the user clicks 'yes', get an available table and redirect to the set table page.
    :param category: Selected category from pick_category_bp
    :return: Redirect to the set table page or stay on the ready question page
    """
    user_response = request.form.get("response", "").lower()

    if user_response == "yes":
        return redirect(url_for("goto_table_bp.set_table", category=(category), old_table_number=0))
    else:
        return redirect(url_for("ready_bp.ask_ready_question", category=(category)))




