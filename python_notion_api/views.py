# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, HttpResponse
import requests
import json

import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

def index(request):
    github_data = requests.get('https://api.github.com/repos/sainttobs/python_notion/issues')
    github_data.headers={"Authorization": "token" + env('GITHUB_KEY'), "Accept": "application/vnd.github.v3+json"}
    if github_data.status_code != 200:
        raise ApiError('Response Status: {response.status_code}')
    else:
        # for data in github_data:
        #     githubIssues['url'] = github_data[data]
        github_data = github_data.json()
        # getting length of list
        length = len(github_data)
        githubIssues = dict()
        for i in range(length):
            # githubIssues.append(github_data[i]['title'])
            githubIssues['title'] = github_data[i]['title']
            print(githubIssues)
    
        # id, title, state, body
        return HttpResponse(githubIssues)


# Create your views here.
