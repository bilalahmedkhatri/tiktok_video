import imp
from TikTokApi import TikTokApi
import random
from db import get_data, insert_data

# django models
from django.db import models
from video_editor.models import HashTag, VideoOwner

def save_api_data():
    # Database info
    hashtag_header = ['hashtag', 'count_hashtag', 'created_at', 'updated_at',]
    video_id_header = ['video_id', 'created_at', 'updated_at',]
    hashtag_names = []
    video_id = []
    hashtag_table = "video_editor_hashtag"
    video_id_table = "video_editor_videoid"
    
    # Initlize tiktok API
    api = TikTokApi()
    
    # get oldest hashtags
    top_hashtags = get_data(hashtag_header, hashtag_table)
    if top_hashtags:
        random_hashtag = random.choice(top_hashtags)
        print('randome tag', random_hashtag[0])
        tag = api.hashtag(name=random_hashtag[0])
    else:
        tag = api.hashtag(name="рекомендации")
    print('bilal')
    for v in tag.videos():
        json_v = v.as_dict
        video_id.append(json_v['id'])
        VideoOwner.objects.get_or_create(owner_id=v['id'], name=v['auther']['nickname'], instagram_acc=v['auther']['signature'], total_videos=v['autherStates']['videoCount'])
        print('getting...')
    #     for hashtag in json_v['textExtra']:
    #         hashtag_names.append(hashtag['hashtagName'])
    
    # print("total hashtags:", len(hashtag_names), len(video_id), video_id)
    # # database arguments
    # if hashtag_table:
    #     insert_data(hashtag_header, hashtag_names, hashtag_table)
    # elif video_id_table:
    #     insert_data(video_id_header, video_id, video_id_table)
        

# if __name__ == "__main__":
#     save_api_data()