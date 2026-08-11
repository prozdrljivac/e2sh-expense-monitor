import collections
import requests
import os

import google.oauth2.credentials as google_auth

GoogleSettings = collections.namedtuple('GoogleSettings', ['client_id', 'client_secret', 'access_token', 'refresh_token'])

def main():
    settings = GoogleSettings(os.environ.get("CLIENT_ID"), os.environ.get("CLIENT_SECRET"), os.environ.get("ACCESS_TOKEN"), os.environ.get('REFRESH_TOKEN'))
    # TODO: Read google-auth.readthedocs.io/en/master/reference/google.oauth2.credentials.html, looks like it will not work like this
    credentials = google_auth.Credentials(token='garbage_value', refresh_token=settings.refresh_token)
    if not credentials.valid:
        credentials.refresh()

    response = requests.api.get(url='https://gmail.googleapis.com/gmail/v1/users/me/profile', headers={
       'Authorization': f'Bearer {credentials.token}'
    })
    print(f'Status Code: {response.status_code}')
    


if __name__ == "__main__":
    main()
