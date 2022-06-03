from decouple import config
from src.entrypoints.api.app import create_app

app = create_app(config("FLASK_CONFIG"))
