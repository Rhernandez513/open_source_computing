from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

from . import twitter_interface
from . import reddit_interface
from . import wikipedia_interface
from . import imdb_interface


def index(request):
    response = "Hello World, You're looking at the polls index."
    context = {
        'response' : response
    }

    return render(request, 'index.html', context)

def twitter_results(request, question_id):
    twitter_response = twitter_interface.tweet_api.GetSearch(question_id)
    context = {
        'twitter_reponse' : twitter_response
    }
    # return HttpResponse(twitter_response)
    return render(request, 'twitter_results.html', context)

def reddit_results(request, question_id):
    response = ""
    response = []

    for idx, val in enumerate(reddit_interface.reddit_api.search(question_id, limit=5)):


        response += val.title
        response += "<br/>"
        response += "<br/>"

    context = {
        'reddit_response': response
    }
    # return HttpResponse(response)
    return render(request, 'reddit_results.html', context)

def wiki_results(request, question_id):

    page = wikipedia_interface.api.page(question_id)
    page = wikipedia_interface.api.page(question_id)
    response = ""
    response += page.text
    # return HttpResponse("You're voting on question %s." % question_id)
    return HttpResponse(response)

def imdb_results(request, question_id):
    result = imdb_interface.imdb.search_for_title(question_id)
    return HttpResponse(result)
