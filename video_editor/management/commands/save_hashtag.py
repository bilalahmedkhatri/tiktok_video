import random
from django.utils import timezone
from django.core.management.base import BaseCommand
from TikTokApi import TikTokApi
from video_editor.models import HashTag, VideoID, VideoAuthor


class Command(BaseCommand):
    help = "Get TIKTOK data for download videos."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def hashtags(self, *args):
        author_id_not_exist = HashTag.objects.filter(hashtag=args[0]).exists()
        if not author_id_not_exist:
            HashTag.objects.create(hashtag=args[0])
        else:
            for hashtag_exist in HashTag.objects.filter(hashtag=args[0]):
                hashtag_exist.count_hashtag = hashtag_exist.count_hashtag + 1
                hashtag_exist.updated_at = timezone.now()
                hashtag_exist.save()

    def video_author(self, *args):
        author_id_not_exist = VideoAuthor.objects.filter(author_id=args[0]).exists()
        if not author_id_not_exist:
            VideoAuthor.objects.create(
                author_id=args[0], name=args[1], instagram_acc=args[2], total_videos=args[3], followers=args[4]
            )
        else:
            total_videos = VideoID.objects.filter(author_id=args[0]).values_list('id', flat=True)
            print('total videos ', total_videos)
            # VideoAuthor.objects.filter(author_id=args[0]).update(count_videos=5)

    def videos(self, *args):
        author_id_not_exist = VideoID.objects.filter(video_id=args[0]).exists()
        auther_video = VideoAuthor.objects.get(author_id=args[1])
        if not author_id_not_exist:
            VideoID.objects.create(video_id=args[0], video_hashtags=args[2], author_id=auther_video, len_hashtags=len(args[2]))
        else:
            VideoID.objects.filter(author_id=args[0]).update(len_hashtags=len(args[2]), updated_at=timezone.now())

    def handle(self, *args, **options):
        get_hashtag = HashTag.objects.values('hashtag').order_by('-updated_at')[:10]
        self.stdout.write(f'get hashtag from database {get_hashtag}')
        # loop for update there time for future use.
        for x in get_hashtag:
            HashTag.objects.filter(hashtag=x['hashtag']).update(updated_at=timezone.now())
            print(f"---> datetime update {x['hashtag']}")
        random_hashtag = random.choice(get_hashtag)['hashtag']
        print(random_hashtag)
        with TikTokApi() as API:
            for api in API.hashtag(random_hashtag).videos(count=45):
                hashtags = []
                api_dict = api.as_dict
                for hashtag in api_dict['textExtra']:
                    self.hashtags(hashtag['hashtagName'])
                    hashtags.append(hashtag['hashtagName'])
                self.video_author(api_dict['author']['id'], api_dict['author']['nickname'], api_dict['author']['signature'].split(':')[-1], api_dict['authorStats']['videoCount'], api_dict['authorStats']['followerCount'] )
                self.videos(api_dict['id'], api_dict['author']['id'], hashtags)
                


        
        