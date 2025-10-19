import threading
from time import time

import requests
from bs4 import BeautifulSoup


def runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()
        print(f"Function '{func.__name__}' runtime is : {end_time - start_time:.4f} seconds")
    return wrapper

urls = [
    f"https://www.cnblogs.com/#{page}"
    for page in range(1, 10+1)
]

def home_page(url):
    r =  requests.get(url)
    return r.text

def parse_home_page(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]

if __name__ == "__main__":
    results = parse_home_page(home_page(urls[0]))
    [print(result) for result in results]
