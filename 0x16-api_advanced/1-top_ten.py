#!/usr/bin/python3
'''
module 1-top_ten:
Queries the Reddit API
and prints titles of the first 10 hot posts for a given subreddit
'''
import requests


def top_ten(subreddit):
    '''
    prints the titles of the first 10 hot posts for a given subreddit.
    '''
    sub_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    user_agent = {'User-Agent': 'MyRedditScript/1.0'}

    res = requests.get(sub_url, headers=user_agent)

    if res.status_code == 200:
        try:
            data = res.json()
            posts = data['data']['children']
            for post in posts[:10]:
                # posts assumed to be arranged in 'hotness':
                print(post['data']['title'])
        except (KeyError, ValueError):
            print(None)
    else:
        print(None)
