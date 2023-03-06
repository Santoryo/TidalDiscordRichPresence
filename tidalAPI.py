import tidalapi
from plyer import notification
import os
import sys
import requests
from cryptography.fernet import Fernet
import json

import keys

session = tidalapi.Session()
# Will run until you visit the printed url and link your account

def getSession():
    try:
        fernet = Fernet(keys.getKey())
        f = open("token.brel", "rb")
        encrypted = f.read()
        tokens = fernet.decrypt(encrypted)
        tokens = tokens.decode("utf-8")
        tokens = tokens.split('|')
        session.load_oauth_session(tokens[0], tokens[1], tokens[2], tokens[3])
    except:
        login, future = session.login_oauth()
        notification.notify(title="Open the URL to log in", description=login.verification_uri_complete, app_name="TIDAL Rich Presence")

        if sys.platform=='win32':
            os.startfile(f'https://{login.verification_uri_complete}')
        elif sys.platform=='darwin':
            subprocess.Popen(['open', url])
        else:
            try:
                subprocess.Popen(['xdg-open', url])
            except OSError:
                print ('Please open a browser on: '+url)

        future.result()
        if (session.check_login()):

            key = Fernet.generate_key()
            with open('filekey.key', 'wb') as filekey:
                filekey.write(key)

            token_type = session.token_type
            access_token = session.access_token
            refresh_token = session.refresh_token
            expiry_time = session.expiry_time
            data = f"{token_type}|{access_token}|{refresh_token}|{expiry_time}"
            f = open("token.brel", "wb")
            fernet = Fernet(key)
            print(key)
            encrypted = fernet.encrypt(bytes(data, "utf-8"))
            f.write(encrypted)
            f.close()


def getData(song='K/DA - DRUM GO DUM'):
    getSession()
    media = tidalapi.media

    if(song):
        s = session.search(song, models=None, limit=1, offset=0)


        for track in s['tracks']:
                artists = []
                for artist in track.artists:
                    artists.append(artist.name)
                url = track.album.cover.split('-')
                cover = f"https://resources.tidal.com/images/{url[0]}/{url[1]}/{url[2]}/{url[3]}/{url[4]}/1280x1280.jpg"
                link = track.id
                #for info in dir(track):
                    #print(info)

                _artists = ', '.join(artists)

        data = f'{{"name": "{track.name}", "artists": "{_artists}", "time": "{track.duration}", "cover": "{cover}", "link": "{link}", "largetext": "{track.album.name}"}}'

        data = json.loads(data)

        return data
    