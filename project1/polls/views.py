from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def index(request):
    response = ""

    response = "Hello World, You're looking at the polls index."
    context = {}

    return render(request, 'index.html', context)
    # return HttpResponse(response)

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    from . import twitter_interface
    return HttpResponse(twitter_interface.tweet_api.GetSearch(question_id))

def reddit_results(request, question_id):
    # response = "You're looking at the results of question %s."

    from . import reddit_interface
    response = ""

    for i in reddit_interface.reddit_api.search(question_id, limit=5):
        response += i.title
        response += "<br/>"
        response += "<br/>"
    return HttpResponse(response)

def wiki_results(request, question_id):

    from . import wikipedia_interface
    page = wikipedia_interface.api.page(question_id)
    page = wikipedia_interface.api.page(question_id)
    response = ""
    response += page.text
    # return HttpResponse("You're voting on question %s." % question_id)
    return HttpResponse(response)

def imdb_results(request, question_id):
    from . import imdb_interface
    result = imdb_interface.imdb.search_for_title(question_id)
    return HttpResponse(result)
