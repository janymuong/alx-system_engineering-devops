#!/usr/bin/python3
'''
module 100-count:
Queries the Reddit API recursively, parses the title of all hot articles
and prints a sorted count of given keywords
in the titles of all hot articles for a given subreddit
'''
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    '''
    Prints a sorted count of given keywords
    in the titlesof all hot articles for a subreddit.
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
                sorted_words = sorted(word_count.items(),
                                      key=lambda x: (-x[1], x[0]))
                for word, count in sorted_words:
                    print(f"{word}: {count}")
                return

            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1

            after = data['data']['after']
            return count_words(subreddit, word_list, after, word_count)
        except (KeyError, ValueError):
            return
    else:
        return
