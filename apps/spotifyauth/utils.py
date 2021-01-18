import os
from dotenv import load_dotenv
import requests
import urllib.request
import webbrowser

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

BASE_URL = 'https://accounts.spotify.com/authorize'

req = f?response_type=code&client_id={CLIENT_ID}&redirect_uri=http%3A%2F%2Fabcdefg.com%2Fcallback&scope=user-read-private%20user-read-email"""
webbrowser.open(req)