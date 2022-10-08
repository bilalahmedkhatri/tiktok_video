from TikTokApi import TikTokApi
import random
import string


def download_video(video_id, file_format=None):
    with TikTokApi() as api:
        video = api.video(id=str(video_id))
        video_byte = video.bytes()
        random_name = "".join((random.choice(string.ascii_letters) for i in range(10)))
        with open(f"videos/{random_name}.mp4", 'wb') as file:
            file.write(video_byte)
            print('video downloaded...')


def hashtag():
    
    downloaded_list = ['6815298064023145734', '6962955469765790977']
    video_downloaded_status = False
    auto_generate_hashtag = []
    api = TikTokApi()

    tag = api.hashtag(name="europe")

    count = 0

    for v in tag.videos(count=10):
        
        print('counting ', count, 'v-id', v.id)
        
        json_v = v.as_dict
        for video_ID in downloaded_list:
            if video_ID != str(json_v['id']):
                if json_v['id'] not in downloaded_list:
                    print('not matched')
                    downloaded_list.append(v.id)
                    for hashtag in json_v['textExtra']:
                        if hashtag not in auto_generate_hashtag:
                            auto_generate_hashtag.append(hashtag['hashtagName'])
                    download_video(v.id)
                    video_downloaded_status += True
                    count += 1
        
        print(downloaded_list)
        print(auto_generate_hashtag)
        
        if count == 5:
            print(downloaded_list)
            break
        
    print(count)

hashtag()
