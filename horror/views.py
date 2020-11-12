from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import json
import requests
import os
import praw
from rest_framework import views
from rest_framework.response import Response

client_id = os.environ['CLIENT_ID']
client_sec = os.environ['CLIENT_SECRET']
user_agent = os.environ['USER_AGENT']
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_sec,
                     user_agent=user_agent)


def about(request):
    return render(request, 'horror/about.html')


#getting reddit posts using PRAW
def hot_post(request):
    data = []
    nosleep_data = reddit.subreddit('NoSleep').hot(limit=50)
    for post in nosleep_data:
        if post.stickied == False:
            data.append(post)
    context = {'data': data}
    return render(request, 'horror/hot_post.html', context)


#to render post by post id
def nosleep(request, id):
    post_id = request.GET.get('id')
    # print(post_id)
    data = reddit.submission(id=id)
    if data.subreddit == 'NoSleep':
        context = {'data': data}
        return render(request, 'horror/nosleep.html', context)
    else:
        return render(request, 'horror/404.html')


#list api
class RedditListView(views.APIView):
    def get(self, request):
        data = []
        nosleep_data = reddit.subreddit('NoSleep').hot(limit=50)
        for post in nosleep_data:
            if post.stickied == False:
                data.append([{
                    "post_id": post.id,
                    "author": str(post.author),
                    "title": post.title,
                }])
        return Response(data)


#read api
class RedditReadView(views.APIView):
    def get(self, request, id):
        post_id = request.query_params.get('id')
        data = reddit.submission(id=id)
        if data.subreddit == 'NoSleep':
            data = [{
                "post": data.selftext,
                "nsfw": data.over_18,
                "flair": data.link_flair_text,
                "upvote": data.score,
                "gildings": data.gildings
            }]

        return Response(data)


def custom_404(request, exception):
    return render(request, 'horror/404.html')


def custom_500(request):
    return render(request, 'horror/500.html')
