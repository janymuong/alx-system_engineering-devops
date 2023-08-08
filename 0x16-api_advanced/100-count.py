#!/usr/bin/python3
'''
module 100-count:
Queries the Reddit API recursively, parses the title of all hot articles
and prints a sorted count of given keywords
in the titles of all hot articles for a given subreddit
'''
import requests


def count_words(subreddit, word_list, instances={}, after='', count=0):
    '''
    Prints a sorted count of given keywords
    in the titlesof all hot articles for a subreddit.
    '''
    sub_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    user_agent = {'User-Agent': 'MyRedditScript/1.0'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    res = requests.get(sub_url, headers=user_agent, params=params,
                       allow_redirects=False)
    try:
        data = res.json()
        if res.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    data = data.get('data')
    after = data.get('after')
    count += data.get('dist')
    for c in data.get('children'):
        title = c.get('data').get('title').lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([tc for tc in title if tc == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print('')
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print('{}: {}'.format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
