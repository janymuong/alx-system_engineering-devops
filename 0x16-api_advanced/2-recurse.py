#!/usr/bin/python3
'''
module 2-recurse:
Queries the Reddit API recursively
and returns a list containing the titles of all hot articles for a subreddit
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''
    Returns a list containing the titles of all hot articles.
    '''
    sub_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    user_agent = {'User-Agent': 'MyRedditScript/1.0'}
    params = {'after': after} if after else {}

    res = requests.get(sub_url, headers=user_agent, params=params,
                       allow_redirects=False)

    if res.status_code == 200:
        try:
            data = res.json()
            posts = data['data']['children']

            if not posts:
                return hot_list

            hot_list.extend([post['data']['title'] for post in posts])
            after = data['data']['after']

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        except (KeyError, ValueError):
            return None
    else:
        return None


def top_ten(subreddit):
    '''
    Prints the titles of the first 10 hot posts for a given subreddit.
    '''
    hot_list = recurse(subreddit)

    if hot_list is not None:
        for i, title in enumerate(hot_list[:10], start=1):
            print(f"{i}. {title}")
    else:
        print(None)
