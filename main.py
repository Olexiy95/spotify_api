from authorisation import *

import requests
import json

head = {
    "Content-Type": "application/json",  
    "Authorization": "Bearer {}".format(spotify_token)
}

base_url = 	"https://api.spotify.com"

r = requests.get(base_url + "/v1/me", headers=head)

rr = r.json()

print(rr)