# from TikTokApi import TikTokApi
# import string
# import random

# def download_video(video_id, file_format=None):
#     api = TikTokApi()
#     print('1')
#     video = api.video(id=str(video_id))
#     print('2')
#     video_byte = video.bytes()
#     print('3')
#     random_name = "".join((random.choice(string.ascii_letters) for i in range(10)))
#     print('4')
#     with open(f"{random_name}.mp4", 'wb') as file:
#         print('5')
#         file.write(video_byte)
#         print('video downloaded...')
        



# def download_video(video_id, file_format=None):
#     with TikTokApi() as api:
#         video = api.video(id=str(video_id))
#         video_byte = video.bytes()
#         random_name = "".join((random.choice(string.ascii_letters) for i in range(10)))
#         with open(f"videos/{random_name}.mp4", 'wb') as file:
#             file.write(video_byte)
#             print('video downloadeded...')
            
            
# def hashtag():
    
#     downloaded_list = []
#     video_downloaded_status = False
#     auto_generate_hashtag = []
#     api = TikTokApi()

#     tag = api.hashtag(name="trending")
    
#     count = 0

#     for v in tag.videos(count=10):
        
#         print('counting ', count, 'v-id', v.id)
        
#         json_v = v.as_dict
#         # for video_ID in downloaded_list:
#         for video_ID in json_v:
#             if video_ID != str(json_v['id']):
#                 if json_v['id'] not in downloaded_list:
#                     print('Id not match, Video will download')
#                     downloaded_list.append(v.id)
#                     for hashtag in json_v['textExtra']:
#                         if hashtag not in auto_generate_hashtag:
#                             auto_generate_hashtag.append(hashtag['hashtagName'])
#                     download_video(v.id)
#                     video_downloaded_status += True
#                     count += 1
        
#         if count == 2:
#             print(downloaded_list)
#             print(auto_generate_hashtag)
#             print(len(auto_generate_hashtag))
#             break
    
#     header = ['video_id',]
#     res = add_data(header, auto_generate_hashtag, 'tiktok_hashtag')
#     print('save hashtag ', res)
#     print(count)


from TikTokApi import TikTokApi

with TikTokApi() as api:
    user = api.user(username="ROOHULLAH")

    # x = user.info()
    # print(x)
    for video in user.videos():
        print(video)

    # for liked_video in api.user(username="public_likes").videos():
    #     print(liked_video.id)