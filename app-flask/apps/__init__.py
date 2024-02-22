from flask import Flask
from apps.api.api_init_memory import *


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    app.tables = init_tables(app)
    app.categories_to_company = init_categories_to_company(app)
    app.tables_to_category = init_tables_to_category(app)
    app.available_tables = init_availability(app)
    app.category_done_dicts = init_category_done_dicts(app)
    app.company_done_dicts = init_company_done_dicts(app)

    with app.app_context():
        # Include our Routes
        from .pick_category import pick_category
        from .ready import ready
        from .goto_table import goto_table
        from .timer import timer

        # Register Blueprints
        app.register_blueprint(pick_category.pick_category_bp)
        app.register_blueprint(ready.ready_bp)
        app.register_blueprint(goto_table.goto_table_bp)
        app.register_blueprint(timer.timer_bp)

        return app
    