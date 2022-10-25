import random
import string
from django.utils import timezone
from django.core.management.base import BaseCommand
from TikTokApi import TikTokApi
from video_editor.models import VideoID



class Command(BaseCommand):
    help = "Download TIKTOK videos."

    @property
    def video_id(self):
        video_id = VideoID.objects.values('video_id').order_by('-updated_at')[:10]
        return random.choice(video_id)['video_id']
        
    def handle(self, *args, **options):
        with TikTokApi() as api:
            for x in range(10):
                # print(VideoID.objects.get(video_id=self.video_id).updated_at)
                video = api.video(id=str(self.video_id))
                video_byte = video.bytes()
                random_name = "".join((random.choice(string.ascii_letters) for i in range(10)))
                with open(f"videos/{random_name}.mp4", 'wb') as file:
                    file.write(video_byte)
                    # print('video downloadeded...')
                # x = VideoID.objects.filter(video_id=self.video_id).update(updated_at=timezone.now())
                x = VideoID.objects.get(video_id=self.video_id)
                x.updated_at = timezone.now()
                x.save()
                # print(self.video_id)
                # print(VideoID.objects.get(video_id=self.video_id).updated_at, timezone.now())


        
        