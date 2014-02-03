from django.shortcuts import HttpResponse , render_to_response
from django.template import RequestContext
from os import environ
import requests
# Create your views here.

def index(request):
    CLIENT_ID = environ['CLIENT_ID']
    REDIRECT_URI = environ['REDIRECT_URI']
    login_url = "http://join.agiliq.com/oauth/authorize/?client_id={}&redirect_uri={}".format(CLIENT_ID,REDIRECT_URI)
    return render_to_response("index.html",{ "login_url": login_url },context_instance=RequestContext(request))

def upload(request):
    pay_load = {"client_id":environ['CLIENT_ID'], "client_secret": environ['CLIENT_SECRET'],
                "redirect_uri": environ['REDIRECT_URI'], "code": request.GET['code']}
    response= requests.post("http://join.agiliq.com/oauth/access_token/",data=pay_load)
    if response.ok:
        token_data = response.json()
        data = {"access_token":token_data['access_token']}
        return render_to_response("upload.html",data,context_instance=RequestContext(request))
    else:
        return HttpResponse(str(response.reason))
