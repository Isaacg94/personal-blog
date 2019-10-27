from app import app
import urllib.request,json
from .models import quote


# Getting the movie base url
base_url = app.config["QUOTE_BASE_URL"]