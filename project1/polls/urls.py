from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('twitter_results/<str:question_id>/', views.twitter_results, name='twitter_results'),
    # ex: /polls/5/results/
    path('reddit_results/<str:question_id>/', views.reddit_results, name='reddit_results'),
    # ex: /polls/5/vote/
    path('wiki_results/<str:question_id>/', views.wiki_results, name='wiki_results'),
    path('imdb_results/<str:question_id>/', views.imdb_results, name='imdb_results'),
]