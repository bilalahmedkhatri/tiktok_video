from TikTokApi import TikTokApi
import random
import string
from db import add_data


def download_video(video_id, file_format=None):
    with TikTokApi() as api:
        video = api.video(id=str(video_id))
        video_byte = video.bytes()
        random_name = "".join((random.choice(string.ascii_letters) for i in range(10)))
        with open(f"videos/{random_name}.mp4", 'wb') as file:
            file.write(video_byte)
            print('video downloadeded...')

def hashtag():
    api = TikTokApi()
    tag = api.hashtag(name="pubg")
    return tag


def save_hashtag():
    # Initlize tiktok API
    api = TikTokApi()
    
    # create empty list
    auto_generate_hashtag = []

    tag = api.hashtag(name="trending")

    for v in tag.videos(count=10):
        json_v = v.as_dict
        for hashtag in json_v['textExtra']:
            auto_generate_hashtag.append(hashtag['hashtagName'])
    
    print(auto_generate_hashtag)
    header = ['name',]
    add_data(header, auto_generate_hashtag, 'test_hashtag')
    print('hashtags are saved ')

save_hashtag()


def hashtag():
    
    downloaded_list = []
    video_downloaded_status = False
    auto_generate_hashtag = []
    api = TikTokApi()

    tag = api.hashtag(name="trending")
    
    count = 0

    for v in tag.videos(count=10):
        
        print('counting ', count, 'v-id', v.id)
        
        json_v = v.as_dict
        # for video_ID in downloaded_list:
        for video_ID in json_v:
            if video_ID != str(json_v['id']):
                if json_v['id'] not in downloaded_list:
                    print('Id not match, Video will download')
                    downloaded_list.append(v.id)
                    for hashtag in json_v['textExtra']:
                        if hashtag not in auto_generate_hashtag:
                            auto_generate_hashtag.append(hashtag['hashtagName'])
                    download_video(v.id)
                    video_downloaded_status += True
                    count += 1
        
        if count == 2:
            print(downloaded_list)
            print(auto_generate_hashtag)
            print(len(auto_generate_hashtag))
            break
    
    header = ['video_id',]
    res = add_data(header, auto_generate_hashtag, 'tiktok_hashtag')
    print('save hashtag ', res)
    print(count)

# hashtag()
