import urllib.parse
import requests


def data_from_url(url):
    headers = {}
    url = urllib.parse.unquote(url)
    try:
        return requests.get(url, headers=headers).content
    except Exception as e:
        print('Failed to download article at : {}. '
              'Error: {}'.format(url, e))
