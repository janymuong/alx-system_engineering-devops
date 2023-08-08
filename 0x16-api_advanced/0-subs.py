#!/usr/bin/python3
'''
module 0-subs:
Queries the Reddit API and for number of subreddit subscribers
'''
import requests


def number_of_subscribers(subreddit):
    '''
    returns the number of subscribers for a given subreddit.
    '''
    about_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    user_agent = {'User-Agent': 'MyRedditScript/1.0'}

    res = requests.get(about_url, headers=user_agent)

    if res.status_code == 200:
        try:
            data = res.json()
            return data['data']['subscribers']
        except (KeyError, ValueError):
            return 0
    else:
        return 0
