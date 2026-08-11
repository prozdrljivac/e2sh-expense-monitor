"""
# NOTE

Looks like it is possible to get access token and refresh token via GoogleOauthPlayground, capture that and use it for the auth piece
"""
import collections
import requests
import os

GoogleSettings = collections.namedtuple('GoogleSettings', ['client_id', 'client_secret', 'access_token', 'refresh_token'])


def main():

    # 1. Access environment variables
    google_settings = GoogleSettings(os.environ.get("CLIENT_ID"), os.environ.get("CLIENT_SECRET"), os.environ.get("ACCESS_TOKEN"), os.environ.get('REFRESH_TOKEN'))
    print(google_settings)
    response = requests.api.get(url='https://gmail.googleapis.com/gmail/v1/users/me/profile', headers={
       'Authorization': f'Bearer {google_settings.access_token}'
    })
    print(f'Status Code: {response.status_code}')

    
    # 2. Get access token and refresh token
    # 3. Use access token to get the last email


if __name__ == "__main__":
    main()
