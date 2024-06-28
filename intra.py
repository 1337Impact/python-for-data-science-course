from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import requests

# UID = "u-s4t2ud-a42af52687f2afbc8ad49c7a55e1d637d47ed7cf37d35d03fe6a143297a53a1a"
# SECRET = "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"
# TOKEN_URL = "https://api.intra.42.fr/oauth/token"

# # Create the OAuth2Session with client credentials
# client = BackendApplicationClient(client_id=UID)
# oauth = OAuth2Session(client=client)
# token = oauth.fetch_token(token_url=TOKEN_URL, client_id=UID, client_secret=SECRET)

token = "56c6b58aab35713be72adeeace25feffc9f97bb9e5587001f4fe84800e2abb73"

BASE_URL = 'https://api.intra.42.fr'
endpoint = '/v2/cursus'
headers = {
    'Authorization': f'Bearer 56c6b58aab35713be72adeeace25feffc9f97bb9e5587001f4fe84800e2abb73',
    'Content-Type': 'application/json'
}

users_in_cursus = requests.get(BASE_URL + endpoint, headers=headers)

if users_in_cursus.status_code == 200:
    users_data = users_in_cursus.text
    with open('cursus.json', 'w') as f:
        f.write(users_data)
else:
    print(f"Failed to fetch data: {users_in_cursus.status_code} - {users_in_cursus.text}")
