from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent
import asyncio


# Instantiate the client with the user's username
client = TikTokLiveClient(unique_id="@princerazaq59")


# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)


# Notice no decorator?
# async def on_comment(event: CommentEvent):
#     print(f" bilal ahmed {event.user.nickname} -> {event.comment} \n \n \n")


# Define handling an event via "callback"
# client.add_listener("comment", on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() # to run non-blocking
    client.run()