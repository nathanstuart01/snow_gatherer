import requests 
import json
from bs4 import BeautifulSoup

# gather all ikon/epic pass areas, try this function, see which ones return content, which do not
def get_area_html(area_url):
    area_to_harvest = requests.get(area_url)
    if area_to_harvest.status_code == 200:
        area_content = area_to_harvest.content
        return area_content
    else:
        return False