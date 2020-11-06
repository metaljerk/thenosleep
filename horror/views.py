from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import json
import requests
import os
import praw

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
    context = {'data': data}
    return render(request, 'horror/nosleep.html', context)