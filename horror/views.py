from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import json
import requests
import os

headers = {
    'authority': 'www.reddit.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51',
    'accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-IN,en-GB;q=0.9,en;q=0.8,en-US;q=0.7',
    'cookie': os.environ['COOKIE']
}


def about(request):
    return render(request, 'horror/about.html')


# Create your views here.
def horror(request):
    response = requests.get('https://www.reddit.com/r/nosleep/top/.json',
                            headers=headers)

    #saving the response in json format(stored as dictionary)
    data_response = response.json()

    # data_response has keys data->children->data->title.
    for item in data_response['data']['children']:
        data = item['data']
        break

    context = {'data': data}
    return render(request, 'horror/horror.html', context)
