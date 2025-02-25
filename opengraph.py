# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    """
    Returns the "data" dictionary of OpenGraph metadata found in HTML of given url}
    """
    url1 = f"https://opengraph.lewagon.com/?url={url}"
    response = requests.get(url1)
    if response.status_code != 200:
        return {}
    data = response.json()
    return data['data']



# # To manually test, uncomment the following lines and run `python opengraph.py`:
# if __name__ == "__main__":
#     import pprint
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(fetch_metadata("https://www.github.com"))
