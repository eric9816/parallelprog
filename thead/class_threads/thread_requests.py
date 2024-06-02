import threading

import requests


sources = ["https://ya.ru",
           "https://www.bing.com",
           "https://www.google.ru",
           "https://www.yahoo.com",
           "https://mail.ru"]

def get_request_header(url: str):
    return requests.get(url).headers


class GetHeaders(threading.Thread):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.url_headers = None

    def run(self):
        self.header = get_request_header(self.url)
        self.url_headers = {self.url: self.header}
        #return self.url_headers

threads = [GetHeaders(url) for url in sources]

for i in threads:
    i.start()

for i in threads:
    i.join()

result = [t.url_headers for t in threads]
print(result)
