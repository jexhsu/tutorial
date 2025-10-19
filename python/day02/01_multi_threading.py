import threading
from time import time

import requests


def runtime(func):
    def wrapper():
        start_time = time()
        func()
        end_time = time()
        print(f"Function '{func.__name__}' runtime is : {end_time - start_time:.4f} seconds")
    return wrapper

urls = [
    f"https://www.cnblogs.com/#{page}"
    for page in range(1, 10+1)
]

# print(urls)

def crawl(url):
    r =  requests.get(url)
    # print("status_code is : ", r.status_code)

# crawl(urls[0])

@runtime
def single_thread():
 [crawl(url) for url in urls]

@runtime
def multi_thread():
    threads = []
    [threads.append(threading.Thread(target=crawl, args=(url,))) for url in urls]
    [thread.start for thread in threads]

single_thread()
multi_thread()



