from textwrap import indent
from TikTokApi import TikTokApi
import random
import string
import json
import re

def download_videos():
    
    with TikTokApi() as api:
        
        tag = api.hashtag(name="europe")
        # print('tag info', tag.info_full())
        
        for v in tag.videos(count=1):
            conv = json.dumps(v.as_dict)
            v_json = json.loads(conv)
            dic = json.dumps(v_json, indent=4)
            # print('result', dic)
            video_id = api.video(id=str(v.id))
            print('result', video_id.as_dict)
            with open(f'json/data.json', 'w') as j:
                json.dump(video_id.as_dict, j)
                print('success')
                b = video_id.as_dict
                print(type(b))
                bb = b['video']['bitrateInfo']
                print(json.dumps(bb, indent=4))
                break
            # video_byte = video_id.bytes()            
            # cv = ''.join((random.choice(string.ascii_letters) for i in range(10)))
            # with open(f"videos/{cv}.mp4", "wb") as out_file:
            #     out_file.write(video_byte)
            #     print('success')
        

print(download_videos())

