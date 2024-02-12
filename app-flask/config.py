"""Class-based Flask app configuration."""
import os


class Config:
    """Configuration from environment variables."""

    # Flask Config
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
    FLASK_APP = "wsgi.py"

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = False

    # Hardcoded data
    TABLE_PLACEMENTS_DATA_FILEPATH = r'C:\Users\ainsl\Google Drive\RIT\WiC\WiC_Projects\WiCHack_UtilityWebApp\data\table_placements.csv'
    CATEGORIES_TO_COMPANY_FILEPATH = r'C:\Users\ainsl\Google Drive\RIT\WiC\WiC_Projects\WiCHack_UtilityWebApp\data\categories_to_company.csv'
    CATEGORIES_TO_TABLE_FILEPATH = r'C:\Users\ainsl\Google Drive\RIT\WiC\WiC_Projects\WiCHack_UtilityWebApp\data\categories_to_table.csv'