from TikTokApi import TikTokApi
import string
import random

def download_video(video_id, file_format=None):
    api = TikTokApi()
    print('1')
    video = api.video(id=str(video_id))
    print('2')
    video_byte = video.bytes()
    print('3')
    random_name = "".join((random.choice(string.ascii_letters) for i in range(10)))
    print('4')
    with open(f"{random_name}.mp4", 'wb') as file:
        print('5')
        file.write(video_byte)
        print('video downloaded...')
        