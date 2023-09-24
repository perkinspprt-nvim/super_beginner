
import requests

cache = dict()

def get_article_from_server(url):
    print("Fetching article from server...")
    response = requests.get(url)
    return response.text

def get_article(url):
    print("Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url)
    return cache[url]

# Corrected URL
url = "https://www.thinkful.com/blog/why-learning-to-code-is-so-damn-hard/"
content = get_article(url)

print("Content:")
print(content)

print("Cache:")
print(cache)
