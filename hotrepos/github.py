import requests
from datetime import datetime, timedelta
import json


def get_hot_repos(num=30):
    week_ago = (datetime.utcnow() - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%S%z")
    response = requests.get('https://api.github.com/search/repositories?'
                            'q=created:>' + week_ago + '&'
                                                       'sort=stars&'
                                                       'order=desc')
    repos = json.loads(response.text)['items'][:num]
    print 'fetched ' + repr(len(repos)) + ' repos'
    return repos
