import os
from dotenv import load_dotenv
import webbrowser

from django.shortcuts import redirect, render

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
BASE_URL = "https://accounts.spotify.com/authorize"


# Create your views here.
def request_authentication(request):
    request_authentication_url = (
        f"{BASE_URL}?response_type=code&client_id={CLIENT_ID}"
        + f"&redirect_uri={REDIRECT_URI}&scope=user-read-private"
    )
    # webbrowser.open(request_authentication_url)
    return render(request, "request.html", {"url": request_authentication_url})


def callback(request):
    return None
