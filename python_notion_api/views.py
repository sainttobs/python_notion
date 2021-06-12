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
        github_data = github_data.json()
        # getting length of list
        length = len(github_data)
        githubIssues = dict()
        # gitIssues = []
        for i in range(length):
            githubIssues['id'] = github_data[i]['id']
            githubIssues['title'] = github_data[i]['title']
            githubIssues['state'] = github_data[i]['state']
            githubIssues['body'] = github_data[i]['body']
            # gitIssues.append(githubIssues)
            database_id = env('NOTION_DATABASE_ID')
            notion_post = requests.post('https://api.notion.com/v1/pages')
            notion_post.headers={"Authorization": "Bearer" + env('NOTION_KEY'), "Content-Type": "application/json", "Notion-Version": "2021-05-13"}
            notion_post.data = {"parent":{"database_id": database_id}, "properties" : githubIssues}
            # print(githubIssues)

            if notion_post.status_code != 200:
                return HttpResponse(notion_post.text)
            else:
                return HttpResponse(notion_post.text)
    
        # id, title, state, body
        # return HttpResponse(githubIssues)


# Create your views here.
