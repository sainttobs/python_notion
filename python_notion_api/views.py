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
    github_api = requests.get('https://api.github.com/repos/sainttobs/python_notion/issues')
    github_api.headers={"Authorization": "token" + env('GITHUB_KEY'), "Accept": "application/vnd.github.v3+json"}
    if github_api.status_code != 200:
        raise ApiError('Response Status: {response.status_code}')
    else:
        content = github_api.text
        return HttpResponse(content)


# Create your views here.
