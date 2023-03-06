import time
from datetime import datetime
from pypresence import Presence
import tidalAPI
import json


RPC = Presence(ApplicationIDGoesHere)

def connectRPC():
    RPC.connect()





def updateRPC(song):

    dt = datetime.now()
    ts = datetime.timestamp(dt)

    data = tidalAPI.getData(song)
    RPC.update(
        details = data['name'],
        state = f"by {data['artists']}" ,
        end = int(ts) + int(data['time']),
        large_image = data['cover'],
        large_text= data['largetext'],
        buttons = [{"label": "▶️ Listen on Tidal", "url": f"https://tidal.com/browse/track/{data['link']}"}]
    )


def clearRPC():
    RPC.clear()
