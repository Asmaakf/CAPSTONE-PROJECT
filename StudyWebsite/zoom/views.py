from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
import requests
import json
# Create your views here.
def base64_encode(message):
    import base64

    message = "Python is fun"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    
    return base64_encode

def zoom_session_view(request:HttpRequest):
    code = request.GET["code"]
    data = requests.post(f"https://zoom.us/oauth/token?grant_type=authorization_code&code={code}&redirect_url=http://127.0.0.1:8000/zoom/session/",
        headers={"Authorization" : "Basic" + str(base64_encode('cR3iGP3hTlWpC_W3IGQe2Q:O0cuhx8Fplp0iy716JLzHvbBd4oJmZx5'))
        }
    )
    print(data.text)
    request.session["zoom_access_token"] = data.json()["access_token"]
    return HttpResponseRedirect("/zoom/schedule_session/")
    

def create_zoom_view(request:HttpRequest):

    pass