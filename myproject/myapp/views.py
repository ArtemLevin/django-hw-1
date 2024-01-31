from django.shortcuts import render
import logging
from django.http import HttpResponse
import random

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 0
    except Exception as e:
        logger.exception(f"Error in about page: {e}")
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.")

# Create your views here.
def heads_and_tails(request):
    logger.info('Head and tails page accessed')
    return HttpResponse(f'<h1>{random.choice(["Head", "Tail"])}</h1>')

def about_me_html(request):
    return render(request, "about.html")