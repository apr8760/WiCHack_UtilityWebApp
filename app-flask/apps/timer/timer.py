"""General page routes."""
from flask import Blueprint
from flask import current_app as app


# Blueprint Configuration
timer_bp = Blueprint("timer_bp", __name__, template_folder="templates", static_folder="static")

"""Take in list of chosen categories and process accordingly"""
@timer_bp.route("/<int_list:values>", methods=["GET"])
def timer(values) -> str:
    """
    Serve `Timer` page template.

    :returns: str
    """
    # products = fetch_products(app)
    print("hello from timer")
    return values