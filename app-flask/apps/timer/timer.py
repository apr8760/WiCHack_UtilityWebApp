"""General page routes."""
from flask import Blueprint, render_template
from flask import current_app as app
from apps.api.api_table_alogrithms import *


# Blueprint Configuration
timer_bp = Blueprint("timer_bp", __name__, template_folder="templates", static_folder="static")

"""Take in list of chosen categories and process accordingly"""
@timer_bp.route("/timer/<company>/<int:table_number>", methods=["POST"])
def timer_page(company, table_number):
    """
    Serve `Timer` page template.

    :returns: str
    """
    return render_template("timer_page.html", company=company, table_number=table_number)