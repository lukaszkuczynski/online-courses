import os
import json
import requests


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    #
    # Once you've done this, return the name of the number 1 top artist in
    # Spain.
    body = requests.get(url)
    response = json.loads(body.text)
    top = response['topartists']['artist'][0]['name']
    return top


if __name__ == '__main__':
    api_key = os.environ["LASTFM_API_KEY"]
    url_to_get = f"http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key={api_key}&format=json"
    top = api_get_request(url_to_get)
    print(top)

