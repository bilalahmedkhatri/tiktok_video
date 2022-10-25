from multiprocessing import set_forkserver_preload
import os
import random
import string
from pathlib import Path
from django.utils import timezone
from django.core.management.base import BaseCommand
# from video_editor.models import VideoID



class Command(BaseCommand):
    help = "Download TIKTOK videos."
    
    @property
    def random_name_generator(self) -> str:
        return "".join([random.choice(string.ascii_letters) for s in range(10)]) 
    
    
    # dynamic directory name generator
    @property
    def directory_name(self) -> str:
        cur_dir = os.getcwd()
        create_dir = r"%s/media/compile_videos" % (cur_dir)
        return create_dir
    
    @property
    def get_vid_name(self) -> list:
        get_videos = r"%s/videos" % (os.getcwd())
        return [str(f) for f in Path(get_videos).glob("*.mp4")]
        #only names for
        # return [str(os.path.basename(f.name)) for f in Path(get_videos).glob("*.mp4")]
    
    @property
    def create_txt_file(self):
        file_names = self.get_vid_name
        file_path = r"%s/text_file/%s.txt" % (self.directory_name, self.random_name_generator)
        print(file_path)
        with open(file_path, "w") as create_file:
            for name in file_names:
                create_file.write(f"file {name} \n")
            create_file.close()
        
        # images_formats = ['mp4',]
        # images = []
        # for l in os.listdir():
        #     d = r"%s/%s" % (os.getcwd(), l)
        #     if os.path.isdir(d):
        #         for img_frt in images_formats:
        #             img_format = f"*.{img_frt}"
        #             for b in Path(d).glob(img_format):
        #                 if str(b) not in images:
        #                     images.append(str(b))
        # select_image = random.sample(images, 1)
        # return ''.join(select_image)

    
    
    def videos(self) -> list:
        pass
    
    
    def update_database(self):
        pass
    
    
    def concatenate_videos(self):
        pass
    
    
    def handle(self, *args, **options):
        self.create_txt_file