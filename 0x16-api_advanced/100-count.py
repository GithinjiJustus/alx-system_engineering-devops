#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.
"""
import requests

def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    if word_counts is None:
        word_counts = {}
    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if title.count(word.lower()) > 0:
                    if word.lower() in word_counts:
                        word_counts[word.lower()] += title.count(word.lower())
                    else:
                        word_counts[word.lower()] = title.count(word.lower())
        after = data['data']['after']
        if after is not None:
            count_words(subreddit, word_list, after, word_counts)
        else:
            sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_counts:
                print("{}: {}".format(word, count))
    else:
        print(None)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
