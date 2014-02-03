from django.shortcuts import HttpResponse , render_to_response
from django.template import RequestContext
# Create your views here.

def index(request):
    CLIENT_ID = "test"
    REDIRECT_URI = "test"
    login_url = "http://join.agiliq.com/oauth/authorize/?client_id={}&redirect_uri={}".format(CLIENT_ID,REDIRECT_URI)
    data = { "login_url": login_url }
    return render_to_response("index.html",data,context_instance=RequestContext(request))