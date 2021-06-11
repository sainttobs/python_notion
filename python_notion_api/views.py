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
        # githubIssues = {}
        # for data in github_data:
        #     githubIssues['url'] = github_data[data]
        return HttpResponse(githubIssuesurl)


# Create your views here.