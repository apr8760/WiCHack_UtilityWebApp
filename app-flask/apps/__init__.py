from flask import Flask
from apps.api import *


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    app.tables = init_tables(app)
    app.categories_to_company = init_categories_to_company(app)
    app.categories_to_table = init_categories_to_table(app)
    app.available_tables = init_availability(app)

    with app.app_context():
        # Include our Routes
        from .pick_company import pick_company
        from .ready_for_table import ready_for_table
        from .set_table import set_table
        from .timer import timer

        # Register Blueprints
        app.register_blueprint(pick_company.pick_company_bp)
        app.register_blueprint(ready_for_table.ready_for_table_bp)
        app.register_blueprint(set_table.set_table_bp)
        # app.register_blueprint(timer.timer_bp)

        return app
    