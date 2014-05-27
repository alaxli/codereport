import logging
import sys
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from codereport.lib.django_util import render

LOG = logging.getLogger(__name__)

#def home(request):
#    return render( "index.html", request, {"request":request})


def serve_404_error(request, *args, **kwargs):
    """Registered handler for 404. We just return a simple error"""
    return render("404.html", request, dict(uri=request.build_absolute_uri()))

def serve_500_error(request, *args, **kwargs):
    """Registered handler for 500. We use the debug view to make debugging easier."""
    exc_info = sys.exc_info()
    return render("500.html", request, {'traceback': traceback.extract_tb(exc_info[2])})

