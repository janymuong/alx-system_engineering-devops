# API Advanced
> Uses the Reddit API:  
> [https://www.reddit.com/dev/api/](https://www.reddit.com/dev/api/)  

This project involves interacting with an API to retrieve and manipulate data from the API data. The goal is to demonstrate proficiency in working with APIs, handling `JSON` data, pagination, and other relevant skills.

#### [Jump To:]()

- [Premise](#premise)
- [Getting Started](#getting-started)
- [Usage](#usage)


## Premise

This project focuses on using the Reddit API to accomplish various tasks such as fetching posts, sorting data, and performing recursive API calls. The project follows specific requirements outlined in the project instructions.

## Getting Started:
Install the required dependencies:

```bash
pip install requests
```

## Usage

> 1. Run the project files using Python 3. Make sure the first line of each file is `#!/usr/bin/python3`.  
> 2. Execute the modules to see the demonstration of various tasks using the Reddit API.  
> 3. Follow the command-line prompts to interact with different features of the project(see below):  

```bash
$ cat 100-main.py 
#!/usr/bin/python3
"""
100-main
"""
import sys

if __name__ == '__main__':
    count_words = __import__('100-count').count_words
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
$             
$ python3 100-main.py programming 'react python java javascript scala no_results_for_this_one'
java: 27
javascript: 20
python: 17
react: 17
scala: 4
$ python3 100-main.py programming 'JavA java'
java: 54
$ python3 100-main.py not_a_valid_subreddit 'python java javascript scala no_results_for_this_one'
$ python3 100-main.py not_a_valid_subreddit 'python java'
$ 
```

```bash
$ cat 100-count.py
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
$
```
