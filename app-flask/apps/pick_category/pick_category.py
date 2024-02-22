"""Category selection page routes."""
from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from flask import current_app as app


# Blueprint Configuration
pick_category_bp = Blueprint("pick_category_bp", __name__, template_folder="templates", static_folder="static")

# Assuming app.categories_to_company is a dictionary containing categories for each company
# Example: app.categories_to_company = {'WiC': ['Category1', 'Category2'], 'Fidelity': ['Category3', 'Category4']}


@pick_category_bp.route("/", methods=["GET", "POST"])
def category_selection():
    selected_company = request.form.get("selected_company")
    selected_category = request.form.get("selected_category")

    categories = app.categories_to_company.get(selected_company, []) if selected_company else []

    if request.method == "POST" and selected_company and not selected_category:
        return render_template("pick_category.html", companies=app.categories_to_company.keys(),
                           selected_company=selected_company, categories=categories)

    # if request.method == "POST" and selected_company and selected_category:
    #     return redirect(url_for("ready_bp.ask_ready_question", category=selected_category))
    
    return render_template("pick_category.html", companies=app.categories_to_company.keys(),
                           selected_company=selected_company, categories=categories)


















# @pick_category_bp.route("/", methods=["GET", "POST"])
# def company_selection():
#     selected_company = request.form.get("selected_company")

#     if request.method == "POST" and selected_company:
#         return redirect(url_for("pick_category_bp.category_selection", company=selected_company))

#     return render_template("pick_company.html", companies=app.categories_to_company.keys(), selected_company=selected_company)

# @pick_category_bp.route("/<company>", methods=["GET"])
# def category_selection(company):
#     categories = app.categories_to_company.get(company, [])
#     return render_template("pick_company.html", company=company, categories=categories, selected_company=company)
















































































# @pick_category_bp.route("/")
# def home_page():
#     return render_template("pick_home.html")  # Update with your actual home template


# @pick_category_bp.route("/", methods=["POST"])
# def process_company_selection():
#     """
#     Route to process the user's company selection.
#     If the user submits a selected company, redirect to the ready question page.
#     :return: Redirect to the ready question page or stay on the home page
#     """
#     selected_company = request.form.get("selected_company")

#     if selected_company:
#         return redirect(url_for("pick_category_bp.category_selection", company=selected_company))
#     else:
#         return redirect(url_for("pick_category_bp.home_page"))
    

# @pick_category_bp.route("/", methods=["POST"])
# def process_category_selection():
#     """
#     Route to process the user's category selection.
#     If the user submits a selected category, redirect to the ready question page.
#     :return: Redirect to the ready question page or stay on the home page
#     """
#     selected_category = request.form.get("selected_category")

#     if selected_category:
#         return redirect(url_for("ready_bp.ready_page", category=selected_category))
#     else:
#         return redirect(url_for("pick_category_bp.home_page"))
    

# @pick_category_bp.route("/category-selection/<company>")
# def category_selection(company):
#     """Fetch categories based on the selected company. Use local data to get categories for 
#     the selected company"""
#     categories = app.categories_to_company[company]
#     print(categories)
#     return render_template("pick_home.html", company=company, categories=categories)



