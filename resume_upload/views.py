from django.shortcuts import HttpResponse , render_to_response
from django.template import RequestContext
from os import environ
# Create your views here.

def index(request):
    CLIENT_ID = environ['CLIENT_ID']
    REDIRECT_URI = environ['REDIRECT_URI']
    login_url = "http://join.agiliq.com/oauth/authorize/?client_id={}&redirect_uri={}".format(CLIENT_ID,REDIRECT_URI)
    return render_to_response("index.html",{ "login_url": login_url },context_instance=RequestContext(request))

def login(request):
    pass
