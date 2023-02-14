import requests
from bs4 import BeautifulSoup

FSO_PAGE_URL = 'https://www.bfs.admin.ch/asset/de/'
FSO_ASSET_URL = 'https://www.bfs.admin.ch/bfsstatic/dam/assets/'

class FSOLocateExcetion(Exception):
    pass


def get_asset_url(pxid):
    asset_page_url = f'{FSO_PAGE_URL}{pxid}'
    try:
        resp = requests.get(asset_page_url)
        soup = BeautifulSoup(resp.content, features="html.parser")
        meta_url = soup.find("meta", {"property": "og:url"}).get('content')
        asset_nr = meta_url.split('/')[-1]
    except AttributeError:
        raise FSOLocateExcetion(f'Resource location was not found for {pxid}')
    except Exception as e:
        raise FSOLocateExcetion(f'An unexpected error {e} occured for {pxid}')
    else:
        return f'{FSO_ASSET_URL}{asset_nr}/master'
