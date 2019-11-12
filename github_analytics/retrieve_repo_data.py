print("starting")
import requests
import numpy as np
import scipy as sp
from github import Github
import pandas as pd
import os
import json
import collections
from datetime import date

import getpass
# set to your username here
github_user = "gholcomb"
print("Enter %s's GitHub Password:" % github_user)
github_pass = getpass.getpass()

# current timestamp
import time
ts = time.time()

import datetime
# YYYY-MM-DDTHH:MM:SSZ
# until now
date_until = datetime.datetime.fromtimestamp(ts)
# minus 14 days for since to get last month
date_since = date_until - datetime.timedelta(days=360)

"""
Use the pygithub library to retrieve data
http://pygithub.readthedocs.io/en/latest/introduction.html
"""
# https://pygithub.readthedocs.io/en/latest/apis.html
# using username and password
g = Github(github_user, github_pass)
# get_organization(login)¶
org = g.get_organization('buildlyio')
#  get_repo(full_name_or_id, lazy=True)
repo = org.get_repo('buildly-core')
# get_pulls(state=NotSet, sort=NotSet, direction=NotSet, base=NotSet, head=NotSet)
# https://developer.github.com/v3/pulls/
# https://pygithub.readthedocs.io/en/latest/github_objects/PullRequest.html#github.PullRequest.PullRequest
pulls = repo.get_pulls(state="all",base="master")

# get_commits(sha=NotSet, path=NotSet, since=NotSet, until=NotSet, author=NotSet)
commits = repo.get_commits(since=date_since, until=date_until)

pull_data = collections.defaultdict(dict)

def get_github_meta():
    x=1
    for d in pulls:
        
        if d.created_at > date_since and d.created_at < date_until:
            pull_data['user'][x]=d.user.login
            pull_data['created_at'][x]=d.created_at
            pull_data['title'][x]=d.title
            pull_data['state'][x]=d.state
            pull_data['number'][x]=d.number
            pull_data['assignee'][x]=d.assignee
            pull_data['merged'][x]=d.merged
            pull_data['milestone'][x]=d.milestone
            pull_data['merged_at'][x]=d.merged_at
            pull_data['merged_by'][x]=d.merged_by.name if d.merged_by != None else "Nobody?"

            x=x+1

    df = pd.DataFrame(pull_data)

    # return df
